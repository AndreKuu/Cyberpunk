from django.db import models

# 书籍分类表label
class Label(models.Model):
    label_id = models.AutoField('序号', primary_key=True)
    label_name = models.CharField('分类标签', max_length=10)
    def __str__(self):
        return self.label_name
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '书籍分类'
        verbose_name_plural = '书籍分类'

# 书籍信息表song
class Song(models.Model):
    song_id = models.AutoField('序号', primary_key=True)
    song_name = models.CharField('书名', max_length=50)
    song_singer = models.CharField('作者', max_length=50)
    song_time = models.CharField('页数', max_length=10)
    song_album = models.CharField('发行方', max_length=50)
    song_languages = models.CharField('语种', max_length=20)
    song_type = models.CharField('类型', max_length=20)
    song_release = models.CharField('发行时间', max_length=20)
    song_img = models.CharField('书籍图片', max_length=20)
    song_lyrics = models.CharField('内容', max_length=50, default='暂无内容')
    song_file = models.CharField('内容文件', max_length=50)
    label = models.ForeignKey(Label, on_delete=models.CASCADE,verbose_name='书名分类')
    def __str__(self):
        return self.song_name
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '书籍信息'
        verbose_name_plural = '书籍信息'

# 书籍动态表dynamic
class Dynamic(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='书籍')
    dynamic_plays = models.IntegerField('阅读次数')
    dynamic_search = models.IntegerField('搜索次数')
    dynamic_down = models.IntegerField('点赞次数')
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '书籍动态'
        verbose_name_plural = '书籍动态'

# 书籍点评表comment
class Comment(models.Model):
    comment_id = models.AutoField('序号', primary_key=True)
    comment_text = models.CharField('内容', max_length=500)
    comment_user = models.CharField('用户', max_length=20)
    song = models.ForeignKey(Song, on_delete=models.CASCADE,verbose_name='书名')
    comment_date = models.CharField('日期', max_length=50)
    class Meta:
        # 设置Admin界面的显示内容
        verbose_name = '书籍评论'
        verbose_name_plural = '书籍评论'
# Create your models here.

class PicTest(models.Model):
    """上传图片"""
    # 注意upload_to对应的是相对于static/media目录
    # upload_to对应的booktest是在media目录下新建的目录，名称和应用名一致
    goods_pic = models.ImageField(upload_to="index")
