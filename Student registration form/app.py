from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector
from passlib.hash import bcrypt

app = Flask(__name__)

# Database connection details (replace with your credentials)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Jivan123@mysql",
    "database": "registration_db"
}


@app.route("/")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_user():
    # Form data
    name = request.form["name"]
    father_name = request.form["father_name"]
    mother_name = request.form["mother_name"]
    phone_number = request.form["phone_number"]
    email = request.form["email"]
    date_of_birth = request.form["date_of_birth"]
    address = request.form["address"]
    blood_group = request.form["blood_group"]
    department = request.form["department"]
    course = request.form["course"]
    password = request.form["password"]  # Implement hashing before storing

    # Hash the password using bcrypt
    hashed_password = bcrypt.hash(password)
    
    # Database connection
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert data into users table
    sql = "INSERT INTO users (student_name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (name, father_name, mother_name, phone_number, email, date_of_birth, address, blood_group, department, course, password)
    cursor.execute(sql, data)
    connection.commit()

    cursor.close()
    connection.close()

    return redirect(url_for("register"))  # Display success message or redirect elsewhere

if __name__ == "__main__":
    app.run(debug=True)
