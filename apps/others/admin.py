from django.contrib import admin
from .models import AboutUs, MiniBlog, Support, Help, DidYouKnow, MiniBlogGallery, Rules, Contact


class ModelImageInline(admin.TabularInline):
    model = MiniBlogGallery


class ModelAdmin(admin.ModelAdmin):
    inlines = [ModelImageInline]


admin.site.register(MiniBlog, ModelAdmin)

admin.site.register(Support)
admin.site.register(AboutUs)
admin.site.register(Help)
admin.site.register(DidYouKnow)
admin.site.register(Rules)
admin.site.register(Contact)
