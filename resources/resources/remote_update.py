from flask_api import FlaskAPI, Resource
from flask import request

bp = FlaskAPI(__name__)

class RemoteUpdate(Resource):
    def post(self):
        data = request.data
        download_url = data.get('download_url')
        # 发布更新逻辑
        return {"status": "success", "message": f"更新发布成功，下载地址：{download_url}"}

bp.add_resource(RemoteUpdate, '/')
