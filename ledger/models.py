from django.db import models


def get_filename():
    return models.CharField(max_length=255, blank=True)


class Person(models.Model):
    consumer_id = models.IntegerField(default=0)
    preferred_name = models.CharField(max_length=255, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(
        # upload_to=get_filename
    )

    def __str__(self):
        return self.preferred_name or self.full_name


class Contact(models.Model):
    person = models.ForeignKey(
        to=Person,
        related_name='contacts',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, blank=True)
    number = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.person) + self.number

class Month(models.Model):
    identifier = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True)
    
    def __str__(self):
        return self.identifier

class AbstractSavings(models.Model):
    person = models.ForeignKey(
        to=Person,
        related_name='+',
        on_delete=models.CASCADE
    )
    amount = models.FloatField(default=0)
    month = models.ForeignKey(
        to=Month,
        related_name='+',
        on_delete=models.CASCADE
    )
    remark = models.CharField(max_length=600)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.month) + " " + str(self.person) + " " + str(self.amount)

class Savings(AbstractSavings):
    pass


class Credit(AbstractSavings):
    pass


class RePayment(AbstractSavings):
    pass

