// Default email template
const defaultEmailTemplate = {
    subject: "Performance Update - {employee_name}",
    body: `Dear {employee_name},

I wanted to share some insights about your recent performance:

Performance Metrics:
- Productivity: {productivity}%
- Teamwork: {teamwork}%
- Communication: {communication}%

Recent Achievements:
{achievements}

Keep up the great work!

Best regards,
Your Manager`
};

// Function to format email template
function formatEmailTemplate(template, employee) {
    let formattedTemplate = template.body
        .replace(/{employee_name}/g, employee.name)
        .replace(/{productivity}/g, employee.performance_metrics.productivity)
        .replace(/{teamwork}/g, employee.performance_metrics.teamwork)
        .replace(/{communication}/g, employee.performance_metrics.communication)
        .replace(/{achievements}/g, employee.recent_achievements.map(a => `- ${a}`).join('\n'));

    let subject = template.subject.replace(/{employee_name}/g, employee.name);

    return { subject, body: formattedTemplate };
}

// Function to show email editor modal
function showEmailEditor(employee) {
    const template = formatEmailTemplate(defaultEmailTemplate, employee);
    
    const modal = document.createElement('div');
    modal.className = 'fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full';
    modal.innerHTML = `
        <div class="relative top-20 mx-auto p-5 border w-4/5 shadow-lg rounded-md bg-white">
            <div class="mt-3">
                <h3 class="text-lg font-medium text-gray-900 mb-4">Edit Email</h3>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Subject:</label>
                    <input type="text" id="emailSubject" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" value="${template.subject}">
                </div>
                <div class="mb-4">
                    <label class="block text-gray-700 text-sm font-bold mb-2">Body:</label>
                    <textarea id="emailBody" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" rows="10">${template.body}</textarea>
                </div>
                <div class="flex justify-end space-x-3">
                    <button onclick="this.closest('.fixed').remove()" class="bg-gray-500 text-white px-4 py-2 rounded-md hover:bg-gray-600">Cancel</button>
                    <button onclick="sendCustomEmail('${employee.email}', document.getElementById('emailSubject').value, document.getElementById('emailBody').value)" class="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700">Send Email</button>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

// Function to send custom email
function sendCustomEmail(to, subject, body) {
    // In a real implementation, this would send the actual email
    alert(`Email would be sent to ${to}\n\nSubject: ${subject}\n\nBody:\n${body}`);
    document.querySelector('.fixed').remove();
} 