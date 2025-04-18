from flask import Flask, render_template, jsonify
from flask_cors import CORS
from routes.index import register_route
from errors.error_handle import handle_error


app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


# route
@app.route("/")
def index():
    return render_template("index.html")


# error handling
# @app.errorhandler(Exception)
# def error_handler(error):
#     return handle_error(error)


register_route(app)

# run server
if __name__ == "__main__":
    app.run()
