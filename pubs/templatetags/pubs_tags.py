from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def remove_facet(context, field, value):
    r = context['request'].GET.copy()
    r.getlist('selected_facets').remove( '%s_exact:%s' % (field, value) )
    # reset page
    if r.has_key('page'):
        del r['page']
    return '?%s' % r.urlencode()

@register.simple_tag(takes_context=True)
def add_facet(context, field, value):
    r = context['request'].GET.copy()
    if not r.has_key('selected_facets'):
        r['selected_facets'] = '%s_exact:%s' % (field, value)
    else:
        r.getlist('selected_facets').append( '%s_exact:%s' % (field, value) )
    # reset page
    if r.has_key('page'):
        del r['page']
    return '?%s' % r.urlencode()

@register.simple_tag(takes_context=True)
def change_page(context, page):
    r = context['request'].GET.copy()
    r['page'] = page
    return '?%s' % r.urlencode()
