from django.contrib import admin

from .models import MenuModel, MenuItemModel


class MenuItemInline(admin.TabularInline):
    model = MenuItemModel
    extra = 1


@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
