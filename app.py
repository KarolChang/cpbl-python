# 使用 flask
from flask import Flask, render_template
from flask_cors import CORS

from routes.record import record_blueprint
from routes.schedule import schedule_blueprint
from routes.standings import standings_blueprint
from routes.today_game import todaygame_blueprint
from routes.single_data import singledata_blueprint

app = Flask(__name__)
CORS(app)

# 路由
# index
@app.route("/")
def index():
  return render_template("index.html")

app.register_blueprint(record_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(standings_blueprint)
app.register_blueprint(todaygame_blueprint)
app.register_blueprint(singledata_blueprint)

# run server
if __name__ == "__main__":
  app.run()