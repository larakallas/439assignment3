from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    profession = models.CharField(max_length=100)
    tel_number = models.CharField(max_length=15)
    email_address = models.EmailField()

    def __str__(self):
        return self.name
