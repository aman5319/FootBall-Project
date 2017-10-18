from pymongo import MongoClient
import datetime

client = MongoClient(
    "mongodb://uoixnano1h7qpi5:gISr9fKfV19n4KePWd2U@bcro8hmrdqj6mso-mongodb.services.clever-cloud.com:27017/bcro8hmrdqj6mso")
db = client["bcro8hmrdqj6mso"]


class Team:
    def __init__(self, teamName1):
        self.teamName = teamName1

    def insert_team(self, teamLogo, country, squadpic, founded, homeground, teamcost, teamowner, sponser, teamcoach,
                    teamWebsite, operation):
        self.teamLogo = teamLogo
        self.country = country
        self.squadpic = squadpic
        self.founded = founded
        self.homeground = homeground
        self.teamcost = teamcost
        self.teamowner = teamowner
        self.sponser = sponser
        self.teamcoach = teamcoach
        self.teamWebsite = teamWebsite

        if operation == "insert":
            db.info.insert_one(dict(
                teamName=self.teamName,
                teamLogo=self.teamLogo,
                country=self.country,
                squadPic=self.squadpic,
                founded=founded,
                homeGround=self.homeground,
                teamCost=self.teamcost,
                teamOwner=self.teamowner,
                teamSponsor=self.sponser,
                teamCoach=self.teamcoach,
                teamWebsite=self.teamWebsite
            ))
        elif operation == "update":
            db.info.update_one({"teamName": {"$eq": self.teamName}},
                               {"$set":dict(
                                     teamName=self.teamName,
                                     teamLogo=self.teamLogo,
                                     country=self.country,
                                     squadPic=self.squadpic,
                                     founded=founded,
                                     homeGround=self.homeground,
                                     teamCost=self.teamcost,
                                     teamOwner=self.teamowner,
                                     teamSponsor=self.sponser,
                                     teamCoach=self.teamcoach,
                                     teamWebsite=self.teamWebsite)
                               })



def wantToinsertPlayers(self):
    yes_no = input("want to insert players now press y for yes ,n for no")
    if yes_no.lower() != "y":
        print("you can insert later")
    else:
        while yes_no.lower() == "y":
            self.insertPlayer()
            yes_no = input("want to insert more players press y for yes ,n for no")


def insertPlayer(self):
    self.playerName = input("enter the player name")
    self.country = input("enter the country for which he plays")
    self.club = input("enter the club for which he plays ")
    self.jersyNum = eval(input("enter the jersy number"))
    self.photograph = input("enter his photograph")
    self.cost = eval(input("enter the cost of player in $"))
    self.playingPosition = input("enter the player position")
    self.dateOfBirth = input("enter his date of birth in format yyyy/mm/dd").split("/")
    birth = datetime.datetime(year=int(self.dateOfBirth[0]), month=int(self.dateOfBirth[1]),
                              day=int(self.dateOfBirth[2]))
    self.brandAmbassdor = input("enter if he is brand ambassdor of any product")
    self.contract = input("enter his contract until information date in format yyyy/mm/dd)").split("/")
    cont = datetime.datetime(year=int(self.contract[0]), month=int(self.contract[1]), day=int(self.contract[2]))
    self.playertype = input("enter  player type")
    self.records = input("enter records made by him if any")
    d = dict(playerName=self.playerName,
             country=self.country,
             club=self.club,
             jersyNum=self.jersyNum,
             photograph=self.photograph,
             cost=self.cost,
             playingPosition=self.playingPosition,
             dateOfBirth=birth,
             brandAmb=self.brandAmbassdor,
             contract=cont,
             records=self.records
             )
    db.info.update_one({"teamName": self.teamName}, {"$push": {"players": d}})
