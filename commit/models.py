from django.db import models
from cloudinary.models import CloudinaryField

# Create models he
class Display(models.Model):
      class Meta(object):
        db_table = 'commit'                  
      name = models.CharField("name", max_length=14, blank= False, null=False, db_index=True, default="anonymous")
      body= models.CharField("update", blank=True, null=True, db_index=True, max_length=140, )
      created_at= models.DateTimeField("date", blank=True, auto_now_add=True)
      image= CloudinaryField("pic", blank=True)
      likes= models.PositiveIntegerField('likes', blank=True, default=0)
#filds & component 