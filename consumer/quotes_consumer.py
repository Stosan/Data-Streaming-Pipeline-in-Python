import time

from  producer.pipeline.redis_client import RedisClient


class QuotesConsumer:
    redis_client = RedisClient()
    sleep_seconds = 1

    def run(self):
        while True:
            if self.redis_client.get_data_from_pipeline() == 0:
                print(f'No new data in pipeline, sleeping for {self.sleep_seconds} seconds...')
                time.sleep(self.sleep_seconds)
                self.sleep_seconds += 1
                print("ok")
                continue

            self.sleep_seconds = 1
            data = self.redis_client.get_data_from_pipeline()
            print(f'Obtained data from pipeline, saving to file...')
            with open('quotes.txt', 'a+') as file:
                file.write(data.get('quote'))


if __name__ == "__main__":
    consumer = QuotesConsumer()
    consumer.run()