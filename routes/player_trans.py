from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import crawlers.playertrans

playertrans_blueprint = Blueprint('playertrans', __name__)

# form page
@playertrans_blueprint.route("/playertrans", methods=["POST", "GET"])
def playertransIndex():
  if request.method == "POST":
    year = request.form["year"]
    month = request.form["month"]
    return redirect(url_for("playertrans.playertrans", year=year, month=month))

  else:
    return render_template("playerTrans.html")
  
# json
@playertrans_blueprint.route("/playertrans/<year>/<month>")
def playertrans(year, month): 
  data = crawlers.playertrans.fetchDatas(year, month)
  return data