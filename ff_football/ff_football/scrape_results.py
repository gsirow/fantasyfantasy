from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def pull_matchup_results(week_num, league_id=1097273):
    """pull matchup results for leagure for week"""
    url = ('http://games.espn.go.com/ffl/scoreboard?leagueId={league_id}&scoringPeriodId={week_num}'
           .format(league_id=league_id, week_num=week_num))
    soup = BeautifulSoup(urlopen(url).read(), 'lxml')
    for matchup in soup.findAll('table', 'ptsBased matchup'):
        for team_row in matchup.findAll('tr', id=re.compile('teamscrg')):
            team = team_row.find('td', 'team')
            score = team_row.find('td', 'score')
            return {'team_name': team.a.string,
                    'team_abbrev': team.find('span', 'abbrev').string,
                    'team_record': team.find('span', 'record').string,
                    'team_owner': team.find('span', 'owners').a.string,
                    'score': score.string,
                    'win': len(set(score['class']).intersection(['winning']))}