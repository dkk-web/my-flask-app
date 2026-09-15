from flask import Flask
app = Flask(__name__) #__name__代表目前执行的模组

@app.route("/") # 函式的装饰（Decorator）
def home():
    return "凯哥牛逼"
@app.route('/test') #代表我们要处理的网站路径
def text():
    return "This is Tast"

if __name__ == "__main__": # 如果以主程式执行
    app.run() #立刻启动服务器