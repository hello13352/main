from flask import Flask
from resources import user_management, remote_announce, remote_update, software_settings

app = Flask(__name__)

# 注册 API 资源
app.register_blueprint(user_management.bp, url_prefix='/user-management')
app.register_blueprint(remote_announce.bp, url_prefix='/remote-announce')
app.register_blueprint(remote_update.bp, url_prefix='/remote-update')
app.register_blueprint(software_settings.bp, url_prefix='/software-settings')

@app.route('/')
def index():
    return {"message": "管理端 API 已启动"}

# Vercel 不使用 __main__ 运行，而是直接提供 app 变量
