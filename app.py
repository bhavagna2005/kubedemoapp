
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h2>Registration Form</h2>
<form method="POST">
    <input name="name" placeholder="Enter name" required>
    <br><br>
    <input name="email" type="email" placeholder="Enter email" required>
    <br><br>
    <button type="submit">Register</button>
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = f"Registration successful for {name} ({email})"

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
