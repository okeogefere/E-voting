from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Candidates(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to='images/')
    manifesto = models.TextField()

    def __str__(self):
        return self.name 
    

class Voters(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Vote(models.Model):
    voters = models.ForeignKey(Voters, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voters.user.username} voted for {self.candidate.name}"
