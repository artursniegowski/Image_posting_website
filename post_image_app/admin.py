from django.contrib import admin
from post_image_app.models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post text', {'fields': ['text']}),
        ('File name', {'fields': ['image']}),
        ('Time added', {'fields': ['post_time']}),
    ]

    list_display = ('text', 'image', 'post_time')

admin.site.register(Post, PostAdmin)