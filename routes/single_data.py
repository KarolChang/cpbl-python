from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import crawlers.singledata

singledata_blueprint = Blueprint('singledata', __name__)

# form page
@singledata_blueprint.route("/singledata", methods=["POST", "GET"])
def singledataIndex(): 
  if request.method == "POST":
    return redirect(url_for("singledata.singledata"))

  else:
    return render_template("single_data.html")
  
# json
@singledata_blueprint.route("/singledata/data")
def singledata(): 
  data = crawlers.singledata.fetchDatas()
  print('data', data)
  return {"data": data}