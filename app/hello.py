from flask import Flask, render_template, request, redirect, url_for
from crudClass import Team
from pymongo import MongoClient
import os

client = MongoClient(
    "mongodb://uoixnano1h7qpi5:gISr9fKfV19n4KePWd2U@bcro8hmrdqj6mso-mongodb.services.clever-cloud.com:27017/bcro8hmrdqj6mso")
db = client["bcro8hmrdqj6mso"]

app = Flask(__name__)


@app.route("/test")
def hello():
    return " depoyer"


@app.route("/")
def teamInfo():
    list_of_all_team = []
    list_of_all_team.clear()
    a = db.info.find({}, {"_id": 0, "teamName": 1})
    for b in a:
        list_of_all_team.append(b["teamName"])
    return render_template("index.html", name_list=list_of_all_team)


@app.route("/showTeam/")
def showTeam():
    a = db.info.find({}, {"players": 0, "_id": 0, "leagues": 0})
    return render_template("allTeam.html", teamInformation=a)


@app.route("/addTeam/", methods=["POST", "GET"])
def addTeam():
    if request.method == 'POST':
        t = Team(request.form["teamName"])
        about = request.form.get("teamAbout", None)
        if about == "" or about == " ":
            about = "This team is prominent team in league"

        t.insert_team(teamLogo=request.form.get("teamLogo", None),
                      squadpic=request.form.get("squadPic", None),
                      founded=request.form.get("founded", None),
                      homeground=request.form.get("homeGround", None),
                      teamcost=eval(request.form.get("teamCost", 0)),
                      teamWebsite=request.form.get("teamWebsite", None),
                      teamowner=request.form.get("teamOwner", None),
                      teamcoach=request.form.get("teamCoach", None),
                      sponser=request.form.get("teamSponsor", None),
                      country=request.form.get("country", None),
                      about=about,
                      operation="insert")
        return redirect(url_for("showTeam"))
    else:
        return render_template("teamAddForm.html")


@app.route("/editTeam/<string:teamName>/", methods=["GET", "POST"])
def editTeam(teamName):
    if request.method == "GET":
        a = db.info.find_one({"teamName": teamName}, {"players": 0, "_id": 0, "fixture": 0})
        return render_template("teamEditForm.html", teamInfo=a)
    elif request.method == "POST":
        t = Team(teamName)
        about = request.form.get("teamAbout", None)
        if about == "" or about == " ":
            about = "This team is prominent team in league"
        t.insert_team(teamLogo=request.form.get("teamLogo", None),
                      squadpic=request.form.get("squadPic", None),
                      founded=request.form.get("founded", None),
                      homeground=request.form.get("homeGround", None),
                      teamcost=eval(request.form.get("teamCost", 0)),
                      teamWebsite=request.form.get("teamWebsite", None),
                      teamowner=request.form.get("teamOwner", None),
                      teamcoach=request.form.get("teamCoach", None),
                      sponser=request.form.get("teamSponsor", None),
                      country=request.form.get("country", None),
                      about=about,
                      operation="update")
        print(request.form)
        return redirect(url_for("showTeam"))


@app.route("/feedback/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        db.feedback.insert_one(dict(
            name=request.form.get("name", None),
            email=request.form.get("email", None),
            presentation=request.form.get("presentation", None),
            idea=request.form.get("idea", None),
            objective=request.form.get("objective", None),
            review=request.form.get("review", None)
        ))
        return redirect(url_for("teamInfo"))
    elif request.method == "GET":
        return render_template("feedback.html")


@app.route("/showfeedBack/")
def showFeedback():
    return render_template("feedbackshow.html", feedback=db.feedback.find({}))


@app.route("/matchFixture", methods=["GET", "POST"])
def matchFixture():
    return render_template("matchFixture.html")


@app.route("/topTeam")
def topTeam():
    return render_template("topTeam.html")


@app.route("/team_view/<string:teamName>")
def viewTeam(teamName):
    a = db.info.find_one({"teamName": teamName}, {"_id": 0})
    return render_template("teaminfo.html", teamdata=a)


