from django import template

register = template.Library()

def cut_fn(value, arg):
    """
    cuts all values of "arg" from the string
    """
    return value.replace(arg,'')

register.filter('cutfn',cut_fn)
