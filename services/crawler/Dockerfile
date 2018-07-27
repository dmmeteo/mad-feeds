FROM python:3

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add app
COPY . /usr/src/app

# install requirements
RUN pip install -r requirements.txt

# run server
CMD scrapy crawl mia_feed
