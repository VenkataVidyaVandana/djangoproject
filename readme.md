# Django Booking System

## 📌 Overview

This project is a backend booking system built using **Django** and **PostgreSQL**.
It allows users to sign up, log in, book rooms, and enables admins to manage rooms.


---

## 🚀 Features

###  User Authentication

* User Signup
* User Login
* Role-based access (Admin / User)

###  Room Management 

* Create Room
* Update Room
* Delete Room
* View Rooms

### Booking System

* Create Booking
* Delete Booking
* Prevent overlapping bookings

### Pricing Logic

* Automatically calculates total price:

  ```
  total_price = (check_out - check_in) * room.price
  ```

### Booking Summary

* View all bookings of a user
* Displays:

  * User name
  * Rooms booked
  * Room capacity
  * Total price (sum of bookings)

---

## Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Tools:** Postman, Git, GitHub

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Server

```bash
python manage.py runserver
```

---

##  API Endpoints

###  Authentication

| Method | Endpoint   | Description   |
| ------ | ---------- | ------------- |
| POST   | `/signup/` | Register user |
| POST   | `/login/`  | Login user    |

---

###  Rooms

| Method | Endpoint                        | Description              |
| ------ | -----------------------         | ------------------------ |
| GET    | `/room/`                        | Get all rooms            |
| POST   | `/room/create/`                 | Create room (Admin only) |
| PUT    | `/rooms/update/<room_number>/`  | Update room (Admin only) |
| DELETE | `/rooms/delete/<room_number>/`  | Delete room (Admin only) |

---

###  Bookings

| Method | Endpoint                | Description    |
| ------ | ----------------------- | -------------- |
| GET    | `/booking/<user_id>/`   | get booking    |
| POST   | `/booking/create/`      | Create booking |
| DELETE | `/booking/delete/<id>/` | Delete booking |


---

##  Validation & Logic

* Check-out date must be after check-in
* Prevent overlapping bookings
* Only admin can manage rooms
* Pricing calculated automatically

---

## 👩‍💻 Author

**Vidya Vandana**
