from django.db import models

# Create your models here.
from django.db import models

class PhoneRange(models.Model):
    def_code = models.CharField(max_length=3, db_index=True)
    start_range = models.BigIntegerField(db_index=True)
    end_range = models.BigIntegerField()
    capacity = models.IntegerField()
    operator = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    territory = models.CharField(max_length=255)
    inn = models.CharField(max_length=20)

    class Meta:
        indexes = [
            models.Index(fields=['def_code', 'start_range', 'end_range']),
        ]