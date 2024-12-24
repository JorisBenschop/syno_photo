import django
import logging
import pathlib
import exif
from datetime import datetime
from pprint import pprint

django.setup()
logger = logging.getLogger(__name__)


BASEDIR = "/volume1/photo"
# BASEDIR = "/volume1/photo/MobileBackup/joris/iPad Joris"
basepath = pathlib.Path(BASEDIR)
GLOB_RE = "**/*"

BASE_NEW = pathlib.Path("/volume1/photo/sorted")

DATE_MINIMUM = datetime(1990, 1, 1, 0, 0)

from syno_photo.models import Unit, Folder


class JPGImage:

    suffix = [".jpeg", ".jpg", ".crw", ".cr2" ".heic"]
    suffix_with_exif = [
        ".jpeg",
        ".jpg",
    ]

    db_record = None
    exif = None
    date_source = None
    _date = None

    def __repr__(self):
        return f"{type(self).__name__}: {self._path}"

    # ================================================================
    # Initialization
    @classmethod
    def from_image_path(cls, image_path: pathlib.Path):
        """"""
        instance = cls()
        instance._path = image_path
        instance._get_database_record()
        instance._load_exif_from_jpg()

    @classmethod
    def from_db_record(cls, unit: Unit):
        """"""
        instance = cls()
        instance.db_record = unit
        instance._path = instance.db_record.full_path
        instance._load_exif_from_jpg()

    def _get_database_record(self):
        """ """
        logger.debug("obtaining SynologyPhotos record.")
        matches = Unit.objects.filter(filename=self._path.name)
        match = [x for x in matches if x.full_path == self._path]
        if len(match) != 1:
            raise NotImplementedError("x")
        match = matches[1]
        if not match:
            raise FileNotFoundError(f"unable to find {self._path} in database")
        self.db_record = match

    def _load_exif_from_jpg(self) -> dict:
        """
        get the EXIF metadata from file and store locally
        """

        if self._path.suffix.lower() not in self.suffix_with_exif:
            return None

        logger.debug(f"processing {self._path}")
        try:
            with self._path.open("rb") as img_io:
                img_meta = exif.Image(img_io)
                if not img_meta.has_exif:
                    logger.warning(f"mising EXIF for {self._path}")
                    return None
                else:
                    logger.debug(f"found EXIF data for {self._path.name}")
                    self.exif = img_meta
        except Exception as e:
            logger.error(f"cannot process {self._path} because {str(e)}")
            raise

        # ================================================================

    def get_duplicates(self):
        unit = self.db_record
        dup = unit.duplicate_hash
        others = Unit.objects.filter(duplicate_hash=dup).exclude(pk=unit.pk)
        if others:
            dups = [self.__class__(existing_record=x) for x in others]
            return dups

    def process(self):
        """
        try to obtain the synology database record, but also the files metadata EXIF itself
        """
        logger.info(f"image {self._path} has date {self.date}")
        logger.info(f"path {self._path}: move to {self.new_location}")
        dups = self.get_duplicates()

    # ============================================================
    @property
    def date(self):
        """get the date from EXIF or db record"""
        if self._date is None:
            if r := self._get_date_from_exif():
                self.date_source = "exif"
                logger.debug(f"using EXIF date for {self._path.name}")
            elif r := self._get_date_from_db():
                logger.debug(f"using DB date for {self._path.name}")
                self.date_source = "db"
            else:
                r = None
            if r is None:
                self._date = "no_date"
            else:
                self._date = r

        if self._date == "no_date":
            return None
        return self._date

    @property
    def file_timestamp(self):
        """
        get the mtime form the file object
        """
        return self._path.stat().st_mtime

    def _get_date_from_exif(self):
        if not self.exif:
            return None
        exif_date_str = self.exif.get("datetime")
        if exif_date_str:
            logger.debug(f"converting {exif_date_str} to datetime object")
            dt = datetime.strptime(exif_date_str, exif.DATETIME_STR_FORMAT)
            if dt < DATE_MINIMUM:
                logger.debug(f"date {dt} is smaller than {DATE_MINIMUM}")
                return None
            return dt
        else:
            return None

    def _get_date_from_db(self):
        logger.debug(f"using DB takentime field {self.db_record.takentime} ")
        dt = self.db_record.takentime
        if dt < DATE_MINIMUM:
            logger.debug(f"date {dt} is smaller than {DATE_MINIMUM}")
            return None
        return dt

    def _get_date_from_file(self):
        file_timestamp = self._path.stat().st_mtime
        dt = datetime.fromtimestamp(file_timestamp)
        logger.debug(f"using file mtime {dt}")
        return dt

    # ============================================================

    @property
    def current_location(self):
        return pathlib.Path(self._path)

    @property
    def new_location(self):
        """
        use the date to find a new location, otherwise keep the old relative location
        """
        if d := self.date:
            subfolder = d.strftime("%Y/%Y_%m")
            new_loc = BASE_NEW / "op_datum" / subfolder / self.new_name
        return new_loc

    @property
    def new_name(self):
        """
        create a standard new name based on the date. This mainly gets rid of the weird
        MD5SUM names of synology and the non-informative IMG_nnnn names from Canon
        """
        n = self._path.name
        base = self.date.strftime("%Y-%m-%d_%H.%M.%S")

        suff = self._path.suffix.lower()
        if suff in self.suffix_with_exif:
            suff = ".jpg"
        elif suff not in self.suffix:
            return n

        return f"{base}{suff}"

    # ============================================================

    def as_dict(self):
        """ """
        d = {
            "id": self.db_record.pk,
            "hash": self.db_record.duplicate_hash,
            "old_name": self._path.name,
            "old_path": self._path.parent.as_posix(),
            "new_name": self.new_name if self.date else "",
            "new_path": self.new_location.parent.as_posix() if self.date else "",
            "date_source": self.date_source,
            "ignore_reason": "",
            "primary": None,
        }
        return d


def glob_checksum():
    """
    get unique checksums, deliver
    """


def glob_md5():
    """
    go through the database, sorted on MD5, then collect groups of records with the same checksum
    """
    processed_md5 = []

    folders = Folder.objects.exclude(name__startswith="/series").filter(user_id=0)
    total = folders.count()

    for counter, folder in enumerate(folders):
        logger.info(f"{counter}/{total} processing folder {folder.foldername}")
        hashes = folder.unit_set.values_list("duplicate_hash", flat=True)

        if len(hashes) == 0:
            logger.info("..empty")
            continue

        for duphash in hashes:
            processed_md5.append(duphash)

            units = Unit.objects.filter(duplicate_hash=duphash)
            dups = []
            for unit in units:
                try:
                    dup = JPGImage(existing_record=unit)
                    dups.append(dup)
                    logger.debug(f"added file {dup._path}")
                except FileNotFoundError:
                    logger.debug(f"cannot find file for {unit}")
            if not dups:
                logger.debug("no files found at all")
                continue

            is_sorted = ["photo/op_datum" in d._path.as_posix() for d in dups]
            if all(is_sorted):
                logger.debug("all existing paths are already OK")
                continue
            elif any(is_sorted):

                continue
            else:
                yield dups


def main():
    """"""
    logging.debug("starting main routine")


#    for item in glob_photos():
#        item.process()


if __name__ == "__main__":
    main()
    logging.debug("last line")
