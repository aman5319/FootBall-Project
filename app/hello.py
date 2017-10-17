from flask import Flask

from pymongo import MongoClient


client = MongoClient("mongodb://uoixnano1h7qpi5:gISr9fKfV19n4KePWd2U@bcro8hmrdqj6mso-mongodb.services.clever-cloud.com:27017/bcro8hmrdqj6mso")

app = Flask(__name__)

db = client["bcro8hmrdqj6mso"]


def insertTeam():
    db.info.insert_one(
        {
            "teamName": "Real Madrid",
            "teamLogo": "https://imagelogo.jpg",
            "squadpic": "https://sqaud.jpg",
            "founded": "6 march 1902",
            "homeground": "london",
            "teamcost": 432454363,
            "league": "la liga",
            "club_website": "https://amc.com",
            "teamowner": "Kali",
            "sponser": "Adidas",
            "teamcoach": "Aniket",
            "wikipediaLink": "https://teamLink",
        }
    )


@app.route("/")
def hello():
    return "Deployer"

@app.route("/f")
def xyz():
	return db.info.find({}).pretty()

@app.route("/in")
def insert():
	insertTeam()
	return "insert"
if __name__ == "__main__":
    app.run()
