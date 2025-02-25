from flask_api import FlaskAPI, Resource
from flask import request

bp = FlaskAPI(__name__)

class SoftwareSettings(Resource):
    def post(self):
        data = request.data
        mode = data.get('mode')
        # 启用公益模式
        if mode == "公益":
            end_time = data.get('end_time')
            return {"status": "success", "message": f"公益模式已启用，结束时间: {end_time}"}
        else:
            return {"status": "failed", "message": "无效模式"}

bp.add_resource(SoftwareSettings, '/')
