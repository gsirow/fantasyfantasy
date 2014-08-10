from django.db import models

class League(models.Model):
    league_name = models.CharField(max_length=50)
    league_id = models.IntegerField()

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

class FantasyFantasyParticipant(models.Model):
    name = models.CharField(max_length=30)


class FantasyFantasyRoster(models.Model):
    participant = models.ForeignKey(FantasyFantasyParticipant)
    week = models.IntegerField()
    team = models.ForeignKey(FantasyFootballTeam)
    roster_spot = models.CharField(max_length=2,
                                   choices = [('B', 'Bench'),
                                              ('S1', 'Starter 1'),
                                              ('S2', 'Starter 2'),
                                              ('S3', 'Starter 3')])
    
    

