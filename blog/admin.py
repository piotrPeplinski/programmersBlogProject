from django.contrib import admin
from .models import Post

class DisplayDate(admin.ModelAdmin):
    readonly_fields = ('createDate',)

admin.site.register(Post, DisplayDate)
