from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='cars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/images/')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'Image of {self.car.brand} {self.car.model}'

