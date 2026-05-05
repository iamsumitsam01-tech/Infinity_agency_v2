from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    price = models.CharField(max_length=100)   # ✅ ADD THIS

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()

    phone = models.CharField(max_length=15, blank=True, null=True)  # ✅ correct place

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    