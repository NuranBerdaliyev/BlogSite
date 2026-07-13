# Multi-User Blog Platform

A Django-based web application for blogging where multiple users can register, create accounts, publish articles, and read or comment on posts written by other authors.

---

## 🚀 Key Features

* **User Management:** Secure user registration, login/logout system, and custom user profiles.
* **Content Management:** Full CRUD capabilities (Create, Read, Update, Delete) for blog posts.
* **Categorization:** Grouping articles by categories and tags for smooth navigation and filtering.
* **Interactivity:** A built-in comment section under each article for reader engagement.
* **Role-Based Permissions:** Restricting post edits and deletions strictly to the post's author or site administrators.

---

## 🛠 Tech Stack

* **Language:** Python 3.12
* **Framework:** Django 6.0.7
* **Database:** SQLite (default for local development) / PostgreSQL
* **Frontend styling:** HTML5, CSS3, Bootstrap or Tailwind CSS

---

## 📦 Local Installation Guide

Follow these steps to set up and run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com/NuranBerdaliyev/BlogSite
```

### 2. Set Up a Virtual Environment
Create and activate an isolated virtual environment:

* **Windows:**
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
* **macOS/Linux:**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```
*(If you do not have a requirements.txt file yet, manually run `pip install django`)*

### 4. Apply Database Migrations
Create the necessary database tables and schema:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
Generate an administrative account to access the Django admin panel:
```bash
python manage.py createsuperuser
```

### 6. Start the Development Server
Launch the local server:
```bash
python manage.py runserver
```

Open your browser and navigate to:  
* Main application: http://127.0.0/  
* Admin Dashboard: http://127.0.0/admin/
---

## 📂 Project Structure Overview
* `blog_app/` — The core application containing post and comment models, views, and business logic.
* `users/` — Custom application managing user registration, logins, and profile data.
* `templates/` — Global HTML files used to structure the layout of the website.
