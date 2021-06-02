from django import template
register= template.Library()

@register.filter(name='trun') #This is a decorater
def trun(value,n):
    return value[0:n]
#def trun5(value):    #Another way to define custom filters
    #name=value[0:5]
    #return name
    #register.filter('alias_name',trun5)
