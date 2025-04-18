from routes.record import record_blueprint
from routes.schedule import schedule_blueprint
from routes.standings import standings_blueprint
from routes.today_game import todaygame_blueprint
from routes.single_data import singledata_blueprint
from routes.players import players_blueprint
from routes.player_trans import playertrans_blueprint


def register_route(app):
    app.register_blueprint(record_blueprint)
    app.register_blueprint(schedule_blueprint)
    app.register_blueprint(standings_blueprint)
    app.register_blueprint(todaygame_blueprint)
    app.register_blueprint(singledata_blueprint)
    app.register_blueprint(players_blueprint)
    app.register_blueprint(playertrans_blueprint)
