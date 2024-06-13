# EAgri Project

## Introduction
EAgri is a web-based platform built using Python and Django, designed to facilitate the buying and selling of fresh vegetables. The project aims to connect local farmers with consumers, ensuring the freshest produce reaches the market directly from the source. This approach supports local agriculture and provides consumers with high-quality, fresh vegetables at competitive prices.

## Features
- **User Registration and Login:** Secure registration and login system for both farmers and consumers.
- **Product Listings:** Farmers can list their fresh produce, including details such as type of vegetable, quantity available, and price.
- **Search and Filter:** Consumers can search for vegetables and filter results based on criteria like price, type, and location.
- **Cart and Checkout:** A shopping cart system where consumers can add products and proceed to checkout.
- **Order Management:** Farmers can manage orders and track the sales of their listed products.
- **Reviews and Ratings:** Consumers can leave reviews and ratings for the products they purchase.

## Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** SQLite (default for Django, can be changed to PostgreSQL, MySQL, etc.)
- **Version Control:** Git

## Prerequisites
- Python 3.x
- Django 3.x or later
- Git
- Virtualenv (recommended for managing dependencies)

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/eagri.git
    cd eagri
    ```

2. **Create a virtual environment** (if only required)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Create a superuser**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin user.

4. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server**
    ```bash
    python manage.py runserver
    ```
    Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Project Structure

![WhatsApp Image 2024-06-12 at 3 30 25 PM](https://github.com/dobariyaJay05/EAgri-Shop/assets/155874428/d22285a0-6d03-4ae8-8e69-c6cabb777e34)
