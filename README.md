# 🎓 SnapClass AI Attendance System

## 🚀 Overview

SnapClass is an AI-powered attendance management system that automates classroom attendance using Face Recognition and Voice Recognition technologies.

The platform enables teachers to create subjects, manage students, capture attendance, and track attendance records while providing students with a simple interface to join courses and view attendance statistics.

This project was built as an end-to-end AI application integrating Machine Learning concepts, database management, authentication, deployment, and modern web technologies.

---

## ✨ Features

### 👨‍🏫 Teacher Module

* Teacher Registration & Login
* Create and Manage Subjects
* Share Class Join Codes
* Upload Student Photos
* Face Recognition-Based Attendance
* Voice Recognition Integration
* Attendance Tracking Dashboard
* Attendance Analytics
* Student Management

### 👨‍🎓 Student Module

* Student Registration & Login
* Join Courses Using Subject Codes
* View Attendance Statistics
* Track Attendance History
* Unenroll from Subjects

### 🤖 AI Features

* Face Recognition Attendance System
* Voice Recognition Support
* Automated Student Identification
* Smart Attendance Logging

---

## 🏗️ System Architecture

Student / Teacher
↓
Frontend
↓
Streamlit UI
↓
Application Logic
↓
Supabase DB
↓
Attendance Records

---

## 🛠️ Tech Stack

### Programming

* Python

### Frontend

* Streamlit

### Backend

* Python
* Streamlit

### Database

* Supabase

### AI / Machine Learning

* Face Recognition
* Voice Recognition
* OpenCV
* NumPy

### Deployment

* Streamlit Community Cloud

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```bash
snapclass-ai-attendance-system/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── database/
│   ├── screens/
│   ├── components/
│   ├── services/
│   └── utils/
│
├── assets/
│
└── .streamlit/
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/snapclass-ai-attendance-system.git
```

### Move into Project

```bash
cd snapclass-ai-attendance-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

Create:

```bash
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_KEY"
```

---


---

## 🌟 Key Learnings

Through this project I learned:

* Building End-to-End AI Applications
* Face Recognition Integration
* Voice Recognition Workflows
* Database Design with Supabase
* Authentication Systems
* Streamlit Development
* Deployment on Streamlit Cloud
* Git & GitHub Workflow
* Debugging Real-World Applications
* Project Architecture and Modular Design

---

## 👨‍💻 Author

Praveena Pawar

Aspiring AI Engineer | Data Science Enthusiast | Machine Learning Developer

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
