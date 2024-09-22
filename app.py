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


# Fetching the data from database into a dataframe
#table-1
def fetch_feedback_data(connection):
    query = """
    SELECT Courses.Title, AVG(CourseFeedback.Rating) as AverageRating
    FROM CourseFeedback
    JOIN Courses ON CourseFeedback.CourseID = Courses.CourseID
    GROUP BY Courses.Title;
    """
    return pd.read_sql(query, connection)

#table-2
def fetch_enrollment_data(connection):
    query = """
    SELECT Courses.Title, COUNT(Enrollments.UserID) as EnrollmentCount
    FROM Enrollments
    JOIN Courses ON Enrollments.CourseID = Courses.CourseID
    GROUP BY Courses.Title;
    """
    return pd.read_sql(query, connection)

#table-3
def fetch_user_roles_data(connection):
    query = "SELECT Role, COUNT(*) as RoleCount FROM Users GROUP BY Role;"
    return pd.read_sql(query, connection)

#table-4
def fetch_price_data(connection):
    query = "SELECT Price FROM Courses;"
    return pd.read_sql(query, connection)

#table-5
def fetch_students_with_courses(connection):
    query = """
    SELECT u.FirstName, u.LastName, c.Title AS CourseTitle, 
           i.FirstName AS InstructorFirstName, i.LastName AS InstructorLastName
    FROM Enrollments e
    JOIN Users u ON e.UserID = u.UserID
    JOIN Courses c ON e.CourseID = c.CourseID
    JOIN Users i ON c.InstructorID = i.UserID
    WHERE u.Role = 'Student';
    """
    return pd.read_sql(query, connection)

#table-6
def fetch_popular_courses(connection):
    query = """
    SELECT c.Title, COUNT(e.UserID) AS EnrollmentCount
    FROM Courses c
    JOIN Enrollments e ON c.CourseID = e.CourseID
    GROUP BY c.Title
    HAVING COUNT(e.UserID) > 2;
    """
    return pd.read_sql(query, connection)

# Route for the homepage
@app.route('/')
def index():
    connection = create_connection()
    
    feedback_data = fetch_feedback_data(connection)
    enrollment_data = fetch_enrollment_data(connection)
    user_roles_data = fetch_user_roles_data(connection)
    price_data = fetch_price_data(connection)
    students_with_courses = fetch_students_with_courses(connection)
    popular_courses = fetch_popular_courses(connection)

    generate_graphs(feedback_data, enrollment_data, user_roles_data, price_data, students_with_courses, popular_courses)

    connection.close()
    return render_template('index.html')

def generate_graphs(feedback_data, enrollment_data, user_roles_data, price_data, students_with_courses, popular_courses):
    sns.set(style="whitegrid")
    plt.figure(figsize=(20, 16))

    # 1. Average Course Ratings (Bar Plot)
    plt.subplot(3, 2, 1)
    barplot = sns.barplot(x="Title", y="AverageRating", data=feedback_data, palette="Blues_d")
    plt.title('Average Course Ratings')
    plt.ylabel('Average Rating')
    plt.ylim(0, 5)
    barplot.legend(title='Course Titles', labels=feedback_data['Title'], loc='upper left', bbox_to_anchor=(1, 1), fontsize='small')

    # 2. Enrollments per Course (Pie Chart)
    plt.subplot(3, 2, 2)
    pie = plt.pie(enrollment_data['EnrollmentCount'], labels=None, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
    plt.title('Enrollments per Course')
    plt.legend(enrollment_data['Title'], title="Courses", loc='upper left', bbox_to_anchor=(1.2, 1))

    # 3. User Roles Distribution (Pie Chart)
    plt.subplot(3, 2, 3)
    plt.pie(user_roles_data['RoleCount'], labels=user_roles_data['Role'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("husl"))
    plt.title('User Roles Distribution')

    # 4. Course Price Distribution (Histogram)
    plt.subplot(3, 2, 4)
    sns.histplot(price_data['Price'], kde=True, bins=10, color="purple")
    plt.title('Course Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')

    # 5. Students Enrolled in Courses (Bar Plot)
    plt.subplot(3, 2, 5)
    student_counts = students_with_courses.groupby('CourseTitle').size().reset_index(name='StudentCount')
    sns.barplot(x='StudentCount', y='CourseTitle', data=student_counts, palette="rocket")
    plt.title('Number of Students per Course')
    plt.xlabel('Student Count')

    # 6. Popular Courses (Bar Plot)
    plt.subplot(3, 2, 6)
    sns.barplot(x='EnrollmentCount', y='Title', data=popular_courses, palette="coolwarm")
    plt.title('Popular Courses (More than 2 Students Enrolled)')
    plt.xlabel('Enrollment Count')

    
    plt.tight_layout(pad=4.0)

    # Saving the graphs
    plt.savefig(os.path.join('static', 'graphs.png'))
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)