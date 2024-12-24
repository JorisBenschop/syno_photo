from pathlib import Path
from django.db import models
from django.conf import settings
from datetime import datetime


class TimeStampField(models.BigIntegerField):
    def get_prep_value(self, value, *args, **kwargs):
        value2 = int(datetime.timestamp(value))
        return super().get_prep_value(value2, *args, **kwargs)

    def from_db_value(self, value, *args, **kwargs):
        return datetime.fromtimestamp(value)


class UserInfo(models.Model):
    uid = models.BigIntegerField(unique=True, blank=True, null=True)
    name = models.TextField()
    config = models.TextField()  # This field type is a guess.
    enable = models.BooleanField()

    class Meta:
        managed = False
        db_table = "user_info"

    @property
    def basedir(self):
        start = self.name
        if start.startswith("/"):
            full = Path(start)
        else:
            full = Path("/var/services/homes") / start / "Photos"
        if full.exists() and full.is_dir():
            return full
        raise FileNotFoundError(f"path {full} does not exist")


class ExtendedFolderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user")


class Folder(models.Model):
    name = models.TextField()
    parent = models.ForeignKey("self", models.DO_NOTHING, db_column="parent")
    mtime = TimeStampField()
    user = models.ForeignKey(UserInfo, models.DO_NOTHING, db_column="id_user")

    objects = ExtendedFolderManager()

    @property
    def foldername(self):
        return self.user.basedir / self.name.lstrip("/")

    class Meta:
        managed = False
        db_table = "folder"


class ExtendedUnitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("folder", "folder__user")


class Unit(models.Model):
    type = models.SmallIntegerField()
    item_type = models.SmallIntegerField()
    filename = models.TextField()
    filesize = models.BigIntegerField()
    # createtime = models.BigIntegerField()
    mtime = TimeStampField()
    takentime = TimeStampField()
    duplicate_hash = models.TextField()
    # cache_key = models.TextField()
    resolution = models.TextField()  # This field type is a guess.
    # index_stage = models.SmallIntegerField()
    version = models.BigIntegerField()

    normalized_filename = models.TextField()
    is_major = models.BooleanField()

    folder = models.ForeignKey(Folder, models.DO_NOTHING, db_column="id_folder")
    user = models.ForeignKey(UserInfo, models.DO_NOTHING, db_column="id_user")

    objects = ExtendedUnitManager()

    class Meta:
        managed = False
        db_table = "unit"

    def __str__(self):
        return f"JPEG {self.filename}"

    @property
    def full_path(self):
        p = self.folder.foldername / self.filename
        if p.exists() and p.is_file():
            return p
        raise FileNotFoundError(f"cannot find {p}")
