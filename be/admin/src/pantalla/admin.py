from django.contrib import admin
from django.contrib.postgres import fields  # if django < 3.1
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import *
from django.apps import apps


class ModelAdmin(admin.ModelAdmin):
    search_fields = (
        "description",
    )

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[0][0] == 'add_item':
                return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[1][0] == 'change_item':
                return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if request.user.groups.filter(name='travelexpert').exists():
            if self.model._meta.permissions is not None and len(self.model._meta.permissions) > 0 and self.model._meta.permissions[2][0] == 'delete_item':
                return True
        return False

    def get_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.has_perm('items.read_item'):
            return [f.name for f in self.model._meta.fields]
        return super(ModelAdmin, self).get_fields(
            request, obj=obj
        )


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        # self.list_display = [field.description for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)
    formfield_overrides = {
        models.TextField: {'widget': JSONEditorWidget},
    }
    

modellist = apps.get_models()
for model in modellist:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin, ), {})
    admin_class_perm = type('AdminClass', (admin_class, ModelAdmin, ), {})

    try:
        admin.site.register(model, admin_class_perm)
    except Exception as e:
        pass
