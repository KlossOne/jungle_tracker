import requests

import Const
import time


class RiotAPI(object):
    def __init__(self, name, api_key, region= Const.REGIONS['europe_west']):
        self.name = name
        self.api_key = api_key
        self.region  = region

#   La methode request ne fait que request n'a donc aucune gestion d'erreur ou de controle de retour
    def _request(self, api_url, params=()):
        time.sleep(.05)
        args= {'api_key' : self.api_key }
#       Fait le tour de tout les parametres donne
        for key, value in params:
#           Si une clef existe deja ( par erreur pourr exemple )  on ne l'ajoute pas sinon probleme
#           Faire une trace ???
            if key not in args:
                args[key] = value
        response = requests.get(
#               Le format permet d'ajouter les 'variables' dans le string
            Const.URL['base'].format(
                region = self.region,
                url   = api_url
            ),
#               Ici le params n'est pas le'meme' que en haut
            params = args
        )
        print response.url
        return response.json()
    def get_summoner_by_name(self, name):
        api_url = Const.URL['getSummonerByNameV3'].format(
            name=name
        )
        return self._request(api_url)
    def get_current_game(self, summoner):
        api_url= Const.URL['getCurrentGame'].format(
            summonerId=summoner['id']
        )
        return self._request(api_url)
    def get_current_game_by_name(self,name):
        summoner=self.get_summoner_by_name(name)
        return self.get_current_game(summoner)

    def get_my_current_game(self):
        summoner=self.get_summoner_by_name(self.name)
        return self.get_current_game(summoner)

    def get_my_jungle_ennemi(self):
        team_id = 0
        result=self.get_my_current_game()
        my_jungler_ennemi={}
        for summoner_in_game in result['participants']:
            if summoner_in_game['summonerName'] != self.name:
                team_id = summoner_in_game['teamId']
        for summoner_in_game in result['participants']:
            if (summoner_in_game['teamId'] == team_id and (
                    summoner_in_game['spell2Id'] == 11 or summoner_in_game['spell1Id'] == 11)):
                my_jungler_ennemi= summoner_in_game
        return my_jungler_ennemi