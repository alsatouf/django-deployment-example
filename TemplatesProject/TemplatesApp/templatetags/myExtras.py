from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value, par):
    """
        this cuts out all values of par from the string
    """
    return value.replace(par, '')

#register.filter('cut', cut)