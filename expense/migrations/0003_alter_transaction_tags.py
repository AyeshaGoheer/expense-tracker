# Generated by Django 5.0.2 on 2024-03-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_tag_transaction_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='transactions', to='expense.tag'),
        ),
    ]
