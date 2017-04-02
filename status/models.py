from django.db import models
from django.conf import settings

class LikeListField(models.IntegerField):
    #__metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(LikeListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    
class status(models.Model):
    class Meta:
        db_table = 'CMTwitter_status'

    post_id = models.IntegerField(default=0)
    author_id = models.IntegerField(default=0)
    text = models.CharField(max_length=150)
    likes = LikeListField()
    time = models.CharField(max_length=30)

    def __unicode__(self):
        return self.post_id