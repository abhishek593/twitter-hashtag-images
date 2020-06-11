# twitter-hashtag-images
A web app written in Django that scrapes twitter images via hashtag using Scrapy

# Setup
'''
pip install -r requirements.txt
'''

# Database
'''
python manage.py makemigrations
python manage.py migrate
'''
If want to run admin 
'''
python manage.py createsuperuser
'''

# Start Project
run django and scrapyd
## Run django
'''
python manage.py runserver
'''
## Run scrapyd
'''
cd hashtag_images 
scrapyd
'''

# How to use
I did not bothered to create a form and a nice interface. Just gets the job done.
There are only two urls -
## For starting crawling
http://127.0.0.1/hashtag/api/crawl/<your_hashtag>/
## For seeing results
http://127.0.0.1/hashtag/api/show/<above_hashtag>/
