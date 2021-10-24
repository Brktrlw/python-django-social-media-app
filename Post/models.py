from django.db import models

class Post(models.Model):
    postAuthor  =models.ForeignKey("auth.user",on_delete=models.CASCADE)
    postTitle   =models.CharField(max_length=100,verbose_name="Post Başlığı",help_text="Post başlığı bilgisi.",blank=False)
    postContent =models.TextField(max_length=500,verbose_name="Post İçeriği",blank=False)
    postDate    =models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",auto_now=False)
    articleImage=models.FileField(blank=True,null=True)







