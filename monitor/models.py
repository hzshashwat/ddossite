from django.db import models

class BlockedIP(models.Model):
    ip          = models.GenericIPAddressField(unique=True)
    reason      = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.ip
    class Meta:
        verbose_name = "Blocked IP"
        verbose_name_plural = "Blocked IPs"
        ordering = ["-created_at"]