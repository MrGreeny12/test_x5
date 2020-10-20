from django.db import models


class Club(models.Model):
    '''
    Информация о клубе
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Player(models.Model):
    '''
    информация об игроке
    '''
    name = models.CharField(max_length=255)
    club = models.ForeignKey(
        'Club',
        related_name='players',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name