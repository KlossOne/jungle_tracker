# -*- coding: utf-8 -*-

import sys
from RiotAPI import RiotAPI

def main():
    summoner_name = "Snow Eater"
    api = RiotAPI(summoner_name, 'RGAPI-d46320fe-7ca6-4d00-9976-7fc3d3cbc9b4')
    #result = api.get_summoner_by_name('Pedobabar')
    #result = api.get_my_jungle_ennemi()

    #get_jungler_featured_game()
        #Permet presque a coup sur de trouver une game en normal
    match_info_jungler = api.get_jungler_featured_game()
    print match_info_jungler
    jungler = api.get_summoner_by_name(match_info_jungler['summonerName'])
    print jungler
    result = api.get_matchlist_by_account(jungler['accountId'], match_info_jungler['championId'])
    print result

if  __name__ == "__main__":
    REQ_VERSION = (2, 7)
    CUR_VERSION = sys.version_info

    if CUR_VERSION >= REQ_VERSION:
        main()
    else:
        print "Your Python interpreter version should be min 2,7. Please consider upgrading."
