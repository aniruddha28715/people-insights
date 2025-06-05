// Email configuration
const EMAIL_CONFIG = {
    service: 'gmail',
    auth: {
        user: 'your-email@gmail.com',
        pass: 'your-app-specific-password'
    }
};

// Function to generate email content
function generateEmailContent(employee) {
    const metrics = employee.performance_metrics;
    const achievements = employee.recent_achievements;
    
    return `
        Dear ${employee.name},

        I wanted to share some insights about your recent performance:

        Performance Metrics:
        - Productivity: ${metrics.productivity}%
        - Teamwork: ${metrics.teamwork}%
        - Communication: ${metrics.communication}%

        Recent Achievements:
        ${achievements.map(achievement => `- ${achievement}`).join('\n')}

        Keep up the great work!

        Best regards,
        Your Manager
    `;
}

// Function to send email
async function sendEmail(employee) {
    try {
        const response = await fetch('/send-email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ employee })
        });

        const result = await response.json();
        
        if (result.success) {
            alert('Email sent successfully!');
        } else {
            throw new Error(result.message);
        }
        
        return true;
    } catch (error) {
        console.error('Error sending email:', error);
        alert('Failed to send email: ' + error.message);
        return false;
    }
} 