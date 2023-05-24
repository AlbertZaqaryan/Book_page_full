from django.contrib import admin
from .models import Category, Author, Book, Contact, Cart
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'author']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price', 'author']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_email']
    list_display_links = ['id', 'contact_email']
    search_fields = ['name', 'contact_email']

admin.site.register(Cart)