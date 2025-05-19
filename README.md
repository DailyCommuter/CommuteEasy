# CommuteEasy
A web application to offer real-time updates, schedules, and transit information for New York City's public transportation system

## Development

Make sure you have Node/npm installed on your device
If it is your first time starting the app,
**cd into DailyCommuterFrontend\client\daily-commuter**
Then run:

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
<!-- Start React -->
npm run dev
<!-- Start Flask -->
flask --app DailyCommuterBackend run --debug
```
