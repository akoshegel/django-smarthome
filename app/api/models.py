from datetime import datetime

from django.db import models


class DeviceModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(default=datetime.now())
    updated_at = models.DateField(default=datetime.now(), auto_now=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        current_time = datetime.now()
        if not self.id:
            self.created_at = current_time
            self.updated_at = current_time
            super().save(*args, **kwargs)
