# Moengage-assignment

# Brewery Review

Brewery Review is a Django-based web application that allows users to search for breweries, view detailed information about them, and add reviews. This project uses Django for the backend and provides user authentication, brewery search, and review functionality.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Models](#models)
- [Views](#views)
- [Templates](#templates)
- [Admin](#admin)
- [License](#license)

## Features

- User authentication (signup, login, logout)
- Search for breweries by name or city
- View detailed information about a specific brewery
- Add reviews to breweries
- Admin interface to manage breweries and reviews

## Installation

### Prerequisites

- Python 3.10 or higher
- Django 4.2.5
- SQLite (default database)

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/brewery_review.git
    cd brewery_review
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Open your browser and go to:**

    ```
    http://127.0.0.1:8000
    ```

## Usage

### User Authentication

- Sign up at `/signup/`
- Log in at `/accounts/login/`
- Log out at `/accounts/logout/`

### Search Breweries

- Use the search bar at `/search/` to find breweries by name or city.

### View Brewery Details

- Click on a brewery from the search results to view its details and reviews.

### Add Reviews

- Log in and add a review to any brewery by visiting its detail page.

## Project Structure

