from django.contrib import admin
from .models import Model, Review


# # тут происходит магия реализации галереи
# class ModelImageInline(admin.TabularInline):
#     model = ModelsGallery
#
#
# class ModelAdmin(admin.ModelAdmin):
#     inlines = [ModelImageInline]
#
#
# admin.site.register(Model, ModelAdmin)

admin.site.register(Model)
admin.site.register(Review)
