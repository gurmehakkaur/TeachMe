import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template
from urllib.parse import urlparse
app = Flask(__name__)
# Function to create a database connection
def create_connection():
    # Get the ClearDB database URL
    url = os.getenv('CLEARDB_DATABASE_URL')
    if url is None:
        raise Exception("CLEARDB_DATABASE_URL environment variable not set.")

    # Parse the database URL
    url = urlparse(url)
    connection = mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path[1:]  # Remove the leading slash
    )
    return connection

# Fetch course feedback data
def fetch_feedback_data(connection):
    query = """
    SELECT Courses.Title, AVG(CourseFeedback.Rating) as AverageRating
    FROM CourseFeedback
    JOIN Courses ON CourseFeedback.CourseID = Courses.CourseID
    GROUP BY Courses.Title;
    """
    return pd.read_sql(query, connection)

# Fetch enrollment data
def fetch_enrollment_data(connection):
    query = """
    SELECT Courses.Title, COUNT(Enrollments.UserID) as EnrollmentCount
    FROM Enrollments
    JOIN Courses ON Enrollments.CourseID = Courses.CourseID
    GROUP BY Courses.Title;
    """
    return pd.read_sql(query, connection)

# Fetch user roles data
def fetch_user_roles_data(connection):
    query = "SELECT Role, COUNT(*) as RoleCount FROM Users GROUP BY Role;"
    return pd.read_sql(query, connection)

# Route for the homepage
@app.route('/')
def index():
    connection = create_connection()
    
    feedback_data = fetch_feedback_data(connection)
    enrollment_data = fetch_enrollment_data(connection)
    user_roles_data = fetch_user_roles_data(connection)
    
    # Generate graphs
    generate_graphs(feedback_data, enrollment_data, user_roles_data)

    connection.close()
    return render_template('index.html')

# Function to generate and save graphs
def generate_graphs(feedback_data, enrollment_data, user_roles_data):
    # Create the average ratings graph
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 3, 1)
    plt.bar(feedback_data['Title'], feedback_data['AverageRating'], color='skyblue')
    plt.title('Average Course Ratings')
    plt.xlabel('Course Title')
    plt.ylabel('Average Rating')
    plt.xticks(rotation=45)
    plt.ylim(0, 5)
    plt.grid(axis='y')
    
    # Create the enrollment counts graph
    plt.subplot(1, 3, 2)
    plt.bar(enrollment_data['Title'], enrollment_data['EnrollmentCount'], color='lightgreen')
    plt.title('Enrollments per Course')
    plt.xlabel('Course Title')
    plt.ylabel('Number of Enrollments')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Create the user roles graph
    plt.subplot(1, 3, 3)
    plt.bar(user_roles_data['Role'], user_roles_data['RoleCount'], color='salmon')
    plt.title('User Roles Distribution')
    plt.xlabel('Role')
    plt.ylabel('Number of Users')
    plt.grid(axis='y')

    plt.tight_layout()
    plt.savefig(os.path.join('static', 'graphs.png'))
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)
