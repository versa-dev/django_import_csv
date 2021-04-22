from django.db import models

# Create your models here.
import uuid

class Pokemon(models.Model):
    # id = models.CharField(primary_key=True, max_length=100, default=uuid.uuid4)
    name = models.TextField(max_length=50, unique=False)
    type_1 = models.TextField(max_length=50, unique=False)
    type_2 = models.TextField(max_length=50, unique=False)
    total = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    sp_atk = models.IntegerField(null=True)
    sp_def = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    generation = models.IntegerField(null=True)
    legendary = models.BooleanField(null=True)
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['type_1', 'type_2', 'legendary']

def __str__(self):
    return (self.id, self.name, self.type_1, self.type_2, self.total, self.hp, self.attack, self.defense, self.sp_atk, self.sp_def, self.speed, self.generation, self.legendary)