# Generated by Django 4.1 on 2023-05-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_img/', verbose_name='商品画像'),
        ),
    ]