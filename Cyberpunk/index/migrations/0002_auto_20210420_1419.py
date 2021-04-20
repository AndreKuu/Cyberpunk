# Generated by Django 3.1.7 on 2021-04-20 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_pic', models.ImageField(upload_to='index')),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '书籍评论', 'verbose_name_plural': '书籍评论'},
        ),
        migrations.AlterModelOptions(
            name='dynamic',
            options={'verbose_name': '书籍动态', 'verbose_name_plural': '书籍动态'},
        ),
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': '书籍分类', 'verbose_name_plural': '书籍分类'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': '书籍信息', 'verbose_name_plural': '书籍信息'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.song', verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='dynamic_down',
            field=models.IntegerField(verbose_name='点赞次数'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='dynamic_plays',
            field=models.IntegerField(verbose_name='阅读次数'),
        ),
        migrations.AlterField(
            model_name='dynamic',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.song', verbose_name='书籍'),
        ),
        migrations.AlterField(
            model_name='song',
            name='label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.label', verbose_name='书名分类'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_album',
            field=models.CharField(max_length=50, verbose_name='发行方'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.CharField(max_length=50, verbose_name='内容文件'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_img',
            field=models.CharField(max_length=20, verbose_name='书籍图片'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_lyrics',
            field=models.CharField(default='暂无内容', max_length=50, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_name',
            field=models.CharField(max_length=50, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_singer',
            field=models.CharField(max_length=50, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_time',
            field=models.CharField(max_length=10, verbose_name='页数'),
        ),
    ]
