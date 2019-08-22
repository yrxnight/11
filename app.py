from flask import Flask,render_template

app = Flask(__name__)

#如何返回一个网页（模板）
#如何给模板返回数据
@app.route('/')
def hello_world():
    # 比如需要传入网址
    url_str = 'www.itheima.com'
    my_list = [1,3,5,7,9]
    my_dict = {
        'name':'xiniu',
        'url':'www.itheima.com'
    }

    # 通常，模板中使用的变量名和需要传递的数据的变量名保持一致　
    return render_template("index.html",url_str=url_str,my_list=my_list,my_dict=my_dict )
# @app.route()

if __name__ == '__main__':
    app.run()
