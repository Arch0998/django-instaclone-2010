# 📸 Django InstaClone 2010

> **Nostalgic clone of early Instagram versions** - A social photo sharing network recreating the classic Instagram atmosphere from 2010-2012.

[![Django](https://img.shields.io/badge/Django-5.2.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

---

Live demo available for testing: [instaclone-1nla.onrender.com](https://instaclone-1nla.onrender.com/)

**Demo credentials:**  
---- Login: demo_user  
---- Pass: 3edc1qaz

> Desktop version works stably. Mobile app version is under development.

> Note: Some JavaScript features may work slowly or with delays on the free render.com hosting.

---

## 🌟 Features

### 📱 Core Social Features
- **📸 Photo Sharing** - Upload and share your moments with image validation
- **❤️ Advanced Like System** - Real-time likes with Ajax support and visual feedback
- **💬 Comment System** - Full commenting functionality with edit and delete options
- **#️⃣ Hashtag Support** - Automatic hashtag parsing and dedicated hashtag pages
- **👥 Following System** - Follow/unfollow users with real-time updates
- **🔍 Advanced Search** - Live user search with avatar previews
- **📊 Personalized Feed** - Timeline showing posts from followed users with pagination

### 👤 User Management & Profiles
- **🖼️ Custom Avatars** - Upload and manage profile pictures
- **📝 Profile Headers** - Customizable bio/header text (up to 50 characters)
- **📈 Social Statistics** - Real-time follower/following counts and post statistics
- **🔒 Profile Editing** - Full control over personal data including phone validation
- **👁️ Profile Views** - Browse other users' profiles with follow/unfollow functionality
- **📋 Followers/Following Lists** - Paginated lists with user avatars and quick actions

### 📸 Post Management
- **➕ Post Creation** - Upload photos with captions and automatic hashtag detection
- **✏️ Post Editing** - Edit post captions and images (authors only)
- **🗑️ Post Deletion** - Delete posts with confirmation (authors only)
- **🔍 Post Details** - Dedicated post pages with full comment threads
- **📅 Timestamps** - Human-readable timestamps (e.g., "2 hours ago")
- **🏷️ Hashtag Pages** - Browse all posts by specific hashtags with grid layout
- **📷 Image Update** - Change post image during editing

### 💬 Advanced Comment System
- **💭 Real-time Comments** - Add comments to posts instantly
- **✏️ Comment Editing** - Edit your own comments
- **🗑️ Comment Deletion** - Delete comments with proper permissions
- **👤 Comment Authors** - Display comment authors with profile links
- **📅 Comment Timestamps** - Show when comments were made

### 🎨 Modern UI/UX Design
- **🕰️ Retro Instagram Aesthetic** - Faithful recreation of 2010-era Instagram design
- **✨ Interactive Elements** - Hover effects, smooth transitions, and visual feedback
- **🌈 Gradient Design** - Instagram-style gradients and modern color schemes
- **📋 Smart Navigation** - Sticky header with quick access to all features
- **🔄 Ajax Interactions** - Real-time likes, follows, and search without page reloads

### 🔒 Security & Authentication
- **🔐 Custom User Model** - Extended user model with phone validation
- **📧 Secure Registration** - Email and phone number validation
- **🛡️ Permission System** - Proper authorization for post/comment editing
- **🚫 Access Control** - Login required for most features
- **✅ Form Validation** - Client and server-side validation

### 📊 Data Management
- **📈 Pagination** - Efficient pagination for feeds, profiles, and lists
- **🗄️ Optimized Queries** - Database optimization with select_related and prefetch_related
- **📱 Media Handling** - Organized media uploads with date-based directory structure
- **🏷️ Automatic Tagging** - Regex-based hashtag extraction and management
- **📸 Cloudinary Integration** - All images stored and served via Cloudinary
- **💾 Environment Switching** - Use `.env` to switch between dev (SQLite) and prod (PostgreSQL) via `DJANGO_SETTINGS_MODULE`

---

## 🛠️ Technical Stack

### Backend
- **Django 5.2.5** - Modern Python web framework
- **SQLite** - Lightweight database for development
- **Pillow** - Image processing and handling
- **Python 3.12+** - Latest Python features

### Frontend
- **Bootstrap 5.3** - Responsive CSS framework
- **FontAwesome 6.4** - Modern icon library
- **Vanilla JavaScript** - Custom interactions and Ajax
- **CSS3** - Modern styling with gradients and animations

### Architecture
- **Class-Based Views** - Django CBVs for clean, reusable code
- **Model-View-Template** - Standard Django architecture
- **Ajax Integration** - Seamless real-time interactions
- **Signal System** - Automatic profile creation on user registration

---

## 📁 Project Structure

```
📁 django-instaclone-2010/                # Main project root
├── 📝 manage.py                          # Django management script
├── 📁 django_instaclone_2010/            # Django core package (settings, URLs, WSGI/ASGI)
│   ├── asgi.py                           # ASGI config
│   ├── urls.py                           # Main URL routing
│   └── wsgi.py                           # WSGI config
├── 📁 accounts/                          # User management app
│   ├── models.py                         # User, UserProfile, Follow models
│   ├── views.py                          # Profile, authentication, follow views
│   ├── forms.py                          # Registration and profile forms
│   ├── validators.py                     # Custom username validation
│   ├── signals.py                        # Auto profile creation
│   └── 📁 migrations/                    # Database migrations
├── 📁 posts/                             # Posts and content app
│   ├── models.py                         # Post, Comment, PostLike, Hashtag models
│   ├── views.py                          # CRUD operations for posts and comments
│   └── 📁 migrations/                    # Database migrations
├── 📁 settings/                          # Django settings (base, dev, prod, testing)
│   ├── base.py                           # Base settings
│   ├── dev.py                            # Development settings
│   ├── prod.py                           # Production settings
├── 📁 static/                            # Static assets (CSS/JS)
│   ├── 📁 css/                           # Stylesheets for each component
│   └── 📁 js/                            # JavaScript for interactivity
├── 📁 staticfiles/                       # Collected static files (for production)
├── 📁 templates/                         # Django templates
│   ├── base.html                         # Base template with navigation
│   ├── pagination.html                   # Pagination partial
│   ├── 📁 accounts/                      # User-related templates
│   └── 📁 posts/                         # Post-related templates
├── 📁 media/                             # User uploads (avatars, posts)
├── 📝 README.md                          # Project documentation
├── 📝 requirements.txt                   # Python dependencies
└── 🛠️ build.sh                           # Build/deploy script
```

---

## 🚀 Key Features Breakdown

### 🔄 Real-time Interactions
- **Like Button**: Ajax-powered likes with instant visual feedback
- **Follow System**: Real-time follow/unfollow with counter updates
- **Live Search**: Instant user search results with debouncing
- **Comment Management**: Add, edit, delete comments without page refresh

### 🔍 Advanced Search & Discovery
- **User Search**: Find users by username or name with live results
- **Hashtag Discovery**: Browse posts by hashtags with grid view
- **Profile Discovery**: Explore user profiles and their content
- **Follow Suggestions**: See who users are following/followed by

### 📊 Analytics & Statistics
- **Post Counts**: Track how many posts each user has shared
- **Social Metrics**: Real-time follower and following counts
- **Engagement Stats**: Like and comment counts on posts
- **Activity Timestamps**: Track when content was created and updated

---

## 🎯 Instagram 2010 Authenticity

This project faithfully recreates the early Instagram experience:

- **🎨 Visual Design**: Retro gradients, card-based layouts, and classic Instagram aesthetics
- **📸 Photo-Centric**: Images are the primary content with simple, clean presentation
- **👥 Social Core**: Focus on following friends and discovering content through social connections
- **🏷️ Hashtag Culture**: Simple hashtag system for content organization
- **💬 Minimal Comments**: Clean, simple commenting system without threading

---

## 🔧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-instaclone-2010
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root directory and add the following variables:
   
   ```env
   # Django Configuration
   DJANGO_SECRET_KEY=your-secret-key-here
   DJANGO_SETTINGS_MODULE=settings.dev
   
   # Cloudinary Configuration (for image hosting)
   CLOUDINARY_CLOUD_NAME=your-cloudinary-cloud-name
   CLOUDINARY_API_KEY=your-cloudinary-api-key
   CLOUDINARY_API_SECRET=your-cloudinary-api-secret
   ```
   
   **🔑 How to get these values:**


   **Django Secret Key:**
   - Generate a new secret key using Django's built-in function:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   - Or use online generator: https://djecrety.ir/


   **Cloudinary Credentials:**
   - Sign up for free account at: https://cloudinary.com/
   - Go to Dashboard → Account Details
   - Copy Cloud Name, API Key, and API Secret
   - Cloudinary provides free tier with 25GB storage and 25GB bandwidth

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python manage.py runserver
   ```


### ⚠️ Important Notes

- **Never commit your `.env` file** - Add it to `.gitignore`
- **Keep your secret keys secure** - Don't share them publicly
- **Regenerate keys** if they get compromised
- **Use different keys** for development and production environments

---

## 📱 Usage Guide

### 🏠 Getting Started
1. **Register**: Create account with username, email, and phone
2. **Complete Profile**: Add avatar and bio header
3. **Find Friends**: Use search to find and follow other users
4. **Share Content**: Upload your first photo with caption and hashtags

### 📸 Posting Content
- **Upload Photo**: Choose image file (required)
- **Add Caption**: Write description with hashtags (#hashtag)
- **Auto-Tagging**: Hashtags are automatically detected and linked
- **Edit Later**: Modify captions anytime from post detail page

### 👥 Social Features
- **Follow Users**: Click follow button on profiles or search results
- **Explore Feed**: See posts from people you follow in chronological order
- **Interact**: Like posts and leave comments
- **Discover**: Browse hashtag pages to find new content

---

## 🎨 Design Philosophy

This project embodies the simplicity and focus that made early Instagram special:

- **📸 Photography First**: Clean, uncluttered interface that highlights photos
- **👥 Social Connection**: Easy discovery and interaction with other users
- **🎯 Focused Features**: Core functionality without overwhelming complexity
- **🕰️ Nostalgic Feel**: Warm gradients and classic design patterns

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Follow Django best practices
4. Add tests for new features
5. Submit a pull request

---

## 📝 License

This project is for educational purposes, recreating the early Instagram experience for learning Django development.

---

## 🙏 Acknowledgments

- **Instagram**: For the original inspiration and design patterns
- **Django Community**: For the excellent web framework
- **Bootstrap Team**: For the responsive CSS framework

---

*Built with ❤️ and nostalgia for the golden age of social media*
