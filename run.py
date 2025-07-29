"""專案啟動入口，建立並啟動 Flask 應用。"""

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
