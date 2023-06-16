from django.db import models

class UserDetails(models.Model):
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=250)

    class Meta:
        # app_label = 'myuser_app'
        # schema = 'myuser_schema'
        # db_table=u'"myuser_app\".\"myuser_schema"'
        db_table = 'myuser_schema"."userdetails_table'
        # db_table='UserDetails'
        # schema = 'myuser_schema'