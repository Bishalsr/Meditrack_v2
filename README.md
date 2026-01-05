# MediTrack_v2

MediTrack_v2 is a **Django-based healthcare management web application** designed to manage doctors, hospital data, and medical-related information in a simple and organized way.

This project is suitable for academic projects, learning Django, and small clinic or hospital management systems.

---

## 🚀 Features

✔ Manage hospital and doctor information  
✔ Upload and store doctor images  
✔ Django admin panel for data management  
✔ Simple and clean project structure  
✔ SQLite database for quick setup  

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|------|
| Python | Backend logic |
| Django | Web framework |
| SQLite | Database |
| HTML, CSS | Frontend templates |
| Media files | Doctor images |

---

## 📥 Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/Bishalsr/Medittrack_v2.git
cd Meditrack_v2

2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

3. Install required packages
pip install -r requirements.txt

4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

5. Create admin user (optional)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver


Open browser and go to:
http://127.0.0.1:8000/

📁 Project Structure
Meditrack_v2/
├── hospital/                 # Hospital app
├── meditrack/                # Core project files
├── media/doctor_images/      # Uploaded doctor images
├── db.sqlite3                # Database
├── manage.py                 # Django CLI
├── requirements.txt          # Dependencies

🧠 Usage

• Login to admin panel: http://127.0.0.1:8000/admin/
• Add hospitals, doctors and manage uploaded images
• Extend the project to include patients, appointments, billing, etc.

🔮 Future Improvements

✔ Patient records module
✔ Appointment booking system
✔ Payment and billing system
✔ REST API support
✔ PostgreSQL database support

🤝 Contributing

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes

Push to your branch

Create a Pull Request

📜 License

This project is for educational purposes and open for learning and development.

📫 Contact

Project maintained by Bishal Sr
GitHub: https://github.com/Bishalsr
