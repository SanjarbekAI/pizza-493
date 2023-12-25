from django.contrib import admin
from pages.models import ScrollModel, GalleryModel, MenuModel, CategoryModel, ReservationModel


@admin.register(ScrollModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(GalleryModel)
class ScrollModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'description']
    ordering = ['-created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title']
    ordering = ['-created_at']


@admin.register(ReservationModel)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['-created_at']