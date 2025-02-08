from django import forms
from .models import Car, CarImage

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'price', 'mileage', 'description', 'main_image']

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image', 'is_main']
