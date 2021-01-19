#### Starting with a Django project

1. Create django project: 
   `django-admin startproject mysite`

2. Run server
   `python manage.py runserver`

3. Create an 'app' called polls
   `python manage.py startapp polls`

4. Add urls.py to the polls app

5. Add polls/urls.py to the top level urls.py 
   You can open up `http://127.0.0.1:8000/polls/` in browser now. Ignore the migrations related warning - we'll get to it in a bit.

6. Look at settings.py - we will use the default DB sqlite for now:

   ```
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

   INSTALLED_APPS -> default apps

7. To use the above apps, at least one table is needed. We can create it now by running:
   `python manage.py migrate`

8. Create a model
   A model is the single, definitive source of truth about your data. It contains the essential fields and behaviors of the data you’re storing

9. Activate the `polls` app by adding it to INSTALLED_APPS

10. `python manage.py makemigrations polls`
    The change gets stored as a `migration` in the polls/migrations folder

11. Execute it:
    `python manage.py sqlmigrate polls 0001`
    `python manage.py migrate`

12. Admin page:
    `python manage.py createsuperuser` and go to http://127.0.0.1:8000/admin/login/?next=/admin/
    Register app to admin in polls/admin.py

13. Create different views

14. Use Django templates like below:

    ```bash
     {% if latest_question_list %}
            <ul>
            {% for question in latest_question_list %}
                 <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No polls are available.</p>
        {% endif %}
    ```

15. 