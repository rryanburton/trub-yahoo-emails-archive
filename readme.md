#Django app for Trub archives

archived emails from a yahoo group were saved as .json files. this app converts them into a database and provides a front-end to view the messages.

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).



```sh
$ python3 -m venv baseproject-venv
$ source baseproject-venv/bin/activate
$ pip install -r requirements.txt

$ createdb <you_pick_name>  #this may have issues

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```
