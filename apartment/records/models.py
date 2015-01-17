from django.db import models


# Create your models here.
class Renter(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    nick_name = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    personal_id = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    address = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    telephon_number = models.CharField(
        null=False,
        blank=False,
        max_length=100
    )

    email = models.EmailField(
        null=True,
        blank=True,
        max_length=100
    )

    work_place = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )

    move_in_date = models.DateField(
        null=False,
        blank=False,
    )

    move_out_date = models.DateField(
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
