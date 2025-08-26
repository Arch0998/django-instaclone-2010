# 📸 Django InstaClone 2010

> **Nostalgic clone of early Instagram versions** - A social photo sharing network recreating the classic Instagram atmosphere from 2010-2012.

[![Django](https://img.shields.io/badge/Django-5.2.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-4-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

---

## 🌟 Features

### 📱 Core Functionality
- **📸 Photo Sharing** - Upload and share your moments
- **❤️ Likes & Comments** - Interact with other users' content
- **#️⃣ Hashtags** - Organize content by topics
- **👥 Following System** - Follow your favorite users
- **🔍 Search** - Find users and content
- **📊 News Feed** - Personalized feed of posts from followed users

### 👤 User Profiles
- **🖼️ Avatars** - Personalize your profile
- **📝 Biography** - Tell your story
- **📈 Statistics** - Posts, followers, and following counts
- **🔒 Profile Editing** - Full control over personal data

### 🎨 Instagram 2010 Style Design
- **🕰️ Retro Atmosphere** - Recreates the spirit of early Instagram
- **📱 Responsive Design** - Works on all devices
- **🎯 Clean Interface** - Minimalist and intuitive
- **⚡ Fast Navigation** - User-friendly structure

---

## 🛠️ Technologies

### Backend
- **Django 5.2.5** - Main web framework
- **SQLite** - Database (easily replaceable with PostgreSQL/MySQL)
- **Pillow** - Image processing
- **Cloudinary** - Media file storage

### Frontend
- **Bootstrap 4** - Responsive CSS framework
- **Crispy Forms** - Django form styling
- **Vanilla JavaScript** - Interactivity
- **Custom CSS** - Unique design

---

## 🚀 Quick Start

### Requirements
- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**
```
git clone https://github.com/yourusername/django-instaclone-2010.git
cd django-instaclone-2010
```

2. **Create virtual environment**
```
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Setup database**
```
python manage.py migrate
```

5. **Create superuser**
```
python manage.py createsuperuser
```

6. **Run the server**
```
python manage.py runserver
```

7. **Open your browser** and go to `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
django-instaclone-2010/
├── 🏠 manage.py                    # Django management script
├── 📦 requirements.txt             # Python dependencies
├── 🗃️ db.sqlite3                   # SQLite database
├── 
├── 👥 accounts/                    # User application
│   ├── models.py                   # User, UserProfile, Follow models
│   ├── views.py                    # Profile and authentication views
│   ├── forms.py                    # Registration and editing forms
│   └── validators.py               # User validators
├── 
├── 📸 posts/                       # Posts application
│   ├── models.py                   # Post, Comment, Hashtag, PostLike models
│   ├── views.py                    # Post and feed views
│   └── admin.py                    # Admin panel configuration
├── 
├── 🏗️ django_instaclone_2010/     # Main project directory
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # URL configuration
│   └── wsgi.py                     # WSGI configuration
├── 
├── 🎨 static/                      # Static files
│   └── css/                        # CSS styles
│       ├── base.css                # Base styles
│       ├── feed.css                # Feed styles
│       ├── profile.css             # Profile styles
│       └── ...                     # Other styles
├── 
└── 📄 templates/                   # HTML templates
    ├── base.html                   # Base template
    ├── accounts/                   # User templates
    └── posts/                      # Post templates
```

---

## 🎯 Main Features

### 📸 Posts
- ✅ Photo upload with captions
- ✅ Automatic hashtag recognition
- ✅ Likes and comments
- ✅ Post editing and deletion
- ✅ Feed pagination

### 👥 Social Features
- ✅ User following system
- ✅ News feed from followed users
- ✅ User search
- ✅ Profile viewing
- ✅ Followers and following lists

### #️⃣ Hashtags
- ✅ Automatic hashtag creation
- ✅ Hashtag pages with posts
- ✅ Post pagination by hashtags

### 🔐 Authentication
- ✅ New user registration
- ✅ Login/logout system
- ✅ Profile editing
- ✅ Avatar uploads

---

## 🖼️ Screenshots

### 🏠 Home Page
*News feed with posts from followed users*

### 👤 User Profile
*Post grid, statistics, follow buttons*

### 📱 Responsive Design
*Optimized for mobile devices*

---

## ⚙️ Configuration

### 🌐 Production Setup

1. **Update settings in `settings.py`**
```python
DEBUG = True
ALLOWED_HOSTS = []
```

2. **Cloudinary setup for media files**
```python
import cloudinary
cloudinary.config(
    cloud_name='your_cloud_name',
    api_key='your_api_key',
    api_secret='your_api_secret'
)
```

---

## 🤝 Contributing

We welcome any contributions! How you can help:

1. 🐛 **Report bugs** through Issues
2. 💡 **Suggest new features**
3. 🔧 **Submit Pull Requests**
4. 📖 **Improve documentation**

### Contributing Process:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Arthur**
- GitHub: [@arch0998](https://github.com/arch0998)

---

## 🔄 Versions

### v1.0.0 (Current)
- ✅ Basic post functionality
- ✅ User system
- ✅ Following and feed
- ✅ Hashtags
- ✅ Responsive design

---

<div align="center">
  
**⭐ Star this project if you like it! ⭐**

*Made with ❤️ and nostalgia for the old Instagram*

</div>
