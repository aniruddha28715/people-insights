import os
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from jinja2 import Template
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PeopleInsightsGenerator:
    def __init__(self):
        self.employee_data = self._load_employee_data()
        self.email_template = self._load_email_template()
        
    def _load_employee_data(self):
        """Load employee data from a JSON file"""
        try:
            with open('employee_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: employee_data.json not found. Using sample data.")
            return self._get_sample_data()
    
    def _get_sample_data(self):
        """Generate sample employee data"""
        return {
            "employees": [
                {
                    "name": "John Doe",
                    "email": "john.doe@company.com",
                    "role": "Software Engineer",
                    "performance_metrics": {
                        "productivity": 85,
                        "teamwork": 90,
                        "communication": 88
                    },
                    "recent_achievements": [
                        "Completed project X ahead of schedule",
                        "Mentored 2 junior developers"
                    ]
                },
                {
                    "name": "Jane Smith",
                    "email": "jane.smith@company.com",
                    "role": "Product Manager",
                    "performance_metrics": {
                        "productivity": 92,
                        "teamwork": 95,
                        "communication": 90
                    },
                    "recent_achievements": [
                        "Launched new feature Y",
                        "Improved team velocity by 20%"
                    ]
                }
            ]
        }
    
    def _load_email_template(self):
        """Load email template from file"""
        template_str = """
        Dear {{ manager_name }},

        Here are the latest insights for your team member {{ employee.name }}:

        Performance Overview:
        - Role: {{ employee.role }}
        - Productivity Score: {{ employee.performance_metrics.productivity }}%
        - Teamwork Score: {{ employee.performance_metrics.teamwork }}%
        - Communication Score: {{ employee.performance_metrics.communication }}%

        Recent Achievements:
        {% for achievement in employee.recent_achievements %}
        - {{ achievement }}
        {% endfor %}

        Recommendations:
        {% if employee.performance_metrics.productivity < 85 %}
        - Consider discussing productivity improvement strategies
        {% endif %}
        {% if employee.performance_metrics.teamwork < 85 %}
        - Focus on team collaboration opportunities
        {% endif %}
        {% if employee.performance_metrics.communication < 85 %}
        - Work on communication skills development
        {% endif %}

        Best regards,
        People Insights Bot
        """
        return Template(template_str)
    
    def generate_insights(self, employee, manager_name):
        """Generate personalized insights for an employee"""
        return self.email_template.render(
            employee=employee,
            manager_name=manager_name
        )
    
    def send_email(self, to_email, subject, content):
        """Print email content instead of sending it"""
        print("\n" + "="*50)
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print("="*50)
        print(content)
        print("="*50 + "\n")
        return True

def main():
    # Initialize the insights generator
    generator = PeopleInsightsGenerator()
    
    # Example usage
    manager_name = "Sarah Johnson"
    
    for employee in generator.employee_data['employees']:
        # Generate insights
        insights = generator.generate_insights(employee, manager_name)
        
        # Send email
        subject = f"People Insights Report - {employee['name']} - {datetime.now().strftime('%Y-%m-%d')}"
        generator.send_email(employee['email'], subject, insights)

if __name__ == "__main__":
    main()

