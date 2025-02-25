from flask import Flask
from flask_api import FlaskAPI
from resources import user_management, remote_announce, remote_update, software_settings

app = FlaskAPI(__name__)

# 注册 API 资源
app.register_blueprint(user_management.bp, url_prefix='/user-management')
app.register_blueprint(remote_announce.bp, url_prefix='/remote-announce')
app.register_blueprint(remote_update.bp, url_prefix='/remote-update')
app.register_blueprint(software_settings.bp, url_prefix='/software-settings')

@app.route('/')
def index():
    return {"message": "管理端 API 已启动"}

if __name__ == '__main__':
    app.run(debug=True)
