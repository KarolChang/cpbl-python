from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import apis.gettodaygame

todaygame_blueprint = Blueprint('todaygame', __name__)

# form page
@todaygame_blueprint.route("/todaygame", methods=["POST", "GET"])
def todaygameIndex(): 
  if request.method == "POST":
    gameDate = request.form["gameDate"]
    # kindCode = request.form["kindCode"]

    return redirect(url_for("todaygame.todaygame", gameDate=gameDate))

  else:
    return render_template("today_game.html")

# json
@todaygame_blueprint.route("/todaygame/<gameDate>")
def todaygame(gameDate): 
  data = apis.gettodaygame.fetchDatas(gameDate)
  data = json.loads(data)
  dataA = json.loads(data["GameADetailJson"])
  dataD = json.loads(data["GameDDetailJson"])
  return {"data": {
    "一軍": dataA,
    "二軍": dataD
  }}