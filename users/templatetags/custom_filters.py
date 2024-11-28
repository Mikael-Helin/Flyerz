from django import template

register = template.Library()

@register.filter
def friendship_key(friendship_map, key):
    return friendship_map.get(key, None)

