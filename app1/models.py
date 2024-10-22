from django.db import models

class Prediction(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z_exp = models.FloatField(null=True, blank=True)
    z_pred = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"({self.x}, {self.y}) -> z_exp: {self.z_exp}, z_pred: {self.z_pred}"