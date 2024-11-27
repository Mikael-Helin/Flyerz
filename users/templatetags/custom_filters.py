from django import template

register = template.Library()

@register.filter
def friendship_key(friendship_map, args):
    """
    Custom filter to fetch a value from friendship_map
    using a concatenated key (e.g., 'user1-user2').
    """
    user1, user2 = args.split('-')
    key = f"{user1}-{user2}"
    return friendship_map.get(key, None)
