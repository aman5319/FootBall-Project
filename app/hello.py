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


@app.route("/matchFixture", methods=["GET", "POST"])
def matchFixture():
    return render_template("matchFixture.html")


@app.route("/topTeam")
def topTeam():
    return render_template("topTeam.html")


@app.route("/team_view/<string:teamName>")
def viewTeam(teamName):
    a = db.info.find_one({"teamName": teamName}, {"_id": 0, })
    return render_template("teaminfo.html")


@app.route("/team_delete/<string:teamName>", methods=["POST"])
def deleteTeam(teamName):
    if request.method == "POST":
        db.info.delete_one({"teamName": teamName})
        return redirect(url_for("showTeam"))


if __name__ == "__main__":
    # app.run()
    app.run(host="127.0.0.1", port=5000, debug=True)
