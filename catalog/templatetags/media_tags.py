from django import template
from django.conf import settings

register = template.Library()

@register.filter
def media_path(value):
    """
    Фильтр для добавления полного пути к медиафайлу.
    """
    if value:
        return f'{settings.MEDIA_URL}{value}'
    return '#'
