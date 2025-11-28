from django.contrib import admin

from common.models import Comment
from photos.models import Photo


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass
