from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from people_insights import PeopleInsightsGenerator
import json
from datetime import datetime
from whitenoise import WhiteNoise
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='docs')
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')  # Use environment variable in production
CORS(app)

# Initialize WhiteNoise for static files
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

# Initialize the insights generator
insights_generator = PeopleInsightsGenerator()

def get_performance_verdict(metrics):
    """Generate performance verdict based on metrics"""
    if (metrics['productivity'] >= 90 and 
        metrics['teamwork'] >= 90 and 
        metrics['communication'] >= 90):
        return "Outstanding Performance"
    elif (metrics['productivity'] >= 75 and 
          metrics['teamwork'] >= 75 and 
          metrics['communication'] >= 75):
        return "Good Performance"
    elif (metrics['productivity'] >= 50 and 
          metrics['teamwork'] >= 50 and 
          metrics['communication'] >= 50):
        return "Average Performance"
    else:
        return "Needs Improvement"

def get_performance_analysis(metrics):
    """Generate detailed performance analysis based on metrics"""
    if (metrics['productivity'] >= 90 and 
        metrics['teamwork'] >= 90 and 
        metrics['communication'] >= 90):
        return "Exceptional performance across all metrics. Consistently exceeds expectations in productivity, teamwork, and communication."
    elif (metrics['productivity'] >= 75 and 
          metrics['teamwork'] >= 75 and 
          metrics['communication'] >= 75):
        return "Strong performance with good balance across all areas. Shows consistent delivery and effective collaboration."
    elif (metrics['productivity'] >= 50 and 
          metrics['teamwork'] >= 50 and 
          metrics['communication'] >= 50):
        return "Meets basic expectations. Has potential for improvement in all areas."
    else:
        return "Performance needs significant improvement. Immediate attention required in multiple areas."

