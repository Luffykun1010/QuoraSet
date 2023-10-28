from django.db import models
from django.contrib.auth.models import User
class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.post
    class Meta:
        ordering = ['-created_at',]

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comments=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created_at',]
