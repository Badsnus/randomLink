from django.db import models


class Links(models.Model):
    link_name = models.CharField(max_length=20, primary_key=True)
    user_id = models.IntegerField()
    links = models.TextField()
    count_visits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Links'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Users'
