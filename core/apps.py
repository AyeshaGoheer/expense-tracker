from django.contrib.admin.apps import AdminConfig


class ETAdminConfig(AdminConfig):
    default_site = 'core.admin.ETAdminSite'
