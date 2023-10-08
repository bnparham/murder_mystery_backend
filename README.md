# Murder Mystery

Welcome to the Murder Mystery project! This README guide will help you get started with setting up and running the project on your local machine.

## Getting Started

Follow these steps to set up the project:

### 1. Setting Up a Virtual Environment

Before you begin, it's a good practice to create a virtual environment to isolate your project's dependencies. If you haven't installed `virtualenv`, follow these steps to set it up:

```bash
# Install virtualenv globally (if not already installed)
pip install virtualenv

# Create a virtual environment named 'env' (you can choose a different name)
virtualenv env

# Activate the virtual environment
# On Windows
env\Scripts\activate
# On macOS and Linux
source env/bin/activate
```

### 2. Installing Project Dependencies

With your virtual environment activated, navigate to the project directory and install the required dependencies listed in the `requirements.txt` file:

```bash
# Navigate to the project directory
cd murder_mystery

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Project
```bash
#Navigate to the project directory:
cd murder_mystery

#Apply database migrations:
python manage.py migrate

#Start the Django development server:
python manage.py runserver
```