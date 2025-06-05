# People Insights Dashboard

A comprehensive, interactive dashboard designed to streamline employee performance tracking and facilitate effective performance communication. This tool helps managers and HR professionals monitor, evaluate, and communicate employee performance metrics in a user-friendly interface.

## 🌟 Key Features

### 📊 Employee Performance Tracking
- **Comprehensive Metrics**
  - Productivity score (0-100)
  - Teamwork effectiveness rating
  - Communication skills assessment
  - Visual progress bars for quick insights
  - Color-coded performance indicators

- **Achievement Management**
  - Track recent accomplishments
  - Add new achievements with timestamps
  - Remove outdated achievements
  - Achievement history tracking

### 🔄 Interactive Employee Management
- **Real-time Updates**
  - Instant performance metric updates
  - Live achievement tracking
  - Dynamic UI updates
  - No page refresh required

- **Detailed Employee Profiles**
  - Personal information management
  - Role and department tracking
  - Performance history
  - Achievement timeline

### 📧 Performance Communication
- **Email Integration**
  - Pre-formatted performance templates
  - Customizable email content
  - Performance summary inclusion
  - Achievement highlights

- **Communication Tools**
  - Email preview functionality
  - Performance report generation
  - Custom message composition
  - Template management

## 🚀 Live Demo

Experience the dashboard in action: [https://aniruddha28715.github.io/people-insights/](https://aniruddha28715.github.io/people-insights/)

## 💻 Local Development Setup

### Prerequisites
- Python 3.x
- Git
- Modern web browser (Chrome, Firefox, Safari, or Edge)

### Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/aniruddha28715/people-insights.git
cd people-insights
```

2. **Start Local Server**
```bash
cd docs
python3 -m http.server 8000
```

3. **Access the Dashboard**
Open your browser and navigate to:
```
http://localhost:8000
```

## 📖 Detailed Usage Guide

### Viewing Employee Performance

Here's a look at the main dashboard displaying all employee cards:

![Main Dashboard View](docs/screenshots/main-dashboard.png)

- **Employee Cards Display**
  - Employee name and role
  - Current performance metrics
  - Visual progress indicators
  - Recent achievements list
  - Quick action buttons

- **Performance Metrics**
  - Color-coded progress bars
  - Numerical scores
  - Trend indicators
  - Achievement badges

Detail view of employee performance metrics:

![Employee Performance Metrics Detail](docs/screenshots/performance-metrics.png)

### Managing Employee Information

Here's the modal for editing employee details:

![Edit Employee Details Modal](docs/screenshots/edit-details-modal.png)

1. **Access Edit Mode**
   - Click "Edit Details" on employee card
   - View current information
   - Access edit form

2. **Update Information**
   - Modify basic details:
     - Name
     - Email address
     - Role/Position
   - Adjust performance metrics:
     - Productivity score
     - Teamwork rating
     - Communication score
   - Manage achievements:
     - Add new achievements
     - Remove existing ones
     - Update achievement dates

3. **Save Changes**
   - Review modifications
   - Confirm updates
   - View real-time changes

### Sending Performance Emails

This is the modal for composing and sending performance emails:

![Send Performance Email Modal](docs/screenshots/edit-email-modal.png)

1. **Initiate Email Process**
   - Click "Send Email" button
   - Access email template

2. **Customize Content**
   - Edit email subject
   - Modify email body
   - Include performance metrics
   - Add achievement highlights

3. **Send Communication**
   - Preview email content
   - Confirm recipient
   - Send performance update

## 🛠️ Technology Stack

- **Frontend Technologies**
  - HTML5 for structure
  - TailwindCSS for responsive design
  - JavaScript for interactivity
  - Font Awesome for icons

- **Development Tools**
  - Git for version control
  - Python for local server
  - Modern web browsers for testing

## 📁 Project Structure

```
people-insights/
├── docs/                 # Static site files
│   ├── index.html       # Main dashboard interface
│   ├── js/              # JavaScript functionality
│   │   └── dashboard.js # Core dashboard logic
│   └── .nojekyll        # GitHub Pages configuration
└── README.md            # Project documentation
```

## 🤝 Contributing

We welcome contributions to improve the People Insights Dashboard! Here's how you can help:

1. **Fork the Repository**
   - Create your copy of the project
   - Set up development environment

2. **Create Feature Branch**
   - Make a new branch for your changes
   - Follow naming conventions

3. **Make Changes**
   - Implement new features
   - Fix existing issues
   - Update documentation

4. **Submit Changes**
   - Commit your modifications
   - Push to your branch
   - Create pull request

5. **Code Review**
   - Address feedback
   - Make necessary adjustments
   - Get approval for merge

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Made with ❤️ by [Aniruddha Kulkarni]

---

For support or questions, please open an issue in the repository. 