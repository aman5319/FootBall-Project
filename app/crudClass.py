from pymongo import MongoClient
import datetime

client = MongoClient(
    "mongodb://uoixnano1h7qpi5:gISr9fKfV19n4KePWd2U@bcro8hmrdqj6mso-mongodb.services.clever-cloud.com:27017/bcro8hmrdqj6mso")
db = client["bcro8hmrdqj6mso"]


class Team:
    def __init__(self, teamName1):
        self.teamName = teamName1

    def insert_team(self, teamLogo, country, squadpic, founded, homeground, teamcost, teamowner, sponser, teamcoach,
                    teamWebsite, about, operation):
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
        self.teamAbout = about

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
                teamWebsite=self.teamWebsite,
                about=self.teamAbout
            ))
        elif operation == "update":
            db.info.update_one({"teamName": {"$eq": self.teamName}},
                               {"$set": dict(
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
                                   teamWebsite=self.teamWebsite,
                                   about=self.teamAbout)
                               })

    def insertPlayer(self, playername, country, age, photo, dateofbirth, numberofgoals, playerposition, playercost,
                     jerseynum, about, operation, oldPlayerName):
        self.playerName = playername
        self.country = country
        self.age = eval(age)
        self.jersyNum = eval(jerseynum)
        self.photograph = photo
        self.cost = eval(playercost)
        self.playingPosition = playerposition
        self.dateOfBirth = dateofbirth
        self.numberofgoals = eval(numberofgoals)
        self.about = about

        if operation == "insert":
            d = dict(playerName=self.playerName,
                     country=self.country,
                     playerAge=self.age,
                     jersyNum=self.jersyNum,
                     playerPhoto=self.photograph,
                     playerCost=self.cost,
                     playerPosition=self.playingPosition,
                     playerDateOfBirth=self.dateOfBirth,
                     numberOfGoals=self.numberofgoals,
                     about=self.about
                     )
            db.info.update_one({"teamName": self.teamName}, {"$push": {"players": d}})
        elif operation == "update":
            db.info.update_one({"teamName": self.teamName, "players.playerName": oldPlayerName},
                               {"$set": {
                                   "players.$.playerName": self.playerName,
                                   "players.$.country": self.country,
                                   "players.$.playerAge": self.age,
                                   "players.$.jersyNum": self.jersyNum,
                                   "players.$.playerPhoto": self.photograph,
                                   "players.$.playerCost": self.cost,
                                   "players.$.playerPosition": self.playingPosition,
                                   "players.$.playerDateOfBirth": self.dateOfBirth,
                                   "players.$.numberOfGoals": self.numberofgoals,
                                   "players.$.about": self.about
                               }})
