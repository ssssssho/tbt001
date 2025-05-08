from flask import Flask
from flask import render_template


app = Flask(__name__, static_folder='static')


@app.route('/')
def view_test():
    print("testtest")
    test = "a"
    dict_active = {"test1": "active"}
    list_test = []
    for row in range(0, 100):
        list_test.append(row)

    return render_template("app.html",
                           test=test,
                           dict_active=dict_active,
                           list_test=list_test)


@app.route("/test")
def view_app():
    print("testtest")
    test = "a"
    dict_active = {"test2": "active"}

    return render_template("top.html",
                           test=test,
                           dict_active=dict_active)

if __name__ == '__main__':
    app.run(host='192.168.3.4', port=5000, debug=True)