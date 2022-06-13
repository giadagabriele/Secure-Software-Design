from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class ObjectOnDB(models.Model):
    variable_1 = models.CharField(max_length=50)    #small strings
    variable_2 = models.TextField()     #larger strings
    variable_3 = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    variable_4 = models.DateTimeField()
    variable_5 = models.DateTimeField()

    def __str__(self):
        return self.variable_1
