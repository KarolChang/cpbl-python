from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import crawlers.playertrans

playertrans_blueprint = Blueprint('playertrans', __name__)

# form page
@playertrans_blueprint.route("/playertrans", methods=["POST", "GET"])
def playersIndex(): 
  if request.method == "POST":
    return redirect(url_for("playertrans.playertrans"))

  else:
    return render_template("playertrans.html")
  
# json
@playertrans_blueprint.route("/playertrans/data")
def playertrans(): 
  data = crawlers.playertrans.fetchDatas()
  return data
  # return {"data": data}