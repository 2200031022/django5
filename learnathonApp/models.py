from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    age=models.DateField()
    class Meta:
        db_table="Register"


class Feedback(models.Model):
    satisfaction_choices = [
        ('Very satisfied', 'Very satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Dissatisfied', 'Dissatisfied'),
        ('Very dissatisfied', 'Very dissatisfied')
    ]

    likelihood_choices = [
        ('Very likely', 'Very likely'),
        ('Likely', 'Likely'),
        ('Neutral', 'Neutral'),
        ('Unlikely', 'Unlikely'),
        ('Very unlikely', 'Very unlikely')
    ]

    quality_choices = [
        ('Excellent', 'Excellent'),
        ('Very good', 'Very good'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor')
    ]

    delivery_choices = [
        ('Very satisfied', 'Very satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Dissatisfied', 'Dissatisfied'),
        ('Very dissatisfied', 'Very dissatisfied')
    ]

    service_choices = [
        ('Very satisfied', 'Very satisfied'),
        ('Satisfied', 'Satisfied'),
        ('Neutral', 'Neutral'),
        ('Dissatisfied', 'Dissatisfied'),
        ('Very dissatisfied', 'Very dissatisfied')
    ]

    q1 = models.CharField(max_length=50, choices=satisfaction_choices)
    q2 = models.CharField(max_length=50, choices=likelihood_choices)
    q3 = models.CharField(max_length=50, choices=quality_choices)
    q4 = models.CharField(max_length=50, choices=satisfaction_choices)
    q5 = models.CharField(max_length=50, choices=satisfaction_choices)
    q6 = models.CharField(max_length=50, choices=quality_choices)
    q7 = models.CharField(max_length=50, choices=delivery_choices)
    q8 = models.CharField(max_length=50, choices=likelihood_choices)
    q9 = models.CharField(max_length=50, choices=likelihood_choices)
    q10 = models.CharField(max_length=50, choices=service_choices)
    q11 = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # For simplicity, storing passwords in plain text is not recommended in practice

    def __str__(self):
        return self.username
