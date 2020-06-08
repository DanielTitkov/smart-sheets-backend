from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


class Rubric(models.Model):
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    title = models.CharField(max_length=500)
    desc = models.TextField(blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "sheets"

    @property
    def has_children(self):
        return Rubric.objects.filter(published=True, parent=self).exists()

    def __str__(self):
        return f"<Rubric '{self.title}' id={self.id}>" 



class Sheet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    blueprint = models.ForeignKey("sheets.Blueprint", on_delete=models.CASCADE, related_name="blueprint")
    deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "sheets"
        
    def __str__(self):
        return f"<Sheet id={self.id}>"

    @property
    def title(self):
        title_element_data = self.data.filter(element_id=self.blueprint.title_element_id).first()
        return title_element_data.content if title_element_data else "<NO DATA>"

    @property
    def type(self):
        return self.blueprint.type



class Data(models.Model):
    sheet = models.ForeignKey("sheets.Sheet", on_delete=models.CASCADE, related_name="data")
    element_id = models.IntegerField()
    content = JSONField(default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = "sheets"

    def __str__(self):
        return f"<Data id={self.id}>" 



class Blueprint(models.Model):
    rubric = models.ForeignKey("sheets.Rubric", on_delete=models.PROTECT, blank=True, null=True)
    type = models.CharField(max_length=500)
    desc = models.TextField(blank=True)
    guide = models.TextField(blank=True)
    example = models.TextField(blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    title_element_id = models.IntegerField()
    published = models.BooleanField(default=False)
    structure = JSONField(default=dict)

    class Meta:
        app_label = "sheets"

    def __str__(self):
        return f"<Blueprint id={self.id}>" 
