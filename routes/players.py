from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import crawlers.players

players_blueprint = Blueprint('players', __name__)

# form page
@players_blueprint.route("/players", methods=["POST", "GET"])
def playersIndex(): 
  if request.method == "POST":
    return redirect(url_for("players.players"))

  else:
    return render_template("players.html")
  
# json
@players_blueprint.route("/players/data")
def players(): 
  data = crawlers.players.fetchDatas()
  return data
  # return {"data": data}