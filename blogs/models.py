from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    blog_content = models.TextField(null=True,blank=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title