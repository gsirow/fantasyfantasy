import ff_football.ff_football.models as models
from ff_football.ff_football.scrape_results import pull_team_data, pull_matchup_results

def define_leagues():
    """add league data to database"""
    afc = models.League(league_name='AFC', league_id=1097273)
    afc.save()

def load_teams():
    """load basic team data"""
    league_record = models.League.objects.get(league_id=1097273)
    for team_name, owner_name in pull_team_data(1097273):
        row = models.FantasyFootballTeam(owner=owner_name,
                                         team_name=team_name,
                                         league=league_record)
        row.save()

def load_matchup_data():
    """load all matchup data from season"""
    for week_num in range(1, 13):
        for matchup_data in pull_matchup_results(week_num):
            team_record = (models.FantasyFootballTeam.objects
                           .get(owner_name=matchup_data['team_owner']))
            row = models.MatchupResult(team=team_record,
                                       week=week_num,
                                       score=matchup_data['score'],
                                       win=matchup_data['win'])
            row.save()

define_leagues()
load_teams()
load_matchup_data()