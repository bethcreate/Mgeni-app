# Generated by Django 4.1.7 on 2023-03-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0016_alter_invitation_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localadmin',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='securityregistration',
            old_name='gender',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='securityregistration',
            old_name='register_id',
            new_name='purpose',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='address',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='city',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='country',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='description',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='host',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='id_proof_image',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='id_proof_type',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='image',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='register_user_id',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='role',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='status',
        ),
        migrations.RemoveField(
            model_name='securityregistration',
            name='user_id',
        ),
        migrations.AddField(
            model_name='securityregistration',
            name='invite_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='securityregistration',
            name='invite_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='securityregistration',
            name='vehicle_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
