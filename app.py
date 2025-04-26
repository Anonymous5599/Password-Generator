from flask import Flask, render_template, request
from generator import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        user_name = request.form.get("user_name", "")
        length = int(request.form.get("length", 12))
        use_upper = "use_upper" in request.form
        use_lower = "use_lower" in request.form
        use_numbers = "use_numbers" in request.form
        use_symbols = "use_symbols" in request.form

        password = generate_password(user_name, length, use_upper, use_lower, use_numbers, use_symbols)
        
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
