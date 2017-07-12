from RiotAPI import RiotAPI
import sys

def main():
    summoner_name="Snow Eater"
    api = RiotAPI(summoner_name,'RGAPI-615a24fa-0f21-4421-9d47-d0a9b1af9e05')
    #result = api.get_summoner_by_name('Pedobabar')
    #result = api.get_my_jungle_ennemi()

    #get_jungler_featured_game()
        #Permet presque a coup sur de trouver une game en normal
    match_info_jungler = api.get_jungler_featured_game()
    print match_info_jungler
    jungler=api.get_summoner_by_name(match_info_jungler['summonerName'])
    print jungler
    result=api.get_matchlist_by_account(jungler['accountId'],match_info_jungler['championId'])
    print result
if  __name__ == "__main__":
    req_version = (2, 7)
    cur_version = sys.version_info

    if cur_version >= req_version :
        main()
    else:
       print "Your Python interpreter is min 2,7. Please consider upgrading."