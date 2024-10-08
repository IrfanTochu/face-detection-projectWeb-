from django.db import models

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    language = models.CharField(max_length=10)
    visit_count = models.PositiveIntegerField(default=1)
    last_visit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ip_address} - {self.language} - {self.visit_count} visits"
