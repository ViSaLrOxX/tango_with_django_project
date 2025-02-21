from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    """
    Returns a dictionary with all categories to be used in templates.
    If `current_category` is passed, it highlights the active category.
    """
    return {'categories': Category.objects.all(), 'current_category': current_category}
