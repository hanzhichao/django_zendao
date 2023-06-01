# Generated by Django 4.0.5 on 2023-06-01 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mdoc', '0001_initial'),
        ('mproduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
    ]