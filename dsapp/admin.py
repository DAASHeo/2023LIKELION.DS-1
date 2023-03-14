from django.contrib import admin
from .models import Post, Comment, babyLion, failure
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(babyLion)
admin.site.register(failure)