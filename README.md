# People Insights Dashboard

A modern dashboard for tracking employee performance and sending automated performance updates.

## Features

- Employee performance tracking
- Automated email updates
- Modern, responsive UI
- Real-time metrics visualization

## Live Demo

Visit the live dashboard at: [https://aniruddha28715.github.io/people-insights/](https://aniruddha28715.github.io/people-insights/)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/aniruddha28715/people-insights.git
cd people-insights
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_verified_sender@yourdomain.com
SECRET_KEY=your_secret_key
```

4. Run the development server:
```bash
python app.py
```

5. Open http://localhost:5001 in your browser

## Deployment

The dashboard is automatically deployed to GitHub Pages when changes are pushed to the main branch.

## Technologies Used

- Flask
- SendGrid
- TailwindCSS
- JavaScript
- GitHub Actions

## 🌟 Features

- **Performance Tracking**
  - Real-time performance metrics
  - Visual progress indicators
  - Automated insights generation
  - Achievement tracking

- **Automated Communication**
  - Personalized email templates
  - Automated feedback distribution
  - Customizable recommendations

- **Modern Interface**
  - Responsive design
  - Interactive dashboards
  - Real-time updates
  - User-friendly metrics management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aniruddha28715/people-insights.git
cd people-insights
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file in the project root:
```env
EMAIL_FROM=your-email@company.com
EMAIL_USERNAME=your-email@company.com
EMAIL_PASSWORD=your-email-password
SMTP_SERVER=smtp.company.com
SMTP_PORT=587
SECRET_KEY=your-secret-key-here
```

4. Run the application:
```bash
python app.py
```

5. Access the dashboard at `http://localhost:5000`

## 🚀 Deployment

### GitHub Pages Deployment

1. Fork this repository to your GitHub account

2. Enable GitHub Pages in your repository settings:
   - Go to Settings > Pages
   - Select the `gh-pages` branch as the source
   - Click Save

3. Push your changes to the main branch:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/aniruddha28715/people-insights.git
git push -u origin main
```

4. The GitHub Action will automatically deploy your site to GitHub Pages
   - Your site will be available at `https://aniruddha28715.github.io/people-insights`

### Heroku Deployment

1. Install the Heroku CLI:
```bash
# For macOS
brew install heroku

# For Windows
# Download installer from https://devcenter.heroku.com/articles/heroku-cli
```

2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Set environment variables:
```bash
heroku config:set EMAIL_FROM=your-email@company.com
heroku config:set EMAIL_USERNAME=your-email@company.com
heroku config:set EMAIL_PASSWORD=your-email-password
heroku config:set SMTP_SERVER=smtp.company.com
heroku config:set SMTP_PORT=587
heroku config:set SECRET_KEY=your-secret-key-here
```

5. Deploy the application:
```bash
git push heroku main
```

### Docker Deployment

1. Build the Docker image:
```bash
docker build -t people-insights .
```

2. Run the container:
```bash
docker run -p 5000:5000 \
  -e EMAIL_FROM=your-email@company.com \
  -e EMAIL_USERNAME=your-email@company.com \
  -e EMAIL_PASSWORD=your-email-password \
  -e SMTP_SERVER=smtp.company.com \
  -e SMTP_PORT=587 \
  -e SECRET_KEY=your-secret-key-here \
  people-insights
```

### AWS Elastic Beanstalk Deployment

1. Install the EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB application:
```bash
eb init -p python-3.11 people-insights
```

3. Create environment:
```bash
eb create people-insights-env
```

4. Set environment variables:
```bash
eb setenv EMAIL_FROM=your-email@company.com \
  EMAIL_USERNAME=your-email@company.com \
  EMAIL_PASSWORD=your-email-password \
  SMTP_SERVER=smtp.company.com \
  SMTP_PORT=587 \
  SECRET_KEY=your-secret-key-here
```

5. Deploy:
```bash
eb deploy
```

## 🎯 Project Structure

```
people-insights/
├── app.py                 # Main Flask application
├── people_insights.py     # Core insights generation logic
├── employee_data.json     # Employee data storage
├── requirements.txt       # Project dependencies
├── Procfile              # Heroku deployment configuration
├── runtime.txt           # Python runtime specification
├── docs/                 # Static site for GitHub Pages
│   └── index.html        # Static dashboard
├── .github/              # GitHub configuration
│   └── workflows/        # GitHub Actions workflows
│       └── deploy.yml    # Deployment workflow
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Dashboard view
│   └── employee_details.html  # Employee details view
└── .env                  # Environment variables
```

## 💡 Key Components

### 1. Performance Metrics
- Productivity
- Teamwork
- Communication
- Achievement tracking

### 2. Insights Generation
```python
def generate_insights(self, employee, manager_name):
    """Generate personalized insights for an employee"""
    return self.email_template.render(
        employee=employee,
        manager_name=manager_name
    )
```

### 3. Email Automation
```python
def send_email(self, to_email, subject, content):
    """Send email using SMTP"""
    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv('EMAIL_FROM')
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))
        # ... email sending logic
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
```

## 🎯 Usage Guide

### Viewing Dashboard
1. Access the main dashboard at `/`
2. View all employees and their performance metrics
3. Click "View Details" for detailed information

### Managing Employee Data
1. Navigate to employee details page
2. Update performance metrics using the form
3. View and manage achievements
4. Preview generated insights

### Sending Insights
1. Preview insights for each employee
2. Click "Send Insights" to distribute feedback
3. Track sending status with notifications

## 🔧 Configuration

### Performance Thresholds
```python
# Default thresholds for recommendations
PRODUCTIVITY_THRESHOLD = 85
TEAMWORK_THRESHOLD = 85
COMMUNICATION_THRESHOLD = 85
```

### Email Templates
Customize email templates in `people_insights.py`:
```python
template_str = """
Dear {{ manager_name }},

Here are the latest insights for your team member {{ employee.name }}:
...
"""
```

## 📈 Benefits

### For Managers
- Streamlined performance tracking
- Automated feedback distribution
- Data-driven decision making
- Time-saving automation

### For Employees
- Clear performance metrics
- Regular feedback
- Achievement recognition
- Development recommendations

### For Organizations
- Standardized performance tracking
- Consistent communication
- Improved team management
- Data-driven insights

## 🔐 Security

- Environment variables for sensitive data
- Secure email configuration
- Input validation
- Error handling

## 🛠️ Development

### Adding New Features
1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Submit a pull request

### Running Tests
```bash
python -m pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📞 Support

For support, email support@example.com or create an issue in the repository.

## 🙏 Acknowledgments

- Flask framework
- Tailwind CSS
- Font Awesome icons
- Chart.js for visualizations

---

Made with ❤️ by [Aniruddha Kulkarni] 