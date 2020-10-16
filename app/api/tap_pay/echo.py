from sanic import Blueprint
from sanic.response import json

bp = Blueprint("tap_pay", url_prefix="/")


@bp.route("/echo", methods=["GET"])
async def echo(request):
    return json(
        {
            "parsed": True,
            "args": request.args,
            "url": request.url,
            "query_string": request.query_string,
        }
    )
