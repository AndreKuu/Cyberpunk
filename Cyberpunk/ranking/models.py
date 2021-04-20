from django.db import models

# Create your models here.
class PicTest(models.Model):
    """上传图片"""
    # 注意upload_to对应的是相对于static/media目录
    # upload_to对应的booktest是在media目录下新建的目录，名称和应用名一致
    goods_pic = models.ImageField(upload_to="ranking")