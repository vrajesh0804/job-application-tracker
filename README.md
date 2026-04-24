# 💼 Job Application Tracker

A clean and modern Django-based web application to track your job applications efficiently.

Track roles, companies, HR contacts, application status, and manage your job hunt like a pro 🚀

---

## ✨ Features

- 📋 Add new job applications
- 📝 Edit existing applications
- ⚡ Quick status update (Approve / Reject)
- 📅 Group applications by date
- 📊 Daily application count
- 🎨 Clean, responsive UI (portfolio-style design)

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Styling:** Custom CSS (responsive)

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/your-username/job-application-tracker.git
cd job-application-tracker

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install django

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/
