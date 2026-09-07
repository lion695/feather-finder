from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class BirdSpecies(models.Model):
    """
    Model representing a specific bird species catalog profile.
    """
    common_name = models.CharField(max_length=100, unique=True)
    scientific_name = models.CharField(max_length=150, blank=True)
    ai_habitat_guide = models.TextField(blank=True, help_text="AI-Generated habitat insights.")

    class Meta:
        verbose_name_plural = "Bird Species"

    def __str__(self):
        return self.common_name


class Sighting(models.Model):
    """
    Model representing a specific birdencounter logged by a Twitcher.
    Fulfills custom relational schema architecture requirements.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="twitcher_sightings")
    species = models.ForeignKey(BirdSpecies, on_delete=models.CASCADE, related_name="logged_sightings")
    date_spotted = models.DateField()
    location_name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_spotted']

    def __str__(self):
        return f"{self.species.common_name} spotted by {self.user.username} on {self.date_spotted}"