from django import template
register= template.Library()

@register.filter(name='trun')
def trun(value,n):
    return value[0:n]
