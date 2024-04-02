from django.db import models

# Create your models here.
class RefuelSession(models.Model):
    date = models.DateField()
    fuel_type = models.CharField(max_length=20)
    pence_per_litre = models.DecimalField(max_digits=4, decimal_places=1)
    litres_filled = models.DecimalField(max_digits=5, decimal_places=2)
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_cost = round((self.pence_per_litre * self.litres_filled)/100, 2)
        super().save(*args, **kwargs)