# INFO3180 - Project1
This is the starter code for Project1

Remember to always create a virtual environment and install the packages in your requirements file

```
$ python -m venv venv (you may need to use python3 or python3.5 [on Cloud9] instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt 
$ python run.py



sudo service postgresql start 
sudo sudo -u postgres psql
create user "devnubproject";
create database "project1"; 
\password devnubproject                =>(project1)
alter database project1 owner to devnubproject; 

\q 

python flask-migrate.py db init
python flask-migrate.py db migrate
python flask-migrate.py db upgrade 



heroku login
heroku apps:create
git push heroku master 

heroku addons:create heroku-postgresql:hobby-dev
heroku config -s 
```
