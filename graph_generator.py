import matplotlib.pyplot as plt
import seaborn as sns
import os

class GraphGenerator:
    def generate_graphs(self, feedback_data, enrollment_data, user_roles_data, price_data, students_with_courses, popular_courses):
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
        plt.pie(enrollment_data['EnrollmentCount'], labels=None, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set2"))
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
        plt.savefig(os.path.join('static', 'graphs.png'))
        plt.close()
