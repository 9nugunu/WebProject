import markdown
from django import template
from django.utils.safestring import mark_safe
register = template.Library()

# 게시글 번호 자동 맞춤
@register.filter
def sub(value, arg):
    return value - arg

# 마크다운 문법 활용 가능
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))