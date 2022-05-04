from django.contrib import admin
from .models import Author, City, Country, Book, Category, CoverColor


# Register your models here.

@admin.register(Author)
class AuthorAdminModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country', 'city')

@admin.register(City)
class CityAdminModel(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    list_display = ('name', 'shortcode')

@admin.register(Book)
class BookAdminModel(admin.ModelAdmin):
    list_display = ('title', 'ISBN_CODE', 'author', 'price')

@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    list_display = ('name',)\

@admin.register(CoverColor)
class CoverColorAdminModel(admin.ModelAdmin):
    pass