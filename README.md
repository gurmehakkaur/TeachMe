# **TeachMe Analytical Dashboard**

**Live:** [TeachMe Dashboard](https://teachmestats.netlify.app/)
![image](https://github.com/user-attachments/assets/b2be0497-39ee-42a1-89a6-ae043e9729b1)


## **Overview**
The **TeachMe Analytical Dashboard** is a web-based data visualization tool that connects to a MySQL database hosted on Heroku (ClearDB). It fetches and processes data from tables like `Courses`, `Users`, `Enrollments`, and `CourseFeedback`. Using **Pandas** for data processing and **Matplotlib** and **Seaborn** for data visualization, it displays insights and analytics on a Flask-based dashboard.

## **Key Technologies Used**
- **Backend**: Python (Flask)
- **Database**: MySQL (ClearDB on Heroku)
- **Data Processing**: Pandas
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS, Bootstrap (for UI styling)
- **Deployment**: Heroku

![image](https://github.com/user-attachments/assets/fae35539-1e89-482d-b008-859f967b0b19)

## DQL Queries
### 1. Retrieve all students who are enrolled in courses, along with the course titles and instructors.
![image](https://github.com/user-attachments/assets/deeef541-7e33-4614-8888-df9c83d4d7e2)


### 2. Create a view to list all courses along with the number of students enrolled in each course.
![image](https://github.com/user-attachments/assets/8e690441-cad2-4b07-8417-8a272453d46c)

### 3. Calculate the average score for each test across all students.
![image](https://github.com/user-attachments/assets/39c0f1f1-d9bc-4760-bf80-770dee5634f4)

### 4. Find the course with the highest enrollment.
![image](https://github.com/user-attachments/assets/02a4be57-1ef0-44f0-95b5-55e9068eba87)

### 5. List all students who enrolled in the last 30 days.
![image](https://github.com/user-attachments/assets/eef4429e-c5a1-454e-a9da-cf065b9231b0)

### 6. Display the full name of students along with their enrollment dates, formatted.
![image](https://github.com/user-attachments/assets/2532d440-4e51-42a7-b246-1cf934320c11)

### 8. Find the average course price for instructors who have more than one course.
![image](https://github.com/user-attachments/assets/48ca9073-ecb5-4cef-ac1c-4cc42001ef04)




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

