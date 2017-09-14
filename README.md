# Quizzing-Website
This website is made using Python-Django where people can quiz in real time.

#FUNCTIONING<br />
Firstly, the user needs to sign in either by making an account on the website or by signing up via facebook account.

Once he signs in, he has an option to enter any one of the three categories:
  - Sports
  - Movies
  - Maths
Since this is a demo project, there are just 1 or 2 questions depending which category the user selects.

Then he can select the answer and click on "Submit" button. After this, he is directed to a new page showing his score and giving him an option if he wants to play again, clicking on which he is redirected to the page displaying the categories.

#HIERARCHY
  /Polls
  |  /Static
  |  |  /category
  |  |  |  /images: Contains images used in website
  |  |  |  /style.css
  |  |  /polls
  |  |    /style.css
  |  |
  |  /templates
  |  |  /category.html
  |  |  /index.html
  |  |  /result.html
  |  |
  |  /admin.py  - Register tables here
  |  /apps.py   - AppConfig here
  |  /models.py - Made 3 tables here: Category, Question, choice
  |  /views.py  - define views here
  /
    
#HOW TO RUN
1. Run CMD and change directory to the "../quiz" folder
2. Run command "python manage.py runserver"
3. Open browser and type http://127.0.0.1:8000/polls/ in the address bar
4. Create an account and start playing!
