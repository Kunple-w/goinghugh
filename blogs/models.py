from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)    #文章标题
    blog_digest = models.TextField(null=True,blank=True,max_length=200)      #摘要文本
    blog_content = models.TextField(null=True,blank=True)   #博客内容
    createtime = models.DateTimeField(auto_now_add=True)    #创建时间
    blog_img = models.URLField(null=True,blank=True)        #博客图片链接


    def __str__(self):
        return self.title
class Article(models.Model):
    articler = models.CharField(max_length=50)  #评论者姓名
    article_content = models.TextField(max_length=500)  #评论内容
    article_to_blog = models.ForeignKey(to=Blogs,related_name='article_to_blog',blank=True,null=True,on_delete=models.SET_NULL)    #建立评论和内容的关联关系，多对一关系
    article_createtime = models.DateTimeField(auto_now_add=True) #评论创建时间