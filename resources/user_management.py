from flask_api import FlaskAPI, Resource
from flask import request

bp = FlaskAPI(__name__)

class UserManagement(Resource):
    def get(self):
        # 返回用户信息
        return {"status": "success", "message": "查询用户信息"}

    def post(self):
        # 注册密钥
        data = request.data
        key = data.get('key')
        machine_id = data.get('machine_id')
        # 注册逻辑
        return {"status": "success", "message": f"密钥 {key} 注册成功，绑定机器号 {machine_id}"}

    def put(self):
        # 更新用户信息（例如封禁）
        data = request.data
        key = data.get('key')
        action = data.get('action')
        # 执行封禁、恢复操作
        return {"status": "success", "message": f"密钥 {key} 操作: {action} 完成"}

bp.add_resource(UserManagement, '/')
