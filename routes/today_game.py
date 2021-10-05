from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import apis.gettodaygame

todaygame_blueprint = Blueprint('todaygame', __name__)

# form page
@todaygame_blueprint.route("/todaygame", methods=["POST", "GET"])
def todaygameIndex(): 
  if request.method == "POST":
    return redirect(url_for("todaygame.todaygame"))

  else:
    return render_template("today_game.html")

# json
@todaygame_blueprint.route("/todaygame/data")
def todaygame(): 
  data = apis.gettodaygame.fetchDatas()
  data = json.loads(data)
  return {"data": data}