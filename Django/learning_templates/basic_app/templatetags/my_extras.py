from django import templates

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts our all values of "arg" from the string!
    """
    return value.replace(arg,'')

"""Below is another way that you can do this instead of @register"""
# register.filter('cut',cut)
