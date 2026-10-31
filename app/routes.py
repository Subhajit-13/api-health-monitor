from flask import Blueprint, render_template, request
from app.monitor import check_api, validate_url
from app.database import get_api_check_history, save_api_check

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    history = get_api_check_history()
    return render_template("index.html", history=history)



@main_bp.route("/check", methods=["POST"])
def check():
    url = request.form.get("url", "").strip()

    is_valid, error_message = validate_url(url)

    if not is_valid:
        result = {
            "url": url,
            "reachable": False,
            "healthy": False,
            "status_code": None,
            "response_time_ms": 0,
            "error": error_message,
        }
    else:
        result = check_api(url)
        save_api_check(result)

    return render_template(
        "index.html",
        result=result,
        submitted_url=url,
    )

