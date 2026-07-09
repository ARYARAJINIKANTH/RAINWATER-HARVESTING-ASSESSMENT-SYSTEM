from flask import Flask, render_template, request, redirect, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "rainwater_secret"

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="rainwater_db",
    user="postgres",
    password="ARYA2413"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    try:
        name = request.form["name"]
        location = request.form["location"]
        area = float(request.form["area"])
        rainfall = float(request.form["rainfall"])
        runoff = float(request.form["runoff"])
        roof_type = request.form["roofType"]

        # Rainwater Harvesting Formula
        harvest_volume = (area * rainfall * runoff) / 1000
        liters = harvest_volume * 1000
        daily_yield = liters / 365

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO assessments
            (name, location, area, rainfall, runoff,
             roof_type, harvest_volume, liters, daily_yield)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            name,
            location,
            area,
            rainfall,
            runoff,
            roof_type,
            harvest_volume,
            liters,
            daily_yield
        ))

        conn.commit()
        cur.close()

        flash("Assessment Saved Successfully!")
        return redirect("/")

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)