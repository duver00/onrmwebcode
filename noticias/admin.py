from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ("titulo", "imagen","slug","author", "created", "updated")
    prepopulated_fields ={"slug":('titulo',)}


admin.site.register(Post, PostAdmin)