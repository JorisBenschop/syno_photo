import shutil
import logging
import pathlib
import django
import pandas as pd
import filecmp
from datetime import datetime, timedelta

django.setup()

pd.options.display.width = 0

logger = logging.getLogger(__name__)

logger.info("START")

from process import glob_md5

df_list = []
cmd_file = "/volume1/photo_sorted/move.sh"

# writer = open(cmd_file, "w")

for count, unit_list in enumerate(glob_md5()):
    logger.info(f"***** {count} ****")

    if count > 200000:
        break

    l = len(unit_list)
    if l == 0:
        raise NotImplementedError()

    if all(["op_datum" in x._path.as_posix() for x in unit_list]):
        logger.info("all items moved")

        continue

    inclusion_list = []
    for unit in unit_list:
        if "series" in unit._path.as_posix():
            d = unit.as_dict()
            d["ignore_reason"] = "series"
        elif unit.date is None:
            d = unit.as_dict()
            d["ignore_reason"] = "no_date"
            df_list.append(d)
        else:
            inclusion_list.append(unit)

    if len(inclusion_list) == 0:
        logger.info("nothing to include")
        continue

    if all(["op_datum" in x._path.as_posix() for x in inclusion_list]):
        logger.info("all included are already moved")
        continue

    # re-order based on mfile time
    inclusion_list = sorted(inclusion_list, key=lambda mt: mt.file_timestamp)

    # get the first file
    first = inclusion_list[0]
    d = first.as_dict()
    d["primary"] = True

    # set the new file location
    new_loc = first.new_location
    if new_loc.exists():
        if not filecmp.cmp(new_loc, first.current_location, shallow=False):
            collision = True
            d["ignore_reason"] = "file_collision"
            collision_name = new_loc.stem + f"_collision_{first._path.name}"
            d["new_name_collision"] = collision_name
            collision_loc = new_loc.parent / collision_name
            if collision_loc.exists():
                continue
        else:
            collision = False
            collision_loc = None
    else:
        collision = False
        collision_loc = None
        new_loc.parent.mkdir(exist_ok=True, parents=True)

    # move the primary
    df_list.append(d)
    if collision_loc:
        final_loc = collision_loc
    else:
        final_loc = new_loc

    logger.info(f"moving {first.current_location} --> {final_loc}")
    try:
        first.current_location.rename(final_loc)
    except OSError:
        shutil.copy2(first.current_location, final_loc)
        if final_loc.exists():
            first.current_location.unlink()
        x = 1

    # perform the re-location of all dups
    if l > 1:
        for i, dup in enumerate(inclusion_list[1:]):
            d = unit.as_dict()
            d["primary"] = False
            if collision:
                d["ignore_reason"] = "file_collision"
                d["new_name_collision"] = collision_name
                new_dup = pathlib.Path(f"{collision_loc}.duplicate.{i+1}")
            else:
                new_dup = pathlib.Path(f"{new_loc}.duplicate.{i+1}")
            if new_dup.exists():
                if not filecmp.cmp(new_dup, dup.current_location):
                    continue

            df_list.append(d)
            dup.current_location.rename(new_dup)
            logger.info(f"moving {dup.current_location} --> {new_dup}")
            x = 1
            # writer.write(f'mv "{dup.current_location}" "{new_dup}"\n')


df = pd.DataFrame(df_list)
df.to_csv("/volume1/photo_sorted/results2.tab", sep="\t")


"""
f = Unit.objects.first()
logger.debug(f.mtime)

first = f.mtime - timedelta(days=10)

last = f.mtime + timedelta(days=10)

xx = Unit.objects.filter(mtime__gt=first, mtime__lt=last).order_by("mtime")
logger.info(f"{len(xx)}")
x = 1
"""
