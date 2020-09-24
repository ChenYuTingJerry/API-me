import json
from marshmallow import Schema, fields
from sanic import Blueprint, response

from app.serializers.user import BlockUserSerializer
from app.services import me_service

bp = Blueprint("me_block_users", url_prefix="/blocked_users")


class CreateBlockUserSchema(Schema):
    token = fields.String()
    blocked_user_id = fields.Int(required=True)


class GetBlockUserSchema(Schema):
    offset = fields.Int(required=True)
    limit = fields.Int(required=True)
    token = fields.String(required=True)
    device_system_name = fields.String()


create_block_user_schema = CreateBlockUserSchema()
get_block_user_schema = GetBlockUserSchema()


@bp.route("/", methods=["GET"])
async def get_block_users(request):
    current_user = request.ctx.current_user
    errors = get_block_user_schema.validate(request.args)
    if errors:
        return response.json(errors, status=422)
    limit = request.args.get("limit", 0)
    offset = request.args.get("offset", 0)
    users = await me_service.get_block_users(current_user.id, limit, offset)
    blocked_users = tuple(
        map(lambda u: BlockUserSerializer(u, u.picture).to_dict(), users,)
    )
    return response.json(blocked_users)


@bp.route("/", methods=["POST"])
async def create_block_user(request):
    current_user = request.ctx.current_user
    request_body = json.loads(request.body)
    errors = create_block_user_schema.validate(request_body)
    if errors:
        return response.json(errors, status=422)
    await me_service.create_block_user(
        current_user.id, request_body["blocked_user_id"]
    )
    return response.json({"success": True})


@bp.route("/<blocked_user_id:int>", methods=["DELETE"])
async def delete_block_user(request, blocked_user_id):
    current_user = request.ctx.current_user
    await me_service.remove_block_user(current_user.id, blocked_user_id)
    return response.json({"success": True})
