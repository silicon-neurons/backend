from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post, Lens, Correction, Tag

admin.site.register(CustomUser, UserAdmin)

admin.site.register(Post)
admin.site.register(Lens)
admin.site.register(Correction)
admin.site.register(Tag)
