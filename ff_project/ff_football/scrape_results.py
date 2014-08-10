from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

SCOREBOARD_URL = 'http://games.espn.go.com/ffl/scoreboard?leagueId={league_id}&scoringPeriodId={week_num}&seasonId=2013'
STANDINGS_URL = 'http://games.espn.go.com/ffl/standings?leagueId={league_id}&seasonId=2013'

def pull_matchup_results(week_num, league_id=1097273):
    """pull matchup results for league for week"""
    url = SCOREBOARD_URL.format(league_id=league_id, week_num=week_num)
    soup = BeautifulSoup(urlopen(url).read(), 'lxml')
    for matchup in soup.findAll('table', 'ptsBased matchup'):
        for team_row in matchup.findAll('tr', id=re.compile('teamscrg')):
            team = team_row.find('td', 'team')
            score = team_row.find('td', 'score')
            yield {'team_name': team.a.string,
                    'team_abbrev': team.find('span', 'abbrev').string,
                    'team_record': team.find('span', 'record').string,
                    'team_owner': team.find('span', 'owners').a.string,
                    'score': score.string,
                    'win': len(set(score['class']).intersection(['winning']))}

def pull_team_data(league_id):
    """pull team names from standings"""
    url = STANDINGS_URL.format(league_id=league_id)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    for row in soup.findAll('tr', 'tableBody'):
        team_data = row.a['title']
        pattern = re.compile('(.+)\s\((.+)\)')
        team_name, owner_name = pattern.match(team_data).groups()
        yield {'team_name': team_name, 'team_owner': owner_name}
