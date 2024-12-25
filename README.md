# **TeachMe Analytical Dashboard**

**Live:** [TeachMe Dashboard](https://teachmestats.netlify.app/)
![image](https://github.com/user-attachments/assets/b2be0497-39ee-42a1-89a6-ae043e9729b1)


## **Overview**
**TeachMe** is like a clone of Udemy, and I have created a relational database for the application, although it has hypothetical data, the main focus was to be able to structure a complex real-life database, taking care of business logic. Also, I have shown my expertise in querying data using complex joins and subqueries with the screenshots pasted later in this document. The last and final step was to create **TeachMe Analytical Dashboard**, a web-based data visualization tool that connects to a MySQL database hosted on Heroku (ClearDB). It fetches and processes data from all tables of the database and uses **Pandas** for data processing and **Matplotlib** and **Seaborn** for data visualization, thus helping to present users data in an analytical manner which can lead to accurate business planning. 

Overall, this project showcases my expertise in database administration, advanced querying techniques, data processing, and data visualization, demonstrating my ability to manage and analyze complex datasets effectively.

## Business Rules
![image](https://github.com/user-attachments/assets/7db9ab08-a349-4b42-8d5e-210ae3b6864c)

## Tables
![image](https://github.com/user-attachments/assets/ef5aaa23-b760-450a-8baa-521483f83524)
![image](https://github.com/user-attachments/assets/4839e9be-5ac7-4fd7-b152-c8e61e2ebb51)
![image](https://github.com/user-attachments/assets/0a5ab28e-850c-4052-8158-364afaf7929a)
![image](https://github.com/user-attachments/assets/37bd07e9-c1d0-44a1-af2c-833d40ee72e0)
![image](https://github.com/user-attachments/assets/f2838545-cd64-421e-988e-8178b55f0705)
![image](https://github.com/user-attachments/assets/a1ba7bce-9177-42b2-b7f5-f377330f05f3)
![image](https://github.com/user-attachments/assets/5c593b7c-3f6b-48fa-a7fd-3e1a9dc127b2)
![image](https://github.com/user-attachments/assets/76e76c7a-ac41-429c-8846-b942ccc881d7)
![image](https://github.com/user-attachments/assets/59664f48-62ac-4b41-95e0-da1d2c63d266)
![image](https://github.com/user-attachments/assets/c0153963-e78b-407b-b027-67fc9c7afe41)

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

### 7. Find the average course price for instructors who have more than one course.
![image](https://github.com/user-attachments/assets/48ca9073-ecb5-4cef-ac1c-4cc42001ef04)

## **Key Technologies Used**
- **Backend**: Python (Flask)
- **Database**: MySQL (ClearDB on Heroku)
- **Data Processing**: Pandas
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS, Bootstrap (for UI styling)
- **Deployment**: Heroku

