# Generated by Django 2.1.7 on 2019-04-04 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wealthy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_type', models.CharField(choices=[('FULL', 'Full Promotion'), ('MINI', 'Mini Promotion'), ('MICRO', 'Micro Promotion')], default='FULL', max_length=25)),
                ('will_promote', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True)),
                ('wealthy_client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
            options={
                'verbose_name_plural': 'Wealthy',
            },
        ),
    ]
