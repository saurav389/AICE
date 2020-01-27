from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile_view(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name ='profile_view')
    image = models.ImageField(default='default.jpg',upload_to='profile_pic')

    def __str__(self):
        return '{username} Profile'.format(username=self.user.username)
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)