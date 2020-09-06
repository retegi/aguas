from django import template
from aguas.aguas.applications import home

@register.simple_tag
def show_results(home):
    info = home.home.all()
    return {'info': info}