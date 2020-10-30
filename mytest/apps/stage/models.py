from django.db import models

class Stage(models.Model):
    stage_opponent = models.CharField('Номер мошенника', max_length=11)
    stage_time = models.CharField('Время инцидента', max_length=5)

class Dialogue(models.Model):
    dialogue_accept_reaction = models.CharField('Реакция на да', max_length=100)
    dialogue_accept_score = models.IntegerField('Баллы за да')

    dialogue_reaction = models.BooleanField('Реакция игрока')

    dialogue_deny_reaction = models.CharField('Реакция побега', max_length=100)
    dialogue_deny_score = models.IntegerField('Баллы за побег')

class User(models.Model):
    pass

