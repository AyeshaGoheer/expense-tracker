from django import template

register = template.Library()


@register.filter
def tag_to_color(tag):
    color_labels = ['primary', 'success', 'danger', 'warning']
    hashed_tag = hash(tag) + 100
    color_index = hashed_tag % len(color_labels)
    return color_labels[color_index]
