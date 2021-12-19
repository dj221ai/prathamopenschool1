from django.db import models

# Create your models here.

class ExcelUploadModel(models.Model):

    agent_name = models.CharField(max_length=255, blank=True, null=True)
    recovery_file = models.FileField(upload_to='recovery_files')

    def __str__(self):
        return self.agent_name

    def delete(self, *args, **kwargs):
        self.recovery_file.delete()
        return super().delete(*args, **kwargs)


