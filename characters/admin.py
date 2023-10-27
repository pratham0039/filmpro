# characters/admin.py

from django.contrib import admin
from .models import Character, Scene,SceneDurationRemark

admin.site.register(Character)
admin.site.register(Scene)

admin.site.register(SceneDurationRemark)