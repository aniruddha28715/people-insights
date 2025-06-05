# People Insights Dashboard

A simple, interactive dashboard for tracking employee performance and sending performance updates.

## Features

- **Employee Performance Tracking**
  - View performance metrics (Productivity, Teamwork, Communication)
  - Track recent achievements
  - Visual progress indicators

- **Interactive Employee Management**
  - Edit employee details
  - Update performance metrics
  - Add/remove achievements
  - Real-time updates

- **Performance Communication**
  - Send personalized performance emails
  - Customizable email templates
  - Preview before sending

## Live Demo

Visit the dashboard at: https://aniruddha28715.github.io/people-insights/

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/aniruddha28715/people-insights.git
cd people-insights
```

2. Start the local server:
```bash
cd docs
python3 -m http.server 8000
```

3. Open your browser and visit:
```
http://localhost:8000
```

## How to Use

### Viewing Employee Performance
- Each employee card shows:
  - Name and role
  - Performance metrics with visual indicators
  - Recent achievements
  - Action buttons for email and editing

### Editing Employee Details
1. Click the "Edit Details" button on any employee card
2. Update:
   - Basic information (name, email, role)
   - Performance metrics (0-100 scale)
   - Add or remove achievements
3. Click "Save Changes" to update

### Sending Performance Emails
1. Click the "Send Email" button on any employee card
2. Review and customize:
   - Email subject
   - Email body with performance details
3. Click "Send Email" to send

## Technologies Used

- HTML5
- TailwindCSS for styling
- JavaScript for interactivity
- Font Awesome for icons

## Project Structure

```
people-insights/
├── docs/                 # Static site files
│   ├── index.html       # Main dashboard
│   ├── js/              # JavaScript files
│   └── .nojekyll        # GitHub Pages configuration
└── README.md            # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.

---

Made with ❤️ by [Aniruddha Kulkarni] 