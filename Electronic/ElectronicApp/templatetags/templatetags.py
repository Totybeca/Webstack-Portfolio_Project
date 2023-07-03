import os
from django import template
from django.core.files.storage import default_storage

register = template.Library()


@register.filter
def filename(value):
    return os.path.basename(value.file.name)


@register.filter
def file_exists(value):
    if default_storage.exists(value):
        return True
    else:
        return False