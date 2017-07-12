from RiotAPI import RiotAPI
import json
def main():
    summoner_name="elo eraser"
    api = RiotAPI(summoner_name,'RGAPI-615a24fa-0f21-4421-9d47-d0a9b1af9e05')
    #result = api.get_summoner_by_name('Pedobabar')
    result = api.get_my_jungle_ennemi()
    print result



if  __name__ == "__main__":
    main()