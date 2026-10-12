from flask import Flask , render_template, url_for, request, jsonify, flash, redirect

app = Flask(__name__)

#Jinga templaing means you want to embed python like code in HTML
#URL => endpoint /

app.secret_key = "some secret message or key"
@app.route("/")
def hello_world():
    # query = request.args.get("q")
    # print(query)
    # name = request.args.get("name", default = "anonymous")
    # subject = request.args.get("subject")

    # print(url_for("static", filename = "style.css"))

    # data = {"message" : "Welcome to the platform! "}

    # return jsonify(data), 200
    # return render_template("index.html", name = name, sub = subject)
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return "<p>Login Page</p>"

# @app.route("/login",methods = ["GET","POST"])
# def login():
#     if request.method == "POST":
#         name = request.form["username"]
#         password = request.form["password"]


#         # send it to database and
#         friends = ["Adam","Bob","Charlie","Dan"]
#         header = "<header>ABC Website</header>"
    
#         return render_template("Welcome.html", name = name, password = password, friends = friends, header = header)
#     else:
#         return render_template("login.html")


# @app.route("/handle-login", methods = ["GET","POST"])
# def handle_login():
#     if request.method =="POST":
#         print(request.form)
#         name = request.form["username"]
#         password = request.form["password"]

#         # send it to database and verify 

#         return f"<p>Welcome {name} !</p>"
#     return "<p> This page is to handle login </p>"


@app.route("/contact")
def contact():
    flash("support timings are from 9-5")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True)
