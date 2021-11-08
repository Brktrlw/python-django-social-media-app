from django.db import models

class Post(models.Model):
    postAuthor  =models.ForeignKey("auth.user",on_delete=models.CASCADE)
    postTitle   =models.CharField(max_length=100,verbose_name="Post Başlığı",help_text="Post başlığı bilgisi.",blank=False)
    postContent =models.TextField(max_length=500,verbose_name="Post İçeriği",blank=False)
    postDate    =models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi",auto_now=False)
    postImage=models.FileField(blank=True,null=True)

    class Meta:
        verbose_name_plural="Gönderiler"
        ordering=["id"]

    def __str__(self):
        return self.postTitle

class Comment(models.Model):
    commentAuthor=models.ForeignKey("auth.user",on_delete=models.CASCADE)
    commentContent=models.CharField(max_length=200,verbose_name="Yorum",blank=False)
    commentDate=models.DateTimeField(auto_now_add=True,verbose_name="Tarih")





