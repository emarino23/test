# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Catalog(models.Model):
    catalog_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalog'
    def __str__(self):
        return '%s' % (self.description)

class CatalogDetail(models.Model):
    catalog_detail_id = models.IntegerField(primary_key=True)
    catalog = models.ForeignKey(Catalog, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    order = models.IntegerField()
    description = models.CharField(max_length=1024)
    code = models.IntegerField()
    is_active = models.BooleanField()
    value = models.JSONField(blank=True, null=True)
    relation = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_detail'
        unique_together = (('catalog', 'order', 'code', 'description'),)

    def __str__(self):
        return '%s' % (self.description)

class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    contact_name = models.CharField(max_length=64)
    legal_client_type_id = models.BigIntegerField()
    client_type_id = models.BigIntegerField()
    client_dni = models.CharField(unique=True, max_length=32)
    is_owner = models.BooleanField()
    contact_name_2 = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64)
    origin_id = models.BigIntegerField()
    phone = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    birth_date = models.DateField()
    tax_id = models.CharField(
        unique=True, max_length=1024, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    travel_code = models.CharField(max_length=1024, blank=True, null=True)
    lead_passenger = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return '%s' % (self.description)

class Cruise(models.Model):
    cruise_id = models.BigIntegerField(primary_key=True)
    cruise_name = models.CharField(max_length=1024)
    cruise_type = models.CharField(max_length=1024)
    cruise_category = models.CharField(max_length=1024)
    description = models.CharField(max_length=1024, blank=True, null=True)
    owner_name = models.CharField(max_length=1024)
    operator_name = models.CharField(max_length=1024, blank=True, null=True)
    comercial_name = models.CharField(max_length=1024)
    arrival_port = models.CharField(max_length=1024)
    modality = models.CharField(max_length=1024)
    pax = models.CharField(max_length=1024)
    web_page = models.CharField(max_length=1024, blank=True, null=True)
    included = models.CharField(max_length=1024, blank=True, null=True)
    information = models.CharField(max_length=1024, blank=True, null=True)
    guide_number = models.CharField(max_length=1024)
    staff_number = models.CharField(max_length=1024, blank=True, null=True)
    medic = models.CharField(max_length=1024)
    tc = models.CharField(max_length=1024)
    internet = models.CharField(max_length=1024)
    wetsuites = models.CharField(max_length=1024)
    additional_services = models.CharField(
        max_length=1024, blank=True, null=True)
    restrictions = models.CharField(max_length=1024, blank=True, null=True)
    cruise_format = models.CharField(max_length=1024)
    cruise_itinerary = models.CharField(max_length=1024)
    cost = models.CharField(max_length=1024)
    image = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cruise'
    def __str__(self):
        return '%s' % (self.description)


class CruiseDetail(models.Model):
    cruise_detail_id = models.BigIntegerField(primary_key=True)
    cruise = models.ForeignKey(Cruise, models.DO_NOTHING)
    cabine_type = models.CharField(max_length=1024)
    cabine_spec = models.CharField(max_length=1024, blank=True, null=True)
    quantity = models.CharField(max_length=1024)
    net_rate = models.CharField(max_length=1024)

    class Meta:
        managed = False
        db_table = 'cruise_detail'


class Day(models.Model):
    day_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    key_activity_id = models.BigIntegerField()
    day_name = models.CharField(max_length=1024, blank=True, null=True)
    day_description = models.CharField(max_length=1024, blank=True, null=True)
    day_previous = models.CharField(max_length=1024, blank=True, null=True)
    # This field type is a guess.
    experiences = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    transport_id = models.IntegerField()
    day_observation = models.CharField(max_length=1024, blank=True, null=True)
    day_next = models.CharField(max_length=1024, blank=True, null=True)
    meals = models.CharField(max_length=1024, blank=True, null=True)
    tour_detail = models.ForeignKey('TourDetail', models.DO_NOTHING)
    # This field type is a guess.
    props = models.TextField(blank=True, null=True)
    option_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day'
    def __str__(self):
        return '%s' % (self.description)


class DayDetail(models.Model):
    day_detail_id = models.IntegerField(primary_key=True)
    service_id = models.IntegerField()
    experience_id = models.IntegerField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    day = models.ForeignKey(Day, models.DO_NOTHING)
    destination_id = models.IntegerField()
    tour_id = models.IntegerField()
    service_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_detail'
        unique_together = (('day', 'experience_id', 'service_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Media(models.Model):
    media_id = models.BigIntegerField()
    resource_id = models.CharField(max_length=1024)
    business_type = models.BigIntegerField()
    buisness_id = models.BigIntegerField(blank=True, null=True)
    media_type = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'media'


class NetRate(models.Model):
    net_rate_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    # This field type is a guess.
    final_detail = models.TextField(blank=True, null=True)
    tour = models.ForeignKey('Tour', models.DO_NOTHING)
    description = models.CharField(max_length=1024, blank=True, null=True)
    has_approbed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'net_rate'
    def __str__(self):
        return '%s' % (self.description)


class Tour(models.Model):
    tour_id = models.IntegerField(primary_key=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    destination_country_id = models.IntegerField(blank=True, null=True)
    accomodation_type_id = models.IntegerField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    contact_agent = models.ForeignKey(
        'User', models.DO_NOTHING, db_column='contact_agent')
    pasengers = models.IntegerField(blank=True, null=True)
    days = models.IntegerField(blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    client = models.ForeignKey(Client, models.DO_NOTHING)
    detail = models.JSONField(blank=True, null=True)
    match = models.CharField(max_length=1024, blank=True, null=True)
    tour_state_id = models.IntegerField()
    destinations = models.JSONField()
    rooms = models.CharField(max_length=1024)
    playlist_slug = models.CharField(max_length=1024, blank=True, null=True)
    reproductions = models.BigIntegerField(blank=True, null=True)
    services = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'

    def __str__(self):
        return '%s' % (self.description)

class TourDetail(models.Model):
    tour = models.ForeignKey(Tour, models.DO_NOTHING)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    detail = models.TextField()  # This field type is a guess.
    tour_detail_id = models.IntegerField(primary_key=True)
    destination_id = models.IntegerField()
    exploration_days = models.IntegerField()
    destination_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_detail'
        unique_together = (('tour', 'destination_id', 'destination_index'),)


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    firstname = models.CharField(max_length=16, blank=True, null=True)
    lastname = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(max_length=16, blank=True, null=True)
    password = models.CharField(max_length=1024, blank=True, null=True)
    identification = models.CharField(max_length=16)
    state = models.BigIntegerField()
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    confirmation = models.CharField(max_length=1024)
    user_type_id = models.BigIntegerField(blank=True, null=True)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return '%s' % (self.description)
