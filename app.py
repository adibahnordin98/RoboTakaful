from flask import Flask, render_template


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SECRET_KEY'] = 'any secret key'

# Meta
META_IMAGE_LINK = ""
META_DESCRIPTION = ""


@app.route("/")
def index():
    return render_template("home.html", title='RoboTakaful',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/login")
def login():
    return render_template("login.html", title='RoboTakaful | Login',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/signup")
def signup():
    return render_template("signup.html", title='RoboTakaful | SignUp',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


@app.route("/compare")
def compare():
    return render_template("wizard.html", title='RoboTakaful | Compare Tool',
                           meta_description=META_DESCRIPTION,
                           meta_image=META_IMAGE_LINK)


if __name__ == '__main__':
    # HOST = "0.0.0.0"
    # PORT = 5000

    # httpserver.serve(app, host=HOST, port=PORT)
    app.run(port=5000, debug=True)
