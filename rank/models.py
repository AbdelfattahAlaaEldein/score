from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class UserScore(models.Model):
    username = models.CharField(max_length=100, unique=True)
    juggling_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    speed_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    agility_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    dribbling_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    total_score = models.FloatField(editable=False, default=0)

    def save(self, *args, **kwargs):
        self.total_score = (
            self.juggling_score + self.speed_score + self.agility_score + self.dribbling_score
        ) / 4
        super(UserScore, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
