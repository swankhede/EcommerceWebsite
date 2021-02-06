from django import template
register = template.Library()

@register.filter(name='total')

def total(val,arg):
    return int(val)+int(arg)