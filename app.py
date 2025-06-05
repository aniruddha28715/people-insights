from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from people_insights import PeopleInsightsGenerator
import json
from datetime import datetime
from whitenoise import WhiteNoise
import os
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__, static_folder='docs')
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')  # Use environment variable in production
CORS(app)

# Initialize WhiteNoise for static files
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

# Initialize the insights generator
insights_generator = PeopleInsightsGenerator()

# Initialize SendGrid client
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
FROM_EMAIL = os.getenv('FROM_EMAIL', 'your-verified-sender@yourdomain.com')

@app.route('/')
def index():
    """Render the main dashboard"""
    return render_template('index.html', employees=insights_generator.employee_data['employees'])

@app.route('/employee/<email>')
def employee_details(email):
    """Show detailed insights for a specific employee"""
    employee = next((emp for emp in insights_generator.employee_data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        insights = insights_generator.generate_insights(employee, "Sarah Johnson")
        return render_template('employee_details.html', 
                             employee=employee, 
                             insights=insights)
    return redirect(url_for('index'))

@app.route('/send_insights/<email>', methods=['POST'])
def send_insights(email):
    """Send insights email to an employee"""
    employee = next((emp for emp in insights_generator.employee_data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        insights = insights_generator.generate_insights(employee, "Sarah Johnson")
        subject = f"People Insights Report - {employee['name']} - {datetime.now().strftime('%Y-%m-%d')}"
        if insights_generator.send_email(employee['email'], subject, insights):
            flash(f'Insights sent successfully to {employee["name"]}!', 'success')
        else:
            flash('Failed to send insights. Please try again.', 'error')
    return redirect(url_for('employee_details', email=email))

@app.route('/update_metrics/<email>', methods=['POST'])
def update_metrics(email):
    """Update employee performance metrics"""
    employee = next((emp for emp in insights_generator.employee_data['employees'] 
                    if emp['email'] == email), None)
    if employee:
        try:
            employee['performance_metrics']['productivity'] = int(request.form['productivity'])
            employee['performance_metrics']['teamwork'] = int(request.form['teamwork'])
            employee['performance_metrics']['communication'] = int(request.form['communication'])
            
            # Save updated data
            with open('employee_data.json', 'w') as f:
                json.dump(insights_generator.employee_data, f, indent=4)
            
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

if __name__ == '__main__':
    app.run(debug=True, port=5001) 