@app.route("/team_delete/<string:teamName>", methods=["POST"])
def deleteTeam(teamName):
    if request.method == "POST":
        db.info.delete_one({"teamName": teamName})
        return redirect(url_for("showTeam"))


@app.route("/teamPlayers/<string:teamName>")
def teamPlayers(teamName):
    a = db.info.find_one({"teamName": teamName}, {"_id": 0, "players": 1, "teamName": 1})
    return render_template("teamplayers.html", teamPlayersData=a)


@app.route("/addplayers/<string:teamName>", methods=["GET", "POST"])
def addPlayers(teamName):
    if request.method == "POST":
        t = Team(teamName)
        about = request.form.get("about", None)
        if about == "" or about == " ":
            about = "This Player is a prominent Player in " + teamName

        t.insertPlayer(playername=request.form.get("playerName", None),
                       country=request.form.get("country", None),
                       age=request.form.get("playerAge", None),
                       dateofbirth=request.form.get("playerDateOfBirth", None),
                       numberofgoals=request.form.get("numberOfGoals", None),
                       photo=request.form.get("playerPhoto", None),
                       playerposition=request.form.get("playerPosition", None),
                       playercost=request.form.get("playerCost", None),
                       jerseynum=request.form.get("playerJerseyNum", 0),
                       about=about, operation="insert",
                       oldPlayerName="dsada")
        return redirect(url_for("teamPlayers", teamName=teamName))
    elif request.method == "GET":
        return render_template("playerAddForm.html")


@app.route("/editplayers/<string:teamName>/<string:playerName>", methods=["GET", "POST"])
def editPlayers(teamName, playerName):
    if request.method == "POST":
        t = Team(teamName)
        about = request.form.get("about", None)
        if about == "" or about == " ":
            about = "This Player is a prominent Player in " + teamName

        t.insertPlayer(playername=request.form.get("playerName", None),
                       country=request.form.get("country", None),
                       age=request.form.get("playerAge", None),
                       dateofbirth=request.form.get("playerDateOfBirth", None),
                       numberofgoals=request.form.get("numberOfGoals", None),
                       photo=request.form.get("playerPhoto", None),
                       playerposition=request.form.get("playerPosition", None),
                       playercost=request.form.get("playerCost", None),
                       jerseynum=request.form.get("playerJerseyNum", 0),
                       about=about,
                       operation="update",
                       oldPlayerName=playerName)
        return redirect(url_for("teamPlayers", teamName=teamName))
    elif request.method == "GET":

        mydict = {"Goalkeeper": "Goalkeeper",
 "Right full back": "Right full back",
                  "Left full back": " Left full back",
                  "Right half back": "Right half back",
                  "Centre half back": "Centre half back",
                  "Left half back": "Left half back"}
        a = db.info.aggregate([
            {"$unwind": "$players"},
            {"$match": {"teamName": teamName, "players.playerName": playerName}},
            {"$project": {"players": 1, "_id": 0}}
        ], useCursor=False)
        abc = ""
        for ab in a:
            abc = ab["players"]
        return render_template("playerEditForm.html", teamPlayerData=abc, mydict=mydict, target=abc["playerPosition"])


@app.route("/deleteplayers/<string:teamName>/<string:playerName>", methods=["POST"])
def deletePlayers(teamName, playerName):
    if request.method == "POST":
        db.info.update_one({"teamName": teamName}, {"$pull": {"players": {"playerName": playerName}}})
        return redirect(url_for("teamPlayers", teamName=teamName))


@app.route("/viewPlayer/<string:teamName>/<string:playerName>")
def viewPlayer(teamName, playerName):
    a = db.info.aggregate([
        {"$unwind": "$players"},
        {"$match": {"teamName": teamName, "players.playerName": playerName}},
        {"$project": {"players": 1, "_id": 0, "teamLogo": 1}}
    ], useCursor=False)
    abc = ""
    logo = ""
    for ab in a:
        logo = ab["teamLogo"]
        abc = ab["players"]
    return render_template("playerinfo.html", playerData=abc, logo=logo)


if __name__ == "__main__":
    # app.run()
    app.run(host="127.0.0.1", port=5000, debug=True)
