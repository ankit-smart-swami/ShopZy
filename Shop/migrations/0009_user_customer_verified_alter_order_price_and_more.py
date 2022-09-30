# Generated by Django 4.0.3 on 2022-06-30 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('key', models.CharField(max_length=15)),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.status'),
        ),
    ]
