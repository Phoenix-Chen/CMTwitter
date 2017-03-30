from django.db import models
from django.conf import settings

class user(models.Model):
    class Meta:
        db_table = 'CMTwitter_user'

    u_id = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    #email = models.TextField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.email
    
