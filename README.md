# CLOCK-time
Python-based attendance management system that evaluates employee status (Present, Late, Half Day, Overtime, etc.) using clock-in and clock-out times.
# ⏰ Clock Time Attendance System

A simple Python program that checks employee attendance based on clock-in and clock-out times.

## 📌 Features

- Check employee attendance status
- Detect late arrivals
- Detect early departures
- Calculate overtime
- Beginner-friendly Python code

## 🛠️ Technology Used

- Python 3

## 📂 Project Structure

```text
clock-time-attendance/
│
├── clock_time.py
└── README.md
```

## 🚀 How It Works

The program takes:

- Clock-In Time
- Clock-Out Time

and determines whether the employee is:

- ✅ Present
- ⏰ Late Arrival
- 🚪 Early Departure
- 🕒 Half Day
- 💼 Overtime

### Example Output

```text
Enter clock-in time: 9
Enter clock-out time: 18

Status: Present
```

```text
Enter clock-in time: 10
Enter clock-out time: 18

Status: Late Arrival
```

```text
Enter clock-in time: 9
Enter clock-out time: 20

Status: Overtime
```

## ▶️ Run the Program

```bash
python clock_time.py
```

## 📖 Concepts Used

- Variables
- User Input
- If-Else Conditions
- While Loop
- Attendance Logic

## 🤝 Contributing

Feel free to fork this repository and submit pull requests.

## 📜 License

This project is licensed under the MIT License.

---
⭐ If you like this project, don't forget to star the repository!
