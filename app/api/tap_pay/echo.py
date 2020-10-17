from sanic import Blueprint
from sanic.log import logger
from sanic.response import json

bp = Blueprint("tap_pay", url_prefix="")


@bp.route("/echo", methods=["GET"])
async def echo(request):
    logger.info(
        json.dumps(
            {
                "parsed": True,
                "args": request.args,
                "url": request.url,
                "query_string": request.query_string,
            }
        )
    )
    return json(
        {
            "parsed": True,
            "args": request.args,
            "url": request.url,
            "query_string": request.query_string,
        }
    )
