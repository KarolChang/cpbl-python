"""Flask 應用工廠與全域註冊。"""

from flask import Flask, render_template
from flask_cors import CORS
from app.routes.index import register_route
from app.errors.error_handle import handle_error


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    CORS(app)

    # 註冊 Blueprint
    register_route(app)

    # 註冊首頁
    @app.route("/")
    def index():
        return render_template("index.html")

    # 註冊全域錯誤處理
    @app.errorhandler(Exception)
    def error_handler(error):
        return handle_error(error)

    return app
