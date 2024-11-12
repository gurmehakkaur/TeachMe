import pandas as pd

class DataFetcher:
    def __init__(self, connection):
        self.connection = connection

    def fetch_feedback_data(self):
        query = """
        SELECT Courses.Title, AVG(CourseFeedback.Rating) as AverageRating
        FROM CourseFeedback
        JOIN Courses ON CourseFeedback.CourseID = Courses.CourseID
        GROUP BY Courses.Title;
        """
        return pd.read_sql(query, self.connection)

    def fetch_enrollment_data(self):
        query = """
        SELECT Courses.Title, COUNT(Enrollments.UserID) as EnrollmentCount
        FROM Enrollments
        JOIN Courses ON Enrollments.CourseID = Courses.CourseID
        GROUP BY Courses.Title;
        """
        return pd.read_sql(query, self.connection)

    def fetch_user_roles_data(self):
        query = "SELECT Role, COUNT(*) as RoleCount FROM Users GROUP BY Role;"
        return pd.read_sql(query, self.connection)

    def fetch_price_data(self):
        query = "SELECT Price FROM Courses;"
        return pd.read_sql(query, self.connection)

    def fetch_students_with_courses(self):
        query = """
        SELECT u.FirstName, u.LastName, c.Title AS CourseTitle, 
               i.FirstName AS InstructorFirstName, i.LastName AS InstructorLastName
        FROM Enrollments e
        JOIN Users u ON e.UserID = u.UserID
        JOIN Courses c ON e.CourseID = c.CourseID
        JOIN Users i ON c.InstructorID = i.UserID
        WHERE u.Role = 'Student';
        """
        return pd.read_sql(query, self.connection)

    def fetch_popular_courses(self):
        query = """
        SELECT c.Title, COUNT(e.UserID) AS EnrollmentCount
        FROM Courses c
        JOIN Enrollments e ON c.CourseID = e.CourseID
        GROUP BY c.Title
        HAVING COUNT(e.UserID) > 2;
        """
        return pd.read_sql(query, self.connection)
