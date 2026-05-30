# ⏰ Punch Time

A simple Python-based Punch Time Attendance System that checks employee attendance based on punch-in and punch-out times.

## 🚀 Features

- Check employee attendance status
- Present, Late, Early Arrival
- Half Day, Short Day, Overtime
- Beginner-friendly Python project
- Console-based application

## 📋 Attendance Rules

| Punch In | Punch Out | Status |
|-----------|------------|---------|
| 9 | 18 | Present |
| < 12 | 18 | half day |
| > 9 | 18 | SHORT DAY |
| Any | > 18 | Overtime |
| Any | < 18 | Short Day |
| Any | <= 15 | Half Day |

## 🛠️ Technology

- Python 3

## ▶️ How to Run

python PUNCH.py

## 📸 Example

Enter Punch In Time: 9
Enter Punch Out Time: 18

Status: Present

## 📂 Project Structure

punch-time/
│
├── PUNCH.py
└── README.md

## 🎯 Learning Concepts

- Variables
- User Input
- Conditional Statements
- Loops
- Attendance Logic

## 👨‍💻 Author

Arnav Tiwari
