# p8_OC_purbeurre
Project 8 OpenClassrooms Course
# Project 8 - Openclassrooms Python Course - PurBeurre, a web food platform:

## Search for a product that you eat often and check out for healthier suggestions !

### What is in this project ?
- Use of Django Framework.
- Use of OOP and Python 3.7.
- Use of OpenFoodFact API services.
- Use of Bootstrap 4.
- Database (for production): SQLite3.
- Determinate a strategy for testing the application (in prod)
- Project is tested, coverage will reach upto 80% (goal - in prod)
- Test includes : Unit tests, integration tests (in prod)
- Use of pipenv (virtual env.)
- Respect and follow recommendations from PEP8 (style guide),
 PEP257(docformatter)

## The project
For this project, the main goal is to create a web application that allows
the user to search for a product into our database of Purbeurre.
Indeed, the data that you will find in this application has been 
retrieved and cleaned off from OpenFoodFacts and fed to our database.

This project involved in creating a client to connect to the API of OFF,
and then, install the framework Django for our project. From this moment, the 
idea of creating a web application with this framework has to be in this way of
thinking : 1 application = 1 responsibility.

For the user's experience, in one click he will find substitutes to 
his query. He will then have the choice to create an account, in order to 
be able to add this specific product to his favorites. This application
enable users to have a private account to be able to recording all their
likings.

This project has also followed the directions from the client concerning
the graphic chart.

### Structure of the code
In the folder **purbeurre**, is the main folder of the projet.
In the folder **purbeurre.openfoodfact**, you will find the API client for OFF.
In the folder **purbeurre.product**, you will find the first application that controls everypart of the products, its models, its urls, its views and forms.
In the folder **purbeurre.register**, you will find every file that controls users for the application. It also handles the user's favorite.
In the folder **static**, you will find all files and folder concerning
the front-end variables of the application (in CSS, images, JavaScript...).
It's the part that was given with the installation of Bootstrap 4.
In the folder **purbeurre.test**, has been constructed in order to ease the test session when the coder will implement a new feature on the application. I have decided to separate in differents folders the test by their field of testing (unit,integration, functional).
In the folder **templates**, you will find the base.html of this application.


##  Getting started

If you want to run this project, clone this project, and start you favorite editor (example: VisualCode).

First of all, you need to **install pipenv**.
* `pipenv install` (install all requirements), once loaded, don't
forget to `pipenv shell` in your terminal to activate  the environment.
The **advantage** of pipenv is that it is cross-platform. It is 
recommended by the official documentation for python's virtual
environment.

Second, run the command in your terminal :
Place yourself into  the project purbeurre and then :
* `python manage.py runserver` (kickstarts the server and it gives you access to the project)
* You may connect yourself at this adress on your web browser : http://localhost:8000/ or click on
the link that is presented on your terminal screen.
* You can stop the server by doing ctr+c in the server.

Third, the current local database might be empty, to feed it you may do these next steps :
* `python manage.py makemigrations <application_name>` (for example "products")
* `python manage.py migrate`
* `python manage.py initdb`

If you need to delete all the entries if the database, you may :
* 1st step : python manage.py deletedb
* 2nd step : delete the file at the path : purbeurre.products.migrations.0001_initial.py
Becareful not to delete the "____init____.pyc" ! 
* 3rd step : You may add more categories, or change the models.

### RUN Test
* Simply run this command in your terminal in the project : `python3 manage.py test --verbosity 2`

## Acknowledgment
I would like to thank my mentor, Thierry Chappuis, for all the help
and advices he gave to me to accomplish this project.