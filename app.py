from flask import Flask, render_template
from database import DatabaseConnector
from data_fetcher import DataFetcher
from graph_generator import GraphGenerator

app = Flask(__name__)

@app.route('/')
def index():
    db_connector = DatabaseConnector()
    data_fetcher = DataFetcher(db_connector.get_connection())

    feedback_data = data_fetcher.fetch_feedback_data()
    enrollment_data = data_fetcher.fetch_enrollment_data()
    user_roles_data = data_fetcher.fetch_user_roles_data()
    price_data = data_fetcher.fetch_price_data()
    students_with_courses = data_fetcher.fetch_students_with_courses()
    popular_courses = data_fetcher.fetch_popular_courses()

    graph_generator = GraphGenerator()
    graph_generator.generate_graphs(feedback_data, enrollment_data, user_roles_data, price_data, students_with_courses, popular_courses)

    db_connector.close_connection()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
