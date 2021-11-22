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

    return redirect(url_for("todaygame.todaygame", gameDate=gameDate))

  else:
    return render_template("today_game.html")

# json
@todaygame_blueprint.route("/todaygame/<gameDate>")
def todaygame(gameDate): 
  data = apis.gettodaygame.fetchDatas(gameDate)
  data = json.loads(data)
  
  newData = {}
  for key,item in data.items():
    if type(item) == str:
      newData[key] = json.loads(item) if json.loads(item) else item
    else:
      newData[key] = item
      
  return newData
