import traceback
import os

from flask import jsonify


def handle_error(error):
    status_code = getattr(error, "code", 500)
    is_dev = os.environ.get("FLASK_ENV") == "development"

    return (
        jsonify(
            {
                "error": str(error),
                "trace": traceback.format_exc() if is_dev else None,
                "message": "Something went wrong!",
            }
        ),
        status_code,
    )
