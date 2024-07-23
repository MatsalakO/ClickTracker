from django.db import models


class Click(models.Model):
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.browser} - {self.timestamp}"
