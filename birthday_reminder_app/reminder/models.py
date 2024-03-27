from django.db import models


#class User(models.Model):
#    first_name = models.CharField(max_length=20)
#    last_name = models.CharField(max_length=20)
#    email = models.CharField(max_length=30)


class Birthday(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=20)
    month = models.IntegerField()
    day = models.IntegerField()

    def __str__(self):
        return f"Birthday of {self.person_name}: {self.day}/{self.month}"
