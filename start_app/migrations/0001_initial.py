# Generated by Django 3.0.3 on 2020-10-31 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_filtered_Company_Funder_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_emailAddress', models.EmailField(max_length=254)),
                ('funder_emailAddress', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Company_CEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=100)),
                ('productType', models.CharField(max_length=100)),
                ('budgetRange', models.IntegerField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('isConfirmed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_Funder_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_emailAddress', models.EmailField(max_length=254)),
                ('funder_emailAddress', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Funder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventureName', models.CharField(max_length=100)),
                ('maximum_funding_capacity', models.CharField(max_length=100)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('productType', models.CharField(max_length=300)),
                ('state_list', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=300)),
                ('isConfirmed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='usrOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailAddress', models.EmailField(max_length=254)),
                ('otp', models.IntegerField()),
                ('generated_time_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('productType', models.CharField(max_length=100)),
                ('shortDescription', models.TextField()),
                ('patent', models.BooleanField(default=False)),
                ('company_ceo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_company', to='start_app.Company_CEO')),
            ],
        ),
    ]