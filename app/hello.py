from flask import Flask, render_template, request, redirect, url_for
from crudClass import Team
from pymongo import MongoClient
import os

client = MongoClient(
    "mongodb://uoixnano1h7qpi5:gISr9fKfV19n4KePWd2U@bcro8hmrdqj6mso-mongodb.services.clever-cloud.com:27017/bcro8hmrdqj6mso")
db = client["bcro8hmrdqj6mso"]

app = Flask(__name__)


@app.route("/")
def hello():
    return " depoyer"


@app.route("/teamName/")
def teamInfo():
    list_of_all_team = []
    list_of_all_team.clear()
    a = db.info.find({}, {"_id": 0, "teamName": 1})
    for b in a:
        list_of_all_team.append(b["teamName"])
    return render_template("tempa.html", name_list=list_of_all_team)


@app.route("/addTeam/", methods=["POST", "GET"])
def addTeam():
    if request.method == 'POST':
        t = Team(request.form["teamName"])
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
                      operation="insert")
        return redirect(url_for("teamInfo"))
    else:
        return render_template("teamAddForm.html")


@app.route("/editTeam/<string:teamName>/", methods=["GET", "POST"])
def editTeam(teamName):
    if request.method == "GET":
        a = db.info.find_one({"teamName": teamName}, {"players": 0, "_id": 0, "fixture": 0})
        return render_template("teamEditForm.html", teamInfo=a)
    elif request.method == "POST":
        t = Team(teamName)
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
                      operation="update")
        return redirect(url_for("teamInfo"))


if __name__ == "__main__":
    app.run()
