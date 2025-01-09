# Django 2024

- A python based web framework
- Sometimes called as batteries included fraemwork - because it comes with a lot of built-in features

### Why Django? - Features

- Rapid development
- Database flexibility
- Built in admin interface
- Django uses Django template language (similar to jinja2 in flask)

### Model View Template (MVT) Architecture

- Model: Database

    - ORM: Object Relational Mapping

- View: Business Logic

    - receives http requests and returns http response

- Template: User Interface

    - HTML files

![alt text](image-1.png)


## FastAPI v/s Flask v/s Django

- Flask:
    - Minimalist framework with extendable features
    - Great for building small to medium sized applications
    - Easiest to learn

- Django:
    - Has features that saves a lot of times
        - ORM
        - Forms
        - Authentication
    - Ideal for handling complex web applications
    - Conventional project structure
    - Complex to learn

- Fast APi
    - New framework
    - Asynchronous support
    - Automatic data validation
    - Automatic Generation of OpenAPI documentation
    - Great for quickly building APIs that are self documented
    - Slightly trickier to setup

## Django Installation

'-m' flag is used to run module as script in python

## Running Django

```django-admin startproject mysite```