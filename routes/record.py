from datetime import datetime
from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import apis.getlive
import utils.timeTool as TimeTool

record_blueprint = Blueprint("record", __name__)


# form page
@record_blueprint.route("/record", methods=["POST", "GET"])
def recordIndex():
    if request.method == "POST":
        gameSno = request.form["gameSno"]
        kindCode = request.form["kindCode"]
        year = request.form["year"]
        dataType = request.form["dataType"]

        # 第一個record是blueprint的名稱，第二個record是function名稱
        return redirect(
            url_for(
                "record.record",
                gameSno=gameSno,
                kindCode=kindCode,
                year=year,
                dataType=dataType,
            )
        )

    else:
        current_year = datetime.now().year
        years = TimeTool.getPreviousYears(current_year, 5)
        return render_template("record.html", years=years, selected_year=current_year)


# json
@record_blueprint.route("/record/<gameSno>/<kindCode>/<year>/<dataType>")
def record(gameSno, kindCode, year, dataType):
    data = apis.getlive.fetchDatas(gameSno, kindCode, year, dataType)
    data = json.loads(data)
    return {"data": data}
