# Generated by Django 4.2.13 on 2024-06-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_qahramonmodel_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=80)),
                ('price', models.FloatField()),
                ('count', models.IntegerField(default=0)),
                ('descriptions', models.TextField()),
                ('image', models.FileField(upload_to='product_image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.DeleteModel(
            name='QahramonModel',
        ),
    ]
