from django import template
register= template.Library()

@register.filter(name='trun') #This is a decorater
def trun(value,n):
    return value[0:n]
