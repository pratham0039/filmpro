# models.py
from django.db import models


class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')


class Scene(models.Model):
    scene_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cn = models.TextField(null=True, blank=True)
    hair_makeup = models.TextField(null=True, blank=True)
    prosthetics = models.TextField(null=True, blank=True)
    key_props = models.TextField(null=True, blank=True)
    props = models.TextField(null=True, blank=True)
    set_dressing = models.TextField(null=True, blank=True)
    extras = models.TextField(null=True, blank=True)
    picture_vechiles = models.TextField(null=True, blank=True)
    production = models.TextField(null=True, blank=True)
    special_professionals= models.TextField(null=True, blank=True)
    sfx = models.TextField(null=True, blank=True)
    vfx = models.TextField(null=True, blank=True)
    special_equipments = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    int_ext = models.TextField(null=True, blank=True)
    timeofday = models.TextField(null=True, blank=True)
    story = models.ImageField(upload_to='scene_images/', default='static\img\add.png', null=True, blank=True)


    

    def __str__(self):
        return f'Scene {self.scene_number}'

class Character(models.Model):
    name = models.CharField(max_length=255)
    scenes = models.ManyToManyField(Scene, related_name='characters')
    avatar = models.ImageField(upload_to='char_images/', default='static\img\add.png', null=True, blank=True)

    def __str__(self):
        return self.name



class SceneDurationRemark(models.Model):
    scene_number = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    remark = models.TextField(null=True, blank=True)
    notescs = models.TextField(null=True, blank=True)
    lenscs = models.TextField(null=True, blank=True)
    shotno = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Scene {self.scene_number} Duration and Remark'
