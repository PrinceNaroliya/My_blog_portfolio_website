# Flask Portfolio & Blog Website 🌌

Welcome to my **personal portfolio and blog website**! This project showcases my skills, projects, achievements, and blog posts in a clean, modern, and professional design with a **space-inspired black & white theme**.

---

## 🌐 Live Demo

You can view the live website here:

https://princenaroliya.onrender.com/

---

## 🚀 Features

- **Portfolio Section:**  
  Highlights my projects, skills, and achievements. Includes interactive cards for a modern look.

- **Blog Section:**  
  A dedicated section to share my journey, learning, and projects. Fully responsive and easy to navigate.

- **Space + Black & White Theme:**  
  Unique and visually appealing dark-themed interface with a minimalistic style inspired by space.

- **Skills Section:**  
  Interactive skill cards with icons for Python, Flask, HTML, CSS, Scikit-Learn, Git, GitHub, and more.

- **Experience & Achievements:**  
  Showcase of my professional experience, internships, contributions, and personal milestones.

- **Hobbies Section:**  
  Highlights personal interests like coding challenges, learning AI/ML, reading tech blogs, and gaming in an attractive card layout.

---

## 🛠 Technologies Used

- **Frontend:** HTML5, CSS3, Bootstrap (optional), Jinja2 Templates  
- **Backend:** Flask  
- **Database:** SQLite / SQLAlchemy  
- **Server:** Waitress / Gunicorn (for deployment)  
- **Icons & Images:** skillicons.dev & static assets  

---

## ⚙️ Installation

Follow these steps to run the project locally:

1. Clone the repository

```
git clone https://github.com/yourusername/yourrepo.git
```

2. Navigate to the project folder

```
cd yourrepo
```

3. Create a virtual environment

```
python -m venv venv
```

4. Activate the virtual environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

5. Install dependencies

```
pip install -r requirements.txt
```

6. Run the Flask application

```
python run.py
```

7. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 📁 Project Structure

```
my-flask-website/
│
├── static/          # CSS, JS, Images
├── templates/       # HTML templates
├── run.py           # Main Flask file
├── requirements.txt # Python dependencies
├── Procfile         # For deployment (Render/Heroku)
└── README.md        # This file
```

---

## ⚡ Deployment

This website is ready to deploy on **Render, Heroku, or PythonAnywhere**.

### Render Recommended (Free Tier)

1. Connect your GitHub repo to Render.  
2. Set up the web service with Python runtime.  
3. Procfile command:

```
web: waitress-serve --threads=8 --host=0.0.0.0 --port=$PORT run:app
```

4. Render will automatically build and deploy your app.  
5. Future updates? Just `git push` and Render auto-deploys.

---

## 🌟 Screenshots

![Portfolio Screenshot](static/images/screenshot-portfolio.png)  
![Blog Screenshot](static/images/screenshot-blog.png)

---

## 💡 Future Plans

- Add **user authentication** for blog posts.  
- Integrate **contact form & email notifications**.  
- Enhance the **space theme with animations** and dark-mode toggling.  
- Add more **interactive project showcases** and charts for skills.

---

## 📫 Contact

- **Email:** your.email@example.com  
- **GitHub:** https://github.com/yourusername  
- **LinkedIn:** https://linkedin.com/in/yourprofile  

---

> Made with ❤️ by Prince Naroliya
