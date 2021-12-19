from django import forms
from django.db import models
from django.db.models import fields
from .models import ExcelUploadModel


class ExcelUploadModelForm(forms.ModelForm):

    class Meta:
        model = ExcelUploadModel
        fields = ('agent_name', 'recovery_file')
