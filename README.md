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

## Screenshots

### Dashboard View
![Dashboard View](./docs/screenshots/Dashboard%20View.png)
The main dashboard provides a comprehensive overview of all employees, their performance metrics, and recent achievements. Each employee card displays key performance indicators and a quick summary of their recent accomplishments.

### Employee Dashboard Card
![Employee Dashboard Card](./docs/screenshots/Employee%20Dashboard%20Card.png)
Individual employee cards show:
- Performance metrics (Productivity, Teamwork, Communication)
- Recent achievements
- Performance status indicators
- Quick access to detailed view

### Employee Details
![Employee Details](./docs/screenshots/Employee%20Details.png)
The detailed employee view includes:
- Complete performance metrics
- Achievement management system
- Performance analysis and trends
- Detailed achievement history
- Performance update form

### Admin Panel
![Admin Panel](./docs/screenshots/Admin%20panel.png)
The admin interface provides:
- Complete employee list
- Performance review tools
- Notification system
- Performance analytics
- Employee management controls

### Registration Process
![Register Process](./docs/screenshots/Register%20Process.png)
The employee registration system includes:
- New employee registration form
- Automated performance assessment
- Initial achievement tracking
- Welcome notification system

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

## 🛠️ Technical Architecture

### Backend Framework
- **Flask (v2.0.1)**: Lightweight Python web framework
  - Handles routing and request processing
  - Manages application state
  - Provides template rendering engine
  - Implements RESTful API endpoints

### Frontend Technologies
- **HTML5**: Structure and content
- **TailwindCSS**: Utility-first CSS framework for responsive design
- **Jinja2 (v3.1.2)**: Template engine for dynamic HTML generation
  - Template inheritance
  - Dynamic content rendering
  - Control structures and filters

### Data Management
- **JSON**: Data storage format
  - Employee information
  - Performance metrics
  - Achievement records
- **Pandas (v2.1.0)**: Data manipulation and analysis
  - Performance data processing
  - Metrics calculations
  - Data transformation

### Security & Configuration
- **python-dotenv (v0.19.0)**: Environment variable management
  - Secure configuration handling
  - API key management
  - Environment-specific settings
- **Flask-WTF (v1.2.1)**: Form handling and CSRF protection
  - Form validation
  - Security measures
  - Input sanitization

### API & Communication
- **Requests (v2.26.0)**: HTTP library for API calls
  - External service integration
  - Webhook notifications
  - API communication
- **Flask-CORS (v4.0.0)**: Cross-Origin Resource Sharing
  - API access control
  - Security headers
  - Cross-origin requests handling

### Performance & Deployment
- **Gunicorn (v21.2.0)**: WSGI HTTP Server
  - Production deployment
  - Process management
  - Load balancing
- **WhiteNoise (v6.6.0)**: Static file serving
  - Efficient static file delivery
  - Caching optimization
  - CDN-like functionality

### Email Integration
- **SendGrid (v6.9.7)**: Email service integration
  - Performance report delivery
  - Email templating
  - Delivery tracking

## 🔄 Application Flow

1. **Request Handling**
   ```python
   @app.route('/employee/<email>')
   def employee_details(email):
       # Load employee data
       # Generate insights
       # Render template
   ```

2. **Data Processing**
   ```python
   def get_performance_verdict(metrics):
       # Calculate performance level
       # Generate automated analysis
       # Return performance verdict
   ```

3. **Template Rendering**
   ```html
   {% extends "base.html" %}
   {% block content %}
       <!-- Dynamic content rendering -->
   {% endblock %}
   ```

4. **Form Processing**
   ```python
   @app.route('/update_metrics/<email>', methods=['POST'])
   def update_metrics(email):
       # Process form data
       # Update metrics
       # Save changes
   ```

## 📊 Performance Metrics System

### Metric Categories
1. **Productivity**
   - Task completion rate
   - Project delivery
   - Quality of work

2. **Teamwork**
   - Collaboration effectiveness
   - Support to team members
   - Team contribution

3. **Communication**
   - Clarity of communication
   - Responsiveness
   - Documentation quality

### Automated Analysis
```python
def get_performance_analysis(metrics):
    if (metrics['productivity'] >= 90 and 
        metrics['teamwork'] >= 90 and 
        metrics['communication'] >= 90):
        return "Exceptional performance..."
    # Additional analysis logic
```

## 🔐 Security Features

1. **Input Validation**
   - Form data sanitization
   - Type checking
   - Range validation

2. **Data Protection**
   - Environment variable usage
   - Secure configuration
   - API key management

3. **Access Control**
   - Route protection
   - Admin authentication
   - Session management

## 🚀 Deployment Architecture

### Development Environment
- Flask development server
- Debug mode enabled
- Local file storage

### Production Environment
- Gunicorn WSGI server
- WhiteNoise for static files
- Environment-specific configuration

## 📈 Performance Optimization

1. **Caching**
   - Static file caching
   - Template caching
   - Data caching

2. **Database Optimization**
   - Efficient JSON structure
   - Indexed lookups
   - Optimized queries

3. **Resource Management**
   - Static file serving
   - Memory usage optimization
   - Connection pooling 