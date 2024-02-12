# py-blog

`py-blog` is a Django Blog that allows users to create posts and multiple entries for each post topic. The blog contains a home page that shows all posts in chronological order and other pages that allow users to edit or delete existing posts. 

## Features

'py-blog` is built with a user authentication and registration system. 

## Usage

## ⚙️ Installation

- Open CMD
  
- Change the current directory to the desktop

  `cd desktop`
   
- Clone this repository

  `git clone git@github.com:backendkolawole/py-blog.git`

- Change the current directory

  `cd py-blog`

- Create a virtual environment

  `python -m venv myvirtualenv`
  
- Activate virtual environment

  `myvirtualenv\Scripts\activate`

- Install all the packages listed in your requirements.txt file

  `pip install -r requirements.txt`

- In the same directory as settings.py, create a file called `.env`

  - Generate a secret key and set up `SECRET_KEY` variable in `.env` file

> [!WARNING]
> `SECRET_KEY` is the key to securing signed data – it is vital you keep this secure, or attackers could use it to generate their own signed values.

- Make migrations

  `python manage.py makemigrations`

- Apply migrations

  `python manage.py migrate`
  

- Run the server

  `python manage.py runserver`

