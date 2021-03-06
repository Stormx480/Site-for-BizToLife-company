# Generated by Django 2.1.3 on 2018-11-11 11:15

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub']},
        ),
        migrations.AlterField(
            model_name='post',
            name='picture_preview',
            field=imagekit.models.fields.ProcessedImageField(upload_to='media'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
