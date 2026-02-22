from django.contrib import admin
from .models import Patient, Doctor, Mapping

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Mapping)