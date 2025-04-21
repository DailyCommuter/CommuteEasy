# LCBoot2025

NYC-Transit-Hub
A web application to offer real-time updates, schedules, and transit information for New York City's public transportation system

## Suggested Key Features

- Interactive Map: Display a real-time map of subway and bus routes, allowing users to visualize transit options Service Status
- Dashboard: Show an overview of the status of all MTA services in a single dashboard. Accessibility Information: Include details about elevator and escalator availability at stations for accessibility.
- Multilingual Support: Offer the application in multiple languages.
- User Accounts: Basic account creation and user authentication using [Firebase](https://firebase.google.com/docs/auth/web/start).
- Favorites and Alerts: Allow users to save favorite routes/stations and set up notifications for service changes or delays

## Suggested Technology Stack

- Frontend:
  - Framework: Use any free and open-source JavaScript framework.
  - Styling: Utilize CSS framework for rapid UI development. Ensure the application is mobile-friendly. [Guide](https://github.com/dypsilon/frontend-dev-bookmarks?tab=readme-ov-file#readme)
- Backend:
  - Language: Python with Flask (lightweight and easy-to-use web framework).
  - Database: SQLite (lightweight, file-based database, suitable for small projects).
  - API: Ensure compliance with the chosen API's usage limits.
- Testing: Introduce basic unit and integration testing using tools like Jest (for JavaScript) or PyTest (for Python). [Guide](https://github.com/TheJambo/awesome-testing)
- Deployment: [Netlify](https://www.netlify.com/) or [Vercel](https://vercel.com/) (free hosting options). Version Control: Git (for version control) and GitHub (for repository hosting).
- Security: Implement basic security measures for user data.
- Documentation: Keep code and API usage documented for maintainability. [Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)

## Development

Make sure you have Node/npm installed on your device
If it is your first time starting the app run:

```cmd
npm i
```

For local development, run the following commands in your terminal

```cmd
pip install virtualenv
virtualenv venv
venv\Scripts\activate
(for MacOS/Linux: source venv/bin/activate)
pip install -r requirements.txt

<!-- Initialize the database -->
flask --app DailyCommuterBackend init-db
<!-- Start the app -->
npm run dev
(not sure about this)
flask --app DailyCommuterBackend run --debug
```
