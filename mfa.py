# This code retieves the MFA code for deploying batch jobs
# This code can be inserted to any cli command to avoid needing to manually enter it

import threading
import time
import json
import pika

from pathlib import Path

class MFAToken():

    def __init__(self, phone_number):
        '''
        TODO: Add docstring for init
        '''
        self.code = None
        self.phone_number = phone_number

    def listen_for_message(self):
        '''
        Create a Trilio socketed connetion
        This will monitor for any messages received indicating a new token code
        '''
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='bastion.avantlink.net'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='avant-dev', exchange_type='direct')

        # Get the queue
        self.queue = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = self.queue.method.queue
        self.channel.queue_bind(
            exchange='avant-dev',
            queue=self.queue_name,
            routing_key='authy'
        )

    def callback(self, ch, method, properties, body):
        '''
        Create a periodic callback that checks the code received

        NOTE: Should check every 30 seconds
        FIXME: Need means for checking if code is about to expire (maybe)
        '''
        global snack_text
        if body is not None:
            data = json.loads(str(body, 'utf-8'))
            code = data['code']

            if code == '' or code is None:
                self.listen_for_message()
            else:
                self.code = code

    def background(self):
        '''
        Background the socket server and trigger the callback
        '''
        self.channel.basic_consume(on_message_callback=self.callback, queue=self.queue_name, auto_ack=True)
        self.channel.start_consuming()

# Temp test code
if __name__ == '__main__':
    phone_number = 5135025652
    mfa = MFAToken(phone_number)
    thread = threading.Thread(target=mfa.background)
    thread.daemon = True
    thread.start()

    # driver.implicitly_wait(0)
    # try:
    #     if driver.find_element(By.XPATH, '//input[@name="phoneNumber"]').is_displayed():
    #         driver.find_element(By.XPATH, '//input[@name="phoneNumber"]').send_keys(str(phone_number))
    # except NoSuchElementException:
    #     pass
    # finally:
    #     WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    #     driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//button[@type="submit"]'))

    time.sleep(2)
    mfa.listen_for_message()
    time.sleep(5)