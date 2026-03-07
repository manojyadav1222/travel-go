import os
import uuid
import datetime
import certifi
from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "travelgo_secret"

# ---------------- MONGODB CONNECTION ----------------

MONGO_URI = "mongodb+srv://travelgo_admin:dbtravelgo9346@travelgocluster.qyjpcjs.mongodb.net/travelgo?retryWrites=true&w=majority"

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["travelgo"]

users_collection = db["users"]
bookings_collection = db["bookings"]

# ---------------- STATIC DATA ----------------

bus_data = [
    {"id": "B1", "name": "Super Luxury Bus", "source": "Hyderabad", "dest": "Bangalore", "price": 800},
    {"id": "B2", "name": "Express Bus", "source": "Chennai", "dest": "Hyderabad", "price": 700}
]

train_data = [
    {"id": "T1", "name": "Rajdhani Express", "source": "Hyderabad", "dest": "Delhi", "price": 1500},
    {"id": "T2", "name": "Shatabdi Express", "source": "Chennai", "dest": "Bangalore", "price": 900}
]

flight_data = [
    {"id": "F1", "name": "Indigo 6E203", "source": "Hyderabad", "dest": "Dubai", "price": 8500},
    {"id": "F2", "name": "Air India AI102", "source": "Delhi", "dest": "Singapore", "price": 9500}
]

hotel_data = [
    {"id": "H1", "name": "Grand Palace", "city": "Chennai", "type": "Luxury", "price": 4000},
    {"id": "H2", "name": "Budget Inn", "city": "Hyderabad", "type": "Budget", "price": 1500}
]

# ---------------- HELPER FUNCTION ----------------

def get_transport_info(t_id):

    for bus in bus_data:
        if bus["id"] == t_id:
            return {
                "type": "Bus",
                "source": bus["source"],
                "destination": bus["dest"],
                "details": f"{bus['name']} ({bus['source']} - {bus['dest']})"
            }

    for train in train_data:
        if train["id"] == t_id:
            return {
                "type": "Train",
                "source": train["source"],
                "destination": train["dest"],
                "details": f"{train['name']} ({train['source']} - {train['dest']})"
            }

    for flight in flight_data:
        if flight["id"] == t_id:
            return {
                "type": "Flight",
                "source": flight["source"],
                "destination": flight["dest"],
                "details": f"{flight['name']} ({flight['source']} - {flight['dest']})"
            }

    for hotel in hotel_data:
        if hotel["id"] == t_id:
            return {
                "type": "Hotel",
                "source": hotel["city"],
                "destination": hotel["city"],
                "details": f"{hotel['name']} in {hotel['city']}"
            }

    return {"type": "General", "source": "", "destination": "", "details": ""}

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return render_template("index.html")

# ---------------- REGISTER ----------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        user = {
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"],
            "created_at": str(datetime.date.today())
        }

        users_collection.insert_one(user)

        return redirect("/login")

    return render_template("register.html")

# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        user = users_collection.find_one({
            "email": request.form["email"]
        })

        if user and user["password"] == request.form["password"]:

            session["user"] = user["email"]
            session["name"] = user["name"]

            return redirect("/dashboard")

        return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")

# ---------------- DASHBOARD ----------------

@app.route('/dashboard')
def dashboard():

    if "user" not in session:
        return redirect("/login")

    bookings = list(bookings_collection.find({
        "email": session["user"]
    }))

    return render_template(
        "dashboard.html",
        name=session["name"],
        bookings=bookings
    )

# ---------------- SERVICES ----------------

@app.route('/bus')
def bus():
    return render_template("bus.html", buses=bus_data)

@app.route('/train')
def train():
    return render_template("train.html", trains=train_data)

@app.route('/flight')
def flight():
    return render_template("flight.html", flights=flight_data)

@app.route('/hotels')
def hotels():
    return render_template("hotels.html", hotels=hotel_data)

# ---------------- SEAT ----------------

@app.route('/seat/<transport_id>/<price>')
def seat(transport_id, price):

    if "user" not in session:
        return redirect("/login")

    return render_template("seat.html", id=transport_id, price=price)

# ---------------- BOOK ----------------

@app.route('/book', methods=['POST'])
def book():

    if "user" not in session:
        return redirect("/login")

    transport_id = request.form["transport_id"]
    seats = request.form.get("seat")
    price = request.form["price"]

    info = get_transport_info(transport_id)

    session["booking_flow"] = {
        "transport_id": transport_id,
        "type": info["type"],
        "source": info["source"],
        "destination": info["destination"],
        "details": info["details"],
        "seat": seats,
        "price": price,
        "date": str(datetime.date.today())
    }

    return render_template("payment.html", booking=session["booking_flow"])

# ---------------- PAYMENT ----------------

@app.route('/payment', methods=['POST'])
def payment():

    if "user" not in session:
        return redirect("/login")

    booking = session["booking_flow"]

    booking["booking_id"] = str(uuid.uuid4())[:8]
    booking["email"] = session["user"]
    booking["payment_method"] = request.form["method"]
    booking["payment_reference"] = request.form["reference"]

    bookings_collection.insert_one(booking)

    session.pop("booking_flow")

    return render_template("ticket.html", booking=booking)

# ---------------- LOGOUT ----------------

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)