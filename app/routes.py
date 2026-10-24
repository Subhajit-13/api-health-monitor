from flask import Blueprint, render_template, request

from app.monitor import check_api, validate_url

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html")



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

    return render_template(
        "index.html",
        result=result,
        submitted_url=url,
    )

