from django.db import models

class League(models.Model):
    league_name = models.CharField(max_length=50)
    url = models.URLField()

class FantasyFootballTeam(models.Model):
    owner = models.CharField(max_length=30)
    league = models.ForeignKey(League)
    team_name = models.CharField(max_length=50)
    team_abbrev = models.CharField(max_length=4)

class MatchupResult(models.Model):
    team = models.ForeignKey(FantasyFootballTeam)
    week = models.IntegerField()
    score = models.FloatField()
    win = models.BooleanField()
    
    

