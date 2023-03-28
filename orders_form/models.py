from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField
class order(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    e_mail=models.EmailField(null=True)
    phone=PhoneField()
    country=CountryField(null=True)
    city=models.CharField(max_length=20)
    description=models.TextField()

    def __str__(self):
        return f"{self.first_name} - {self.last_name[:20]} - {self.e_mail} - {self.phone} - {self.country} - {self.city} - {self.description}"




