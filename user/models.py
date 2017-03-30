from django.db import models
from django.conf import settings

class FollowListField(models.IntegerField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(FollowListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    
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
    
class follow(models.Model):
    class Meta:
        db_table = 'CMTwitter_follow'
        
    u_id = models.IntegerField(default=0)
    follow = FollowListField()
