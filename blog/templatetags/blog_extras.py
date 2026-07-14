from django import template
from django.utils.html import format_html
from blog.models import Post
register = template.Library()


@register.filter
def author_details(author, current_user):
    """
    Displays the author's full name if available.
    Appends '(Me)' if the current logged-in user is the author.
    """

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = author.username

    if current_user.is_authenticated and author == current_user:
        return f"{name} (Me)"

    return name
@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)



@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return '</div>'

@register.filter
def wordcount(content):
    """
    Returns the number of words in the supplied text.
    """
    if not content:
        return 0

    return len(content.split())
@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row{}',extra_classes)
  
@register.inclusion_tag("blog/recent-posts.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]

    return {
        "title": "Recent Posts",
        "posts": posts,
    }
@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col {}">', extra_classes)
@register.simple_tag
def endcol():
    return format_html("</div>")