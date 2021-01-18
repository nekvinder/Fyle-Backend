from django.db import models


class banks(models.Model):
    name = models.TextField(max_length=50)

    class Meta:
        db_table = "banks"


class branches(models.Model):
    ifsc = models.TextField(max_length=11, null=False, primary_key=True)
    branch = models.TextField(max_length=74)
    address = models.TextField(max_length=195)
    city = models.TextField(max_length=50)
    district = models.TextField(max_length=50)
    state = models.TextField(max_length=26)
    bank = models.ForeignKey(banks, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "branches"
