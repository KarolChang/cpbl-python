from flask import Blueprint
from flask import Flask, render_template, redirect, url_for, request
import json

import crawlers.standings

standings_blueprint = Blueprint("standings", __name__)


# form page
@standings_blueprint.route("/standings", methods=["POST", "GET"])
def standingsIndex():
    if request.method == "POST":
        kindCode = request.form["kindCode"]
        seasonCode = request.form["seasonCode"]
        if (kindCode == "") & (seasonCode == ""):
            return redirect(url_for("standings.nowStandings"))

        return redirect(
            url_for("standings.standings", kindCode=kindCode, seasonCode=seasonCode)
        )

    else:
        return render_template("standings.html")


# json
@standings_blueprint.route("/standings/<kindCode>/<seasonCode>")
def standings(kindCode, seasonCode):
    data = crawlers.standings.fetchDatas(kindCode, seasonCode)
    return {"data": data}


@standings_blueprint.route("/standings/now")
def nowStandings():
    data = crawlers.standings.fetchDatas()
    return {"data": data}
