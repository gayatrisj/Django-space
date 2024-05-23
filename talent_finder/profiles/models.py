from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    linkedin = models.JSONField(null=True, blank=True)
    leetcode = models.JSONField(null=True, blank=True)
    hackerrank = models.JSONField(null=True, blank=True)
    gfg = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
