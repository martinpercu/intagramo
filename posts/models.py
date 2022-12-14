"""Post models"""

#Django
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    """ Post Model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length= 250)
    photo = models.ImageField(upload_to="posts/photo")

    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username """
        return '{} by @{}'.format(self.title, self.user.username)
        

