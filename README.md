# Study Time Tracker

A comprehensive web application built with Django and modern CSS to help students track their study time across different subjects and chapters.

## 🌟 Features

### Core Functionality
- **User Authentication**: Secure login and registration system
- **Subject Management**: Create and organize study subjects
- **Chapter Tracking**: Add chapters to each subject for detailed organization
- **Study Sessions**: Interactive timer to track study sessions
- **Notes System**: Add and save notes for each chapter

### Analytics & Insights
- **Study Time Analytics**: Visual dashboard with total study time statistics
- **Subject-wise Breakdown**: See time distribution across different subjects
- **Progress Tracking**: Monitor your study habits and patterns
- **Interactive Charts**: Beautiful visualizations using Chart.js

### User Experience
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Modern UI**: Clean, gradient-based design with smooth animations
- **Intuitive Navigation**: Easy-to-use interface with clear navigation
- **Real-time Updates**: Live timer and instant save functionality

## 🚀 Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern gradients and animations
- **Charts**: Chart.js for data visualization
- **Icons**: Emoji-based icons for visual appeal
- **Fonts**: Poppins font family from Google Fonts

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd study-time-tracker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to `http://localhost:8000`

## 🎯 Usage Guide

### Getting Started
1. **Register an account** or login if you already have one
2. **Add subjects** for the topics you want to study
3. **Create chapters** within each subject for detailed tracking
4. **Start study sessions** using the interactive timer
5. **Add notes** to chapters for future reference

### Key Pages
- **Dashboard**: Overview of your subjects and study analytics
- **Study Session**: Interactive timer with subject/chapter selection
- **Add Subject**: Form to create new study subjects
- **Add Chapter**: Form to add chapters to existing subjects
- **Login/Register**: Authentication pages

## 📊 Database Models

### Subject
- `name`: Name of the subject
- `user`: ForeignKey to User model
- `total_time`: Total minutes studied for this subject

### Chapter
- `subject`: ForeignKey to Subject model
- `name`: Name of the chapter
- `time_studied`: Minutes spent on this chapter
- `notes`: Text field for chapter notes

## 🎨 Design Features

- **Color Scheme**: Gradient backgrounds (#667eea to #764ba2) with accent colors (#ff6b6b)
- **Typography**: Poppins font family for modern, clean readability
- **Components**: Card-based design with subtle shadows and hover effects
- **Animations**: Smooth transitions and fade-in effects
- **Responsive**: Mobile-first design that works on all screen sizes

## 🔧 Customization

### Adding New Features
1. Create new models in `models.py`
2. Add views in `views.py`
3. Create templates in `templates/studyapp/`
4. Update URLs in `urls.py`
5. Add static files in `static/studyapp/`

### Modifying Styles
- Main CSS file: `static/studyapp/css/style.css`
- Color scheme can be modified by changing CSS custom properties
- Component styles are organized by section in the CSS

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Django framework for robust backend functionality
- Chart.js for beautiful data visualizations
- Google Fonts for the Poppins typeface
- Modern CSS techniques for responsive design

## 📞 Support

If you have any questions or need help with the application, please:
1. Check the documentation above
2. Review the code comments
3. Create an issue in the GitHub repository

---

**Happy Studying!** 📚⏱️
