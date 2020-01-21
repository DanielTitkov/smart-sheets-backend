from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Sheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    blueprint = models.ForeignKey("sheets.Blueprint", on_delete=models.CASCADE, related_name="blueprint")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "sheets"
        
    def __str__(self):
        return str(self.blueprint)



class Data(models.Model):
    sheet = models.ForeignKey("sheets.Sheet", on_delete=models.CASCADE, related_name="data")
    element_id = models.IntegerField()
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "sheets"

    def __str__(self):
        return f"<Data object for {str(self.sheet)} id {self.sheet.id} field {self.element_id}>" 



class Blueprint(models.Model):
    type = models.CharField(max_length=500)
    desc = models.CharField(max_length=2000, blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    title_element_id = models.IntegerField()
    structure = JSONField(default=dict)

    class Meta:
        app_label = "sheets"

    def __str__(self):
        return self.type
