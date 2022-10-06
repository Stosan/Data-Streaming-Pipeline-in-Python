### This ptroject uses Scrapy and Redis to simulate a streaming pipeline.
#### Data streaming is the process of transmitting a continuous flow of data.

We’ll be using Redis as the data pipeline and a very simple data scraping microservice using Scrapy independently as a data producer and a separate microservice as a data consumer.
To start the app:
- pip install requirements.txt
- Run  scrapy startproject producer in terminal
- Run scrapy crawl quotes
