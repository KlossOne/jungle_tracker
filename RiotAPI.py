# -*- coding: utf-8 -*-
import time
import requests
import Const


class RiotAPI(object):
    def __init__(self, name, api_key, region=Const.REGIONS['europe_west']):
        self.name = name
        self.api_key = api_key
        self.region = region

    #   La methode request ne fait que request n'a donc aucune gestion d'erreur ou de controle de retour
    def _request(self, api_url, params={}):
        time.sleep(.05)
        args = {'api_key': self.api_key}
        #       Fait le tour de tout les parametres donne
        print params
        for key in params:
            #           Si une clef existe deja ( par erreur pourr exemple )  on ne l'ajoute pas sinon probleme
            #           Faire une trace ???
            if key not in args:
                args[key] = params[key]
        response = requests.get(
            #               Le format permet d'ajouter les 'variables' dans le string
            Const.URL['base'].format(
                region=self.region,
                url=api_url
            ),
            #               Ici le params n'est pas le'meme' que en haut
            params=args
        )
        print response.url
        #print response.headers
        if self.is_error(response.json()):
            raise Exception("Faire reference a l'url et le code")
        return response.json()

#######################################################################################################################
# Pour faciliter le debugage de la collecte de donnees
#######################################################################################################################

    def get_featured_games(self):
        api_url = Const.URL['getFeaturedGames']
        return self._request(api_url)

    def get_jungler_featured_game(self):
        matchs = self.get_featured_games()
        # Faire un rand pour choisir la game ?
        #matchs['gameList']
        for match in matchs['gameList']:
            if match['mapId'] == Const.MAP["Summoner's Rift"]:
                return self.get_jungler_by_match(match)
        print "Pas de match en sur la Summoner's Rift"
        return 0


#######################################################################################################################
    def get_summoner_by_name(self, name):
        api_url = Const.URL['getSummonerByNameV3'].format(
            name=name
        )
        return self._request(api_url)

    def get_current_game(self, summoner):
        api_url = Const.URL['getCurrentGame'].format(
            summonerId=summoner['id']
        )
        return self._request(api_url)

    def get_current_game_by_name(self, name):
        summoner = self.get_summoner_by_name(name)
        return self.get_current_game(summoner)

    def get_my_current_game(self):
        summoner = self.get_summoner_by_name(self.name)
        result = self.get_current_game(summoner)
        return result

    def get_jungler_by_match(self, match, team_id=100):
        jungler_ennemi = {}
        for summoner_in_game in match['participants']:
            #print str(summoner_in_game['teamId'])+"<- team ID "+ " spell 2->" +str(summoner_in_game['spell2Id'])+ " spell 1->"+str(summoner_in_game['spell1Id'])
            if summoner_in_game['teamId'] == team_id and (summoner_in_game['spell2Id'] == Const.SUMMONER_SPELL['Smite'] or summoner_in_game['spell1Id'] == Const.SUMMONER_SPELL['Smite']):
                jungler_ennemi = summoner_in_game
        return jungler_ennemi

    def get_my_jungle_ennemi(self):
        result = self.get_my_current_game()
        for summoner_in_game in result['participants']:
            if summoner_in_game['summonerName'] != self.name:
                return self.get_jungler_by_match(result, summoner_in_game['teamId'])

    def is_error(self, result):
        if 'status' in result:
            print "status_code : "+str(result['status']['status_code'])
            print "message : "+str(result['status']['message'])
            return 1
        else:
            return 0
    def get_matchlist_by_account(self, account_id, champion_id=-1, begin_index=-1, end_index=-1):
        params = {}
        if(champion_id > -1):
            params.update({'champion' : champion_id})
        #if(begin_index > -1 and end_index > -1):
        #    params.update({'beginIndex' : begin_index,'endIndex' : end_index})
            params.update({'beginIndex' : 0, 'endIndex' : 20})
            api_url = Const.URL['getMatchList'].format(
                accountId=account_id
            )
            return self._request(api_url, params)
        else:
            print "Aucun champion donner"
            return 0