def load_employee_data():
    try:
        with open('employee_data.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, dict) or 'employees' not in data:
                return {'employees': []}
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {'employees': []}

def save_employee_data(data):
    with open('employee_data.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    """Render the main dashboard"""
    employees = load_employee_data().get('employees', [])
    return render_template('index.html', employees=employees)

@app.route('/admin')
def admin_panel():
    """Render the admin panel"""
    employees = load_employee_data().get('employees', [])
    return render_template('admin.html', employees=employees)

@app.route('/employee/<email>')
def employee_details(email):
    """Show detailed insights for a specific employee"""
    data = load_employee_data()
    employee = next((emp for emp in data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        insights = insights_generator.generate_insights(employee, "Sarah Johnson")
        performance_verdict = get_performance_verdict(employee['performance_metrics'])
        performance_analysis = get_performance_analysis(employee['performance_metrics'])
        return render_template('employee_details.html', 
                             employee=employee, 
                             insights=insights,
                             performance_verdict=performance_verdict,
                             performance_analysis=performance_analysis)
    return redirect(url_for('index'))

@app.route('/send_insights/<email>', methods=['POST'])
def send_insights(email):
    """Send insights email to an employee"""
    data = load_employee_data()
    employee = next((emp for emp in data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        try:
            insights = insights_generator.generate_insights(employee, "Sarah Johnson")
            subject = f"People Insights Report - {employee['name']} - {datetime.now().strftime('%Y-%m-%d')}"
            
            # Create email content
            email_content = f"""
==================================================
To: {employee['email']}
Subject: {subject}
==================================================

Dear {employee['name']},

Here are the latest insights for your team member {employee['name']}:

Performance Overview:
- Role: {employee['role']}
- Productivity Score: {employee['performance_metrics']['productivity']}%
- Teamwork Score: {employee['performance_metrics']['teamwork']}%
- Communication Score: {employee['performance_metrics']['communication']}%

Performance Verdict: {get_performance_verdict(employee['performance_metrics'])}

Analysis:
{get_performance_analysis(employee['performance_metrics'])}

Recent Achievements:
{chr(10).join(['- ' + achievement for achievement in employee['recent_achievements']])}

Keep up the great work!

Best regards,
Your Manager
"""
            # Print email to terminal
            print(email_content)
            flash(f'Insights sent successfully to {employee["name"]}!', 'success')
        except Exception as e:
            flash(f'Failed to send insights: {str(e)}', 'error')
    return redirect(url_for('employee_details', email=email))

@app.route('/update_metrics/<email>', methods=['POST'])
def update_metrics(email):
    """Update employee performance metrics"""
    data = load_employee_data()
    employee = next((emp for emp in data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        try:
            employee['performance_metrics']['productivity'] = int(request.form['productivity'])
            employee['performance_metrics']['teamwork'] = int(request.form['teamwork'])
            employee['performance_metrics']['communication'] = int(request.form['communication'])
            
            # Update last updated timestamp and mark as reviewed
            employee['admin_remarks'] = {
                'last_updated': datetime.now().strftime('%Y-%m-%d'),
                'remarks': get_performance_analysis(employee['performance_metrics']),
                'reviewed': True
            }
            
            # Save updated data
            save_employee_data(data)
            
            flash('Metrics updated successfully!', 'success')
        except Exception as e:
            flash(f'Error updating metrics: {str(e)}', 'error')
    return redirect(url_for('employee_details', email=email))

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        employee = data['employee']
        
        # Create email content
        email_content = f"""
        Dear {employee['name']},

        I wanted to share some insights about your recent performance:

        Performance Metrics:
        - Productivity: {employee['performance_metrics']['productivity']}%
        - Teamwork: {employee['performance_metrics']['teamwork']}%
        - Communication: {employee['performance_metrics']['communication']}%

        Performance Verdict: {get_performance_verdict(employee['performance_metrics'])}
        
        Analysis:
        {get_performance_analysis(employee['performance_metrics'])}

        Recent Achievements:
        {chr(10).join(['- ' + achievement for achievement in employee['recent_achievements']])}

        Keep up the great work!

        Best regards,
        Your Manager
        """

        # Create SendGrid message
        message = Mail(
            from_email=FROM_EMAIL,
            to_emails=employee['email'],
            subject=f'Performance Update - {employee["name"]}',
            plain_text_content=email_content
        )

        # Send email
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        return jsonify({'success': True, 'message': 'Email sent successfully'})
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/register', methods=['GET', 'POST'])
def register_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')
        achievements = [a.strip() for a in request.form.get('achievements').split('\n') if a.strip()]
        
        # Create new employee data matching the existing structure
        new_employee = {
            "name": name,
            "email": email,
            "role": role,
            "performance_metrics": {
                "productivity": 0,
                "teamwork": 0,
                "communication": 0
            },
            "recent_achievements": achievements,
            "admin_remarks": {
                "last_updated": datetime.now().strftime("%Y-%m-%d"),
                "remarks": "New employee - Initial assessment pending",
                "reviewed": False
            }
        }
        
        # Load existing data
        data = load_employee_data()
        employees = data.get('employees', [])
        
        # Check if employee already exists
        if any(emp['email'] == email for emp in employees):
            flash('An employee with this email already exists.', 'error')
            return redirect(url_for('register_employee'))
        
        # Add new employee
        employees.append(new_employee)
        data['employees'] = employees
        save_employee_data(data)
        
        flash('Registration successful! Please wait for admin review.', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html')

@app.route('/add_achievement/<email>', methods=['POST'])
def add_achievement(email):
    """Add a new achievement for an employee"""
    data = load_employee_data()
    employee = next((emp for emp in data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        try:
            new_achievement = request.form.get('achievement', '').strip()
            if new_achievement:
                employee['recent_achievements'].append(new_achievement)
                save_employee_data(data)
                flash(f'New achievement added for {employee["name"]}!', 'success')
            else:
                flash('Achievement cannot be empty.', 'error')
        except Exception as e:
            flash(f'Error adding achievement: {str(e)}', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001) 