# **TeachMe Analytical Dashboard**

**Live:** [TeachMe Dashboard](https://teachmestats.netlify.app/)

## **Overview**
The **TeachMe Analytical Dashboard** is a web-based data visualization tool that connects to a MySQL database hosted on Heroku (ClearDB). It fetches and processes data from tables like `Courses`, `Users`, `Enrollments`, and `CourseFeedback`. Using **Pandas** for data processing and **Matplotlib** and **Seaborn** for data visualization, it displays insights and analytics on a Flask-based dashboard.

## **Key Technologies Used**
- **Backend**: Python (Flask)
- **Database**: MySQL (ClearDB on Heroku)
- **Data Processing**: Pandas
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS, Bootstrap (for UI styling)
- **Deployment**: Heroku

## **How to Run**

### **1. Set Up Database**
- Configure a MySQL database on ClearDB (or locally) using the provided DDL statements.
- Ensure the `CLEARDB_DATABASE_URL` environment variable is set with your database URL.

### **2. Install Dependencies**
Install the required python packages :

``bash
pip install -r requirements.txt

This will include:

Flask
mysql-connector-python
pandas
matplotlib
seaborn

## **3. Run the application**
export CLEARDB_DATABASE_URL='mysql://username:password@hostname/database'
python app.py

## **Access the dashboard**
Open http://127.0.0.1:5000 in your web browser to view the dashboard, which will display generated graphs showing key metrics for the TeachMe platform.

