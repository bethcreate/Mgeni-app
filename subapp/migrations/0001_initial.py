# Generated by Django 4.1.7 on 2023-03-28 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('type', models.CharField(choices=[('ORGANISATION_ADMIN', 'ORGANISATION_ADMIN'), ('LOCAL_ADMIN', 'LOCAL_ADMIN'), ('PORTAL_USER ', 'PORTAL_USER'), ('  STAFF_RESIDENT', 'STAFF_RESIDENT'), ('SECURITY_PERSONEL', 'SECURITY_PERSONEL')], default='  STAFF_RESIDENT', max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('is_organisationadmin', models.BooleanField(default=False)),
                ('is_localadmin', models.BooleanField(default=False)),
                ('is_portaluser', models.BooleanField(default=False)),
                ('is_staffresident', models.BooleanField(default=False)),
                ('is_securitypersonel', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_id', models.CharField(max_length=100)),
                ('visitor_id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('meeting_time', models.TimeField()),
                ('meeting_date', models.DateField()),
                ('meeting_duration_time', models.IntegerField()),
                ('purpose_of_meeting', models.TextField()),
                ('invite_code', models.CharField(max_length=5, null=True)),
                ('status', models.CharField(choices=[('Waiting', 'Waiting'), ('Accepted', 'Accepted')], default='Waiting', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('invite_time', models.TimeField(null=True)),
                ('invite_date', models.DateField(null=True)),
                ('id_number', models.CharField(max_length=100)),
                ('vehicle_number', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocalAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VisitorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('id_number', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(max_length=100)),
                ('checkin_time', models.DateField()),
                ('checkout_time', models.TimeField()),
                ('checkin_from', models.TimeField()),
                ('vehicle_number', models.CharField(max_length=100, null=True)),
                ('pax', models.CharField(max_length=100, null=True)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Unappoinment_visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('id_proof_type', models.CharField(max_length=100)),
                ('id_proof_image', models.FileField(upload_to='images/')),
                ('meeting_time', models.TimeField()),
                ('meeting_date', models.DateField()),
                ('meeting_duration_time', models.IntegerField()),
                ('purpose_of_meeting', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('security_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('starting_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('organisational_address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('postal_address', models.CharField(max_length=100)),
                ('location_address', models.CharField(max_length=100)),
                ('organisation_code', models.CharField(max_length=100)),
                ('organisation_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subapp.organisationcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('id_proof_type', models.CharField(blank=True, max_length=100, null=True)),
                ('id_proof_image', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.host')),
                ('register_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example4', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('no_of_department', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example6', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='example5', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Checker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('location_address', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('organisation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='subapp.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='StaffResident',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('staff_number', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('localAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.localadmin')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.roles')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityPersonnel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('invite_date', models.DateField()),
                ('invite_time', models.TimeField()),
                ('vehicle_number', models.CharField(max_length=100, null=True)),
                ('id_number', models.CharField(max_length=100, null=True)),
                ('localAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.localadmin')),
            ],
        ),
        migrations.CreateModel(
            name='PortalUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, unique=True)),
                ('department', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('staff_number', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('localAdmin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.localadmin')),
            ],
        ),
        migrations.CreateModel(
            name='OrganisationalAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(db_index=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('maximum_branch', models.CharField(max_length=100)),
                ('organisational_address', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('organisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.organisation')),
            ],
        ),
        migrations.AddField(
            model_name='localadmin',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.branches'),
        ),
        migrations.AddField(
            model_name='branches',
            name='organisational_admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subapp.organisationaladmin'),
        ),
    ]
