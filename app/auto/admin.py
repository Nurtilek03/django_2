from django.contrib import admin
from .models import Car, CarImage

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]

admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
