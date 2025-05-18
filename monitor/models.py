from django.db import models

class BlockedIP(models.Model):
    ip_address   = models.GenericIPAddressField(unique=True)
    detected_at  = models.DateTimeField(auto_now_add=True)
    reason       = models.CharField(max_length=120)

    def __str__(self):
        return self.ip_address
