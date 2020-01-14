from django.db import models
from django.contrib.auth.models import User

# from inventories.models import Sample
# from inventories.models import Norm
# from inventories.models import Scale

# from vkpsytest.utils import timing


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, default=None, blank=True)
    sex = models.CharField(max_length=10, null=True, default=None, blank=True)
    city = models.CharField(max_length=30, null=True, default=None, blank=True)
    country = models.CharField(max_length=30, null=True, default=None, blank=True)
    timezone = models.CharField(max_length=10, null=True, default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{} profile".format(self.user)


    @staticmethod
    def is_new_data(obj, data): # this should be actually put in separate library
        for k, v in data.items():
            if getattr(obj, k, None) != v:
                return True
        return False