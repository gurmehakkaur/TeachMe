****TeachMe Analytical Dashboard

Live: https://teachmestats.netlify.app/

**Overview
This project connects to a MySQL database hosted on Heroku using ClearDB and fetches data from tables such as Courses, Users, Enrollments, and CourseFeedback. 
It then processes the database using Pandas and visualizes these data points as graphs using Matplotlib and Seaborn, displaying the results on a web-based dashboard built with Flask.

**Key Technologies Used
Backend: Python (Flask)
Database: MySQL (ClearDB on Heroku)
Data Processing: Pandas
Data Visualization: Matplotlib, Seaborn
Frontend: HTML, CSS, Bootstrap (for UI styling)
Deployment: Heroku

**How to Run
*Set Up Database:
Configure a MySQL database on ClearDB (or locally) with the provided DDL statements.
Make sure to set up the CLEARDB_DATABASE_URL environment variable with your database URL.

*Install Dependencies:
bash
Copy code
pip install -r requirements.txt
This includes Flask, mysql-connector-python, pandas, matplotlib, and seaborn.

*Run the Application:
export CLEARDB_DATABASE_URL='mysql://username:password@hostname/database'
python app.py
This will start the Flask server, which you can access at http://127.0.0.1:5000.

*Access the Dashboard:
Open http://127.0.0.1:5000 in your web browser.
The dashboard displays generated graphs on key metrics for the TeachMe platform.

