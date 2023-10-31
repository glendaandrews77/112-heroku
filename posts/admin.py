from django.contrib import admin
from.models import Post, Status

class PostAdmin(admin.ModelAdmin):
    list_display =[
        "title", "subtitle", "author", "created_on"
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Status)