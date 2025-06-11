---
layout: default
title: People Insights Dashboard
---

# People Insights Dashboard

A comprehensive employee performance management system built with Flask that helps track, analyze, and improve employee performance through metrics, achievements, and automated insights.

## 🌟 Features

### Employee Management

* **Employee Registration**: Easy onboarding process for new employees
* **Performance Metrics**: Track three key metrics:  
   * Productivity  
   * Teamwork  
   * Communication
* **Achievement Tracking**:  
   * Add and manage employee achievements  
   * View achievement history  
   * Real-time achievement updates

### Performance Analysis

* **Automated Performance Verdicts**: Based on performance metrics:  
   * Outstanding Performance (≥90% in all metrics)  
   * Good Performance (≥75% in all metrics)  
   * Average Performance (≥50% in all metrics)  
   * Needs Improvement (<50% in any metric)
* **Detailed Performance Analysis**: Automated insights based on metrics
* **Visual Performance Indicators**: Color-coded performance status

### Admin Features

* **Admin Dashboard**: Centralized view of all employees
* **Performance Review**: Easy access to employee details and metrics
* **Notification System**: Track new employee registrations
* **Metrics Management**: Update and manage performance metrics

### Communication

* **Automated Insights**: Generate and send performance insights
* **Email Notifications**: Send performance updates to employees
* **Terminal-based Email Preview**: View email content before sending

## 📸 Screenshots

### Dashboard View
![Dashboard View](https://github.com/aniruddha28715/people-insights/raw/main/docs/screenshots/Dashboard%20View.png)
The main dashboard provides a comprehensive overview of all employees, their performance metrics, and recent achievements. Each employee card displays key performance indicators and a quick summary of their recent accomplishments.

### Employee Dashboard Card
![Employee Dashboard Card](https://github.com/aniruddha28715/people-insights/raw/main/docs/screenshots/Employee%20Dashboard%20Card.png)
Individual employee cards show:
- Performance metrics (Productivity, Teamwork, Communication)
- Recent achievements
- Performance status indicators
- Quick access to detailed view

### Employee Details
![Employee Details](https://github.com/aniruddha28715/people-insights/raw/main/docs/screenshots/Employee%20Details.png)
The detailed employee view includes:
- Complete performance metrics
- Achievement management system
- Performance analysis and trends
- Detailed achievement history
- Performance update form

### Admin Panel
![Admin Panel](https://github.com/aniruddha28715/people-insights/raw/main/docs/screenshots/Admin%20panel.png)
The admin interface provides:
- Complete employee list
- Performance review tools
- Notification system
- Performance analytics
- Employee management controls

### Registration Process
![Register Process](https://github.com/aniruddha28715/people-insights/raw/main/docs/screenshots/Register%20Process.png)
The employee registration system includes:
- New employee registration form
- Automated performance assessment
- Initial achievement tracking
- Welcome notification system

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip (Python package manager)
* Git

### Installation

1. Clone the repository:  
```  
git clone https://github.com/aniruddha28715/people-insights.git  
cd people-insights  
```
2. Create and activate virtual environment:  
```  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```
3. Install dependencies:  
```  
pip install -r requirements.txt  
```
4. Run the application:  
```  
python app.py  
```

The application will be available at `http://127.0.0.1:5001`

## 🛠️ Technology Stack

* **Backend**: Flask (Python)
* **Frontend**: HTML, TailwindCSS
* **Data Storage**: JSON
* **Email**: Terminal-based preview system
* **Containerization**: Docker

## 📝 Recent Updates

### Employee Achievement System

* Added ability to add new achievements for employees
* Achievement management in employee details page
* Achievement preview on dashboard cards

### Admin Panel Improvements

* Added notification system for new employees
* Improved performance review interface
* Automated performance verdicts

### Performance Analysis

* Implemented automated performance analysis
* Added color-coded performance indicators
* Enhanced metrics visualization

### Email System

* Implemented terminal-based email preview
* Added performance insights email template
* Improved email content formatting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

* **Aniruddha Kulkarni** \- _Initial work_ \- aniruddha28715

## 🙏 Acknowledgments

* Flask documentation
* TailwindCSS for the beautiful UI
* All contributors who have helped improve this project 