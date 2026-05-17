# ✈️ TravelGo – Cloud-Based Travel Booking System

TravelGo is a cloud-based travel booking web application built using Flask and AWS services.  
The platform allows users to register, log in, browse transport and hotel services, book tickets, and receive booking notifications using AWS SNS.

---

# 🚀 Features

- User Registration & Login
- Session-based Authentication
- Bus Booking
- Train Booking
- Flight Booking
- Hotel Booking
- Seat Selection
- Payment Workflow
- Booking Ticket Generation
- AWS SNS Notifications
- DynamoDB Database Integration
- Cloud-ready Flask Application

---

# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Backend
- Python
- Flask

## AWS Services
- AWS DynamoDB
- AWS SNS
- AWS EC2

## Other Libraries
- Boto3

---

# ☁️ AWS Architecture

```text
Frontend UI
     ↓
Flask Application (EC2)
     ↓
AWS DynamoDB
     ↓
AWS SNS Notifications
```

---

# 📂 Project Structure

```bash
travel-go/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── bus.html
│   ├── train.html
│   ├── flight.html
│   ├── hotels.html
│   ├── seat.html
│   ├── payment.html
│   └── ticket.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── screenshots/
```

---

# 🔐 Authentication

The application uses Flask session management for maintaining user authentication.

Users can:
- Register
- Login
- Logout
- Access personalized dashboard

---

# 🗄️ Database

AWS DynamoDB is used as the primary database.

## Tables Used

### travel-Users
Stores:
- User name
- Email
- Password
- Login count

### Bookings
Stores:
- Booking details
- Transport information
- Payment details
- User email
- Booking ID

---

# 📢 AWS SNS Integration

AWS SNS is used for sending booking confirmation notifications.

After successful payment:
- Booking details are stored in DynamoDB
- SNS publishes booking confirmation message

---

# ⚙️ Environment Variables

The project uses environment variables for security.

## Required Variables

```bash
FLASK_SECRET_KEY=your_secret_key
AWS_REGION=ap-south-1
```

---

# ▶️ Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/travel-go.git
cd travel-go
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create `requirements.txt`

```txt
Flask
boto3
```

---

# ▶️ Run Application

```bash
python app.py
```

Application runs on:

```bash
http://127.0.0.1:5000
```

---

# 📸 Application Modules

## Home Page
Displays:
- Travel options
- Navigation menu

## Dashboard
Displays:
- User bookings
- Booking history

## Booking System
Supports:
- Bus booking
- Train booking
- Flight booking
- Hotel booking

## Payment System
Handles:
- Payment method selection
- Payment reference tracking

## Ticket Generation
Generates:
- Booking ID
- Ticket details
- Payment confirmation

---

# 🔍 Key Backend Features

- UUID-based Booking IDs
- Session Handling
- AWS Cloud Integration
- DynamoDB Query Optimization
- Error Handling
- Secure Environment Variables

---

# 📈 Future Improvements

- Password Hashing
- Payment Gateway Integration
- Admin Dashboard
- Responsive Mobile Design
- Real-time Booking Updates
- Email Notifications
- Docker Deployment
- CI/CD Pipeline

---

# 🧠 Learning Outcomes

This project helped in understanding:

- Flask Backend Development
- AWS Cloud Services
- DynamoDB Operations
- SNS Notifications
- Session Management
- Cloud Deployment Concepts
- Full Stack Application Workflow

---

# 👨‍💻 Author

## S.Manoj Kumar
- GitHub: https://github.com/manojyadav1222

---

# ⭐ Project Highlights

✔ Flask Backend  
✔ AWS DynamoDB Integration  
✔ AWS SNS Notifications  
✔ Cloud-based Architecture  
✔ Booking Workflow System  
✔ Session Authentication  
✔ Internship-ready Project  
