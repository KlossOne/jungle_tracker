from RiotAPI import RiotAPI
import sys

def main():
    summoner_name="Snow Eater"
    api = RiotAPI(summoner_name,'RGAPI-615a24fa-0f21-4421-9d47-d0a9b1af9e05')
    #result = api.get_summoner_by_name('Pedobabar')
    #result = api.get_my_jungle_ennemi()

    #get_jungler_featured_game()
        #Permet presque a coup sur de trouver une game en normal
    result = api.get_jungler_featured_game()
    print result



if  __name__ == "__main__":
    req_version = (2, 7)
    cur_version = sys.version_info

    if cur_version >= req_version :
        main()
    else:
       print "Your Python interpreter is min 2,7. Please consider upgrading."