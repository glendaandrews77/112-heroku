from django.db import models

class YourModelName(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Add more fields as needed

    def __str__(self):
        return self.field1  
