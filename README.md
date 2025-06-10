# People Insights Dashboard

A comprehensive employee performance management system built with Flask that helps track, analyze, and improve employee performance through metrics, achievements, and automated insights.

## 🌟 Features

### Employee Management
- **Employee Registration**: Easy onboarding process for new employees
- **Performance Metrics**: Track three key metrics:
  - Productivity
  - Teamwork
  - Communication
- **Achievement Tracking**: 
  - Add and manage employee achievements
  - View achievement history
  - Real-time achievement updates

### Performance Analysis
- **Automated Performance Verdicts**: Based on performance metrics:
  - Outstanding Performance (≥90% in all metrics)
  - Good Performance (≥75% in all metrics)
  - Average Performance (≥50% in all metrics)
  - Needs Improvement (<50% in any metric)
- **Detailed Performance Analysis**: Automated insights based on metrics
- **Visual Performance Indicators**: Color-coded performance status

### Admin Features
- **Admin Dashboard**: Centralized view of all employees
- **Performance Review**: Easy access to employee details and metrics
- **Notification System**: Track new employee registrations
- **Metrics Management**: Update and manage performance metrics

### Communication
- **Automated Insights**: Generate and send performance insights
- **Email Notifications**: Send performance updates to employees
- **Terminal-based Email Preview**: View email content before sending

## 📸 Screenshots Needed
1. **Dashboard View**
   - Main dashboard showing employee cards
   - Performance metrics visualization
   - Recent achievements preview

2. **Employee Details**
   - Individual employee performance page
   - Performance metrics update form
   - Achievement management section
   - Performance analysis display

3. **Admin Panel**
   - Admin dashboard overview
   - New employee notifications
   - Performance review interface

4. **Registration Process**
   - New employee registration form
   - Success confirmation

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aniruddha28715/people-insights.git
cd people-insights
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5001`

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, TailwindCSS
- **Data Storage**: JSON
- **Email**: Terminal-based preview system
- **Containerization**: Docker

## 📝 Recent Updates

### Employee Achievement System
- Added ability to add new achievements for employees
- Achievement management in employee details page
- Achievement preview on dashboard cards

### Admin Panel Improvements
- Added notification system for new employees
- Improved performance review interface
- Automated performance verdicts

### Performance Analysis
- Implemented automated performance analysis
- Added color-coded performance indicators
- Enhanced metrics visualization

### Email System
- Implemented terminal-based email preview
- Added performance insights email template
- Improved email content formatting

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Aniruddha Kulkarni** - *Initial work* - [aniruddha28715](https://github.com/aniruddha28715)

## 🙏 Acknowledgments

- Flask documentation
- TailwindCSS for the beautiful UI
- All contributors who have helped improve this project 