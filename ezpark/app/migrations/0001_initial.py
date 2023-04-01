# Generated by Django 4.1.7 on 2023-03-29 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            Cname='Client',
            Cfields=[
                ('cid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                ('fullname', models.CharField(max_length=100)),
                ('email',models.CharField(max_length=100)),            
                ('phone',models.IntegerField(max_length=100)),
                ('password',models.CharField(max_length=15)),
                ('booking_status',models.CharField(max_length=100)),
                ('fine',models.IntegerField(max_length=100)),
                
            ],
            LOname='LandOwner',
            LOfields=[
                ('la_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),               
                ('fullname', models.CharField(max_length=100)),
                ('email',models.CharField(max_length=100)),            
                ('phone',models.IntegerField(max_length=100)),
                ('password',models.CharField(max_length=15)),
                ('booking_status',models.CharField(max_length=100)),
                ('pincode',models.CharField(max_length=100)),
                ('landmark',models.CharField(max_length=100))

            ],
            Lname='Land',
            Lfields=[
                ('l_id',models.AutoField(primary_key=True)),
                ('pincode',models.IntegerField(max_length=100)),
                ('sq_feet',models.FloatField(max_length=100)),
                ('booking_status',models.CharField(max_length=100)),


            ],
            Vname='Vehicle',
            Vfields=[
                ('v_id',models.AutoField(primary_key=True)),
                ('v_number',models.CharField(max_length=100)),
                ('v_type',models.CharField(max_length=100))
            
            ],
            Bname='Booking',
            Bfields=[
                ('B_id',models.AutoField(primary_key=True)),
                ('booking_status',models.CharField(max_length=100))

            ],
        ),
    ]
