# Flask Movie App

## Overview

Welcome to the **Flask Movie App**! This project is a dynamic web application built with Flask and SQLAlchemy, designed to manage a collection of movies. The app allows users to add, edit, and delete movies, as well as sort and view them based on various attributes. The application also features an elegant and responsive design, leveraging Bootstrap for styling.

## Features

- **Movie Management:** Add new movies to the database with details such as title, year, description, rating, ranking, review, and image URL.
- **Edit Movie Details:** Update the rating and review for any movie in the collection.
- **Delete Movies:** Remove movies from the database with a single click.
- **Dynamic Sorting:** Sort movies by title, year, rating, or ranking using query parameters.
- **Responsive Design:** The application is fully responsive, ensuring a seamless experience across different devices.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for Python.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Flask-WTF:** Integrates Flask with WTForms to handle form rendering and validation.
- **Bootstrap5:** A front-end framework for building responsive and visually appealing web pages.

## Getting Started

To get started with this project locally, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/flask-movie-app.git
    cd flask-movie-app
    ```

2. **Install Dependencies:**
    Create a virtual environment and install the required packages:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Application:**
    Set up the database and run the Flask development server:
    ```bash
    flask run
    ```

4. **Visit the Application:**
    Open your browser and go to `http://127.0.0.1:5000` to start using the app.

## Database Schema

The application uses a SQLite database with a single table:

- **Movie**
  - `id`: Integer, Primary Key
  - `title`: String, Unique, Not Null
  - `year`: Integer
  - `description`: String
  - `rating`: Float
  - `ranking`: Integer, Unique, Not Null
  - `review`: String
  - `img_url`: String
  - `created_at`: DateTime, Default to Current UTC Time

## Contributing

Feel free to submit issues, pull requests, or suggest improvements. All contributions are welcome!



