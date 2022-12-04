from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _

# Create your models here.
class BlogPost(models.Model):
    author =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,help_text="The author of the post")
    title = models.CharField(max_length=255,help_text="Enter the title of the post")
    post = models.TextField(help_text="Enter your post content")

    class Meta:
        default_related_name ="blog_posts"
        order_with_respect_to ="title"
        verbose_name = _("blog_post")
        verbose_name_plural = _("blog_posts")