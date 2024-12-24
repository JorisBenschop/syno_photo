# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AclPermission(models.Model):
    fullpath = models.TextField()
    permission = models.TextField()
    type = models.SmallIntegerField()
    id_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acl_permission'


class Activity(models.Model):
    id_user = models.IntegerField()
    id_album = models.IntegerField()
    type = models.SmallIntegerField()
    create_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activity'


class Address(models.Model):
    lang = models.SmallIntegerField()
    admin = models.SmallIntegerField()
    level = models.ForeignKey('Administrative', models.DO_NOTHING, db_column='level')
    value = models.TextField()
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'address'


class Administrative(models.Model):
    value = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'administrative'


class Album(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    name = models.TextField()
    type = models.SmallIntegerField()
    shared = models.BooleanField()
    create_time = models.BigIntegerField()
    cover = models.IntegerField()
    sort_by = models.SmallIntegerField()
    sort_direction = models.SmallIntegerField()
    normalized_name = models.TextField()
    version = models.BigIntegerField()
    passphrase_share = models.OneToOneField('Share', models.DO_NOTHING, db_column='passphrase_share', blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True)
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'album'


class Aperture(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'aperture'


class BackgroundTask(models.Model):
    operation = models.SmallIntegerField()
    status = models.SmallIntegerField()
    created_time = models.BigIntegerField()
    modified_time = models.BigIntegerField()
    total = models.BigIntegerField()
    completion = models.BigIntegerField()
    error = models.BigIntegerField()
    id_user = models.IntegerField()
    extra_info = models.TextField(blank=True, null=True)
    payload = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'background_task'


class BurstAdditional(models.Model):
    grouping_key = models.TextField()
    sequence = models.BigIntegerField()
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'burst_additional'


class Camera(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'camera'


class CheckAlbumTask(models.Model):
    id_user = models.IntegerField()
    id_group = models.IntegerField()
    id_folder = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'check_album_task'


class Cluster(models.Model):
    id_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='id_person', blank=True, null=True)
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'cluster'


class ConditionAlbum(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    name = models.TextField()
    type = models.SmallIntegerField()
    shared = models.BooleanField()
    create_time = models.BigIntegerField()
    cover = models.IntegerField()
    sort_by = models.SmallIntegerField()
    sort_direction = models.SmallIntegerField()
    normalized_name = models.TextField()
    version = models.BigIntegerField()
    passphrase_share = models.ForeignKey('Share', models.DO_NOTHING, db_column='passphrase_share', blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True)
    condition = models.TextField(blank=True, null=True)  # This field type is a guess.
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_album'


class Config(models.Model):
    key = models.TextField(primary_key=True)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'config'


class DeleteAlbum(models.Model):
    id_normal_album = models.IntegerField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'delete_album'


class DeleteConditionAlbum(models.Model):
    id_condition_album = models.IntegerField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'delete_condition_album'


class DeleteItem(models.Model):
    id_item = models.IntegerField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'delete_item'


class ExposureTime(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'exposure_time'


class Face(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    bounding_box = models.TextField()  # This field type is a guess.
    landmark = models.TextField()  # This field type is a guess.
    feature = models.BinaryField()
    picture = models.TextField(blank=True, null=True)  # This field type is a guess.
    score = models.IntegerField()
    id_unit = models.IntegerField(blank=True, null=True)
    ref_id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='ref_id_unit')
    id_person_group = models.ForeignKey('PersonGroup', models.DO_NOTHING, db_column='id_person_group', blank=True, null=True)
    id_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='id_person', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'face'


class FileOperationError(models.Model):
    id_task = models.ForeignKey(BackgroundTask, models.DO_NOTHING, db_column='id_task')
    target_type = models.SmallIntegerField()
    target_id = models.IntegerField()
    reason = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'file_operation_error'
        unique_together = (('id_task', 'target_type', 'target_id'),)


class FileOperationTask(models.Model):
    id_task = models.OneToOneField(BackgroundTask, models.DO_NOTHING, db_column='id_task', primary_key=True)
    target_folder_id = models.IntegerField()
    policy = models.SmallIntegerField()
    id_user = models.IntegerField()
    id_item = models.TextField()  # This field type is a guess.
    id_folder = models.TextField()  # This field type is a guess.
    target_folder_id_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file_operation_task'


class Filter(models.Model):
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit')
    id_filter = models.IntegerField()
    filter_type = models.TextField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'filter'
        unique_together = (('id_unit', 'id_filter', 'filter_type', 'id_user'),)


class FocalLength(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'focal_length'


class Folder(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    name = models.TextField()
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent')
    name_for_sort = models.TextField()
    permission = models.TextField(blank=True, null=True)
    mtime = models.BigIntegerField()
    passphrase_share = models.OneToOneField('Share', models.DO_NOTHING, db_column='passphrase_share', blank=True, null=True)
    shared = models.BooleanField()
    sort_by = models.SmallIntegerField()
    sort_direction = models.SmallIntegerField()
    permission_parent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'folder'


class FolderOperationError(models.Model):
    id_task = models.OneToOneField(BackgroundTask, models.DO_NOTHING, db_column='id_task', primary_key=True)
    target_id = models.IntegerField()
    reason = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'folder_operation_error'
        unique_together = (('id_task', 'target_id'),)


class FolderOperationTask(models.Model):
    id_folder = models.IntegerField(primary_key=True)
    id_task = models.ForeignKey(BackgroundTask, models.DO_NOTHING, db_column='id_task')

    class Meta:
        managed = False
        db_table = 'folder_operation_task'


class GeneralTag(models.Model):
    id_user = models.IntegerField()
    name = models.TextField()
    count = models.IntegerField()
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'general_tag'


class Geocoding(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    grouping_key = models.TextField()
    level_1 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_1', blank=True, null=True)
    level_2 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_2', blank=True, null=True)
    level_3 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_3', blank=True, null=True)
    level_4 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_4', blank=True, null=True)
    level_5 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_5', blank=True, null=True)
    level_6 = models.ForeignKey(Administrative, models.DO_NOTHING, db_column='level_6', blank=True, null=True)
    admin_1 = models.SmallIntegerField(blank=True, null=True)
    admin_2 = models.SmallIntegerField(blank=True, null=True)
    admin_3 = models.SmallIntegerField(blank=True, null=True)
    admin_4 = models.SmallIntegerField(blank=True, null=True)
    admin_5 = models.SmallIntegerField(blank=True, null=True)
    admin_6 = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocoding'


class GeocodingInfo(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    lang = models.SmallIntegerField()
    first_level = models.TextField()
    second_level = models.TextField()
    country = models.TextField()
    id_geocoding = models.ForeignKey(Geocoding, models.DO_NOTHING, db_column='id_geocoding', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocoding_info'


class GroupInfo(models.Model):
    gid = models.BigIntegerField(unique=True, blank=True, null=True)
    name = models.TextField()
    enable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'group_info'


class IndexQueue(models.Model):
    id_user = models.IntegerField()
    id_unit = models.IntegerField()
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    task = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'index_queue'


class Iso(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'iso'


class Item(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'item'


class Lens(models.Model):
    name = models.TextField(unique=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'lens'


class LiveAdditional(models.Model):
    grouping_key = models.TextField()
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'live_additional'


class ManyItemHasManyNormalAlbum(models.Model):
    sequence = models.FloatField()
    item_provider_id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='item_provider_id_user', blank=True, null=True)
    id_item = models.OneToOneField(Item, models.DO_NOTHING, db_column='id_item', primary_key=True)
    id_normal_album = models.ForeignKey('NormalAlbum', models.DO_NOTHING, db_column='id_normal_album')
    album_id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='album_id_user')

    class Meta:
        managed = False
        db_table = 'many_item_has_many_normal_album'
        unique_together = (('id_item', 'id_normal_album'),)


class ManyUnitHasManyAdministrative(models.Model):
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', primary_key=True)
    id_administrative = models.IntegerField()
    id_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'many_unit_has_many_administrative'
        unique_together = (('id_unit', 'id_administrative'),)


class ManyUnitHasManyGeneralTag(models.Model):
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', primary_key=True)
    id_general_tag = models.ForeignKey(GeneralTag, models.DO_NOTHING, db_column='id_general_tag')

    class Meta:
        managed = False
        db_table = 'many_unit_has_many_general_tag'
        unique_together = (('id_unit', 'id_general_tag'),)


class ManyUnitHasManyPerson(models.Model):
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', primary_key=True)
    id_person = models.IntegerField()
    id_user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'many_unit_has_many_person'
        unique_together = (('id_unit', 'id_person'),)


class Metadata(models.Model):
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)
    description = models.TextField()
    orientation = models.SmallIntegerField()
    focal_length = models.TextField()
    iso = models.TextField()
    exposure_time = models.TextField()
    aperture = models.TextField()
    lens = models.TextField()
    camera = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    flash = models.SmallIntegerField(blank=True, null=True)
    orientation_original = models.SmallIntegerField()
    rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'metadata'


class MobileConfig(models.Model):
    uuid = models.TextField()
    config = models.TextField()

    class Meta:
        managed = False
        db_table = 'mobile_config'


class NormalAlbum(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    name = models.TextField()
    type = models.SmallIntegerField()
    shared = models.BooleanField()
    create_time = models.BigIntegerField()
    cover = models.IntegerField()
    sort_by = models.SmallIntegerField()
    sort_direction = models.SmallIntegerField()
    normalized_name = models.TextField()
    version = models.BigIntegerField()
    passphrase_share = models.ForeignKey('Share', models.DO_NOTHING, db_column='passphrase_share', blank=True, null=True)
    item_count = models.IntegerField(blank=True, null=True)
    cant_migrate_condition = models.TextField(blank=True, null=True)  # This field type is a guess.
    condition = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.SmallIntegerField()
    start_time = models.BigIntegerField(blank=True, null=True)
    end_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normal_album'


class Notification(models.Model):
    id_user = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='id_user', primary_key=True)
    event = models.TextField()
    target_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'
        unique_together = (('id_user', 'event', 'target_id'),)


class OneFilterHasManyUnit(models.Model):
    id_unit = models.OneToOneField('Unit', models.DO_NOTHING, db_column='id_unit', primary_key=True)
    id_aperture = models.IntegerField(blank=True, null=True)
    id_camera = models.IntegerField(blank=True, null=True)
    id_exposure_time = models.IntegerField(blank=True, null=True)
    id_flash = models.IntegerField(blank=True, null=True)
    id_focal_length = models.IntegerField(blank=True, null=True)
    id_folder = models.IntegerField(blank=True, null=True)
    id_iso = models.IntegerField(blank=True, null=True)
    id_item_type = models.IntegerField(blank=True, null=True)
    id_lens = models.IntegerField(blank=True, null=True)
    id_takentime = models.IntegerField(blank=True, null=True)
    id_user = models.IntegerField(blank=True, null=True)
    id_rating = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'one_filter_has_many_unit'


class Person(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    name = models.TextField()
    hidden = models.BooleanField()
    custom_cover = models.BooleanField()
    cover = models.ForeignKey(Face, models.DO_NOTHING, db_column='cover', blank=True, null=True)
    normalized_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'person'


class PersonGroup(models.Model):
    weight = models.IntegerField(blank=True, null=True)
    feature = models.BinaryField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    id_cluster = models.ForeignKey(Cluster, models.DO_NOTHING, db_column='id_cluster', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_group'


class PersonItemCount(models.Model):
    id_person = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()
    item_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_item_count'
        unique_together = (('id_person', 'id_user'),)


class PersonMigrationMapping(models.Model):
    id_user = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='id_user', primary_key=True)
    id_person_source = models.IntegerField()
    id_person = models.IntegerField()
    named_by_migration = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'person_migration_mapping'
        unique_together = (('id_user', 'id_person_source'),)


class SearchTimeline(models.Model):
    id_item = models.IntegerField(primary_key=True)
    id_user = models.IntegerField()
    item_type = models.SmallIntegerField()
    unit_type = models.SmallIntegerField()
    takentime = models.BigIntegerField()
    id_unit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'search_timeline'


class Share(models.Model):
    passphrase = models.TextField(primary_key=True)
    privacy_type = models.SmallIntegerField()
    modified_time = models.BigIntegerField()
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    expired_time = models.BigIntegerField()
    hashed_password = models.TextField()
    enable = models.BooleanField()
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'share'


class SharePermission(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    permission = models.SmallIntegerField()
    target_type = models.SmallIntegerField()
    target_id = models.IntegerField()
    passphrase_share = models.ForeignKey(Share, models.DO_NOTHING, db_column='passphrase_share')

    class Meta:
        managed = False
        db_table = 'share_permission'
        unique_together = (('passphrase_share', 'target_type', 'target_id'),)


class Takentime(models.Model):
    takentime_day = models.TextField(unique=True)
    takentime_month = models.TextField()
    takentime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'takentime'


class TeamLibraryFolderHasManySorting(models.Model):
    id_user = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='id_user', primary_key=True)
    id_folder = models.ForeignKey(Folder, models.DO_NOTHING, db_column='id_folder')
    sort_by = models.SmallIntegerField()
    sort_direction = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'team_library_folder_has_many_sorting'
        unique_together = (('id_user', 'id_folder'),)


class TeamLibraryGroupPermission(models.Model):
    id_group = models.OneToOneField(GroupInfo, models.DO_NOTHING, db_column='id_group', primary_key=True)
    permission = models.SmallIntegerField()
    auto_backup = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'team_library_group_permission'


class TeamLibraryUserPermission(models.Model):
    id_user = models.OneToOneField('UserInfo', models.DO_NOTHING, db_column='id_user', primary_key=True)
    permission = models.SmallIntegerField()
    auto_backup = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'team_library_user_permission'


class ThumbPreview(models.Model):
    picture = models.TextField()  # This field type is a guess.
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit')

    class Meta:
        managed = False
        db_table = 'thumb_preview'


class Thumbnail(models.Model):
    type = models.SmallIntegerField()
    status = models.SmallIntegerField()
    id_unit = models.ForeignKey('Unit', models.DO_NOTHING, db_column='id_unit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thumbnail'


class Unit(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    type = models.SmallIntegerField()
    item_type = models.SmallIntegerField()
    filename = models.TextField()
    filesize = models.BigIntegerField()
    createtime = models.BigIntegerField()
    mtime = models.BigIntegerField()
    takentime = models.BigIntegerField()
    duplicate_hash = models.TextField()
    cache_key = models.TextField()
    resolution = models.TextField()  # This field type is a guess.
    index_stage = models.SmallIntegerField()
    version = models.BigIntegerField()
    id_geocoding = models.ForeignKey(Geocoding, models.DO_NOTHING, db_column='id_geocoding', blank=True, null=True)
    id_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='id_item')
    mobile_cache_mtime = models.BigIntegerField()
    reindex_flag = models.SmallIntegerField()
    normalized_filename = models.TextField()
    is_major = models.BooleanField()
    id_folder = models.ForeignKey(Folder, models.DO_NOTHING, db_column='id_folder')

    class Meta:
        managed = False
        db_table = 'unit'
        unique_together = (('id', 'id_user'),)


class UserFlag(models.Model):
    id_user = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='id_user')
    flag = models.TextField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_flag'


class UserInfo(models.Model):
    uid = models.BigIntegerField(unique=True, blank=True, null=True)
    name = models.TextField()
    config = models.TextField()  # This field type is a guess.
    enable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_info'


class VersionTime(models.Model):
    version = models.BigAutoField(primary_key=True)
    modified_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'version_time'


class VideoAdditional(models.Model):
    duration = models.BigIntegerField()
    video_info = models.TextField()  # This field type is a guess.
    audio_info = models.TextField()  # This field type is a guess.
    id_unit = models.OneToOneField(Unit, models.DO_NOTHING, db_column='id_unit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_additional'


class VideoConvert(models.Model):
    duration = models.BigIntegerField()
    quality = models.TextField()
    video_info = models.TextField()  # This field type is a guess.
    audio_info = models.TextField()  # This field type is a guess.
    id_unit = models.ForeignKey(Unit, models.DO_NOTHING, db_column='id_unit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'video_convert'
