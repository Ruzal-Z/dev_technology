from django.contrib import admin

from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)               #для редактирвоания поля публикация из списка статей в панеле django
    list_filter = ('is_published', 'time_create')              # поля по которым можно фильтровать список в панеле django
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)