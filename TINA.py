'''
Kristina Covington (ksc3bu) HW3
'''

import boto3
import json
import logging
import os
import aiml
import pymysql
import random

connection = pymysql.connect(host='medicalcenter.martyhumphrey.info', port=3306, user='aardvark9', passwd='sparky12', db='Medical')
crsr = connection.cursor()

bot = aiml.Kernel()
bot.learn("tina.aiml")

from base64 import b64decode
from urlparse import parse_qs


ENCRYPTED_EXPECTED_TOKEN = os.environ['kmsEncryptedToken']

kms = boto3.client('kms')
expected_token = kms.decrypt(CiphertextBlob=b64decode(ENCRYPTED_EXPECTED_TOKEN))['Plaintext']

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err, res=None):
        return {
                    'statusCode': '400' if err else '200',
                    'body': err.message if err else json.dumps(res),
                    'headers': {
                                    'Content-Type': 'application/json',
                                },
                }

def lambda_handler(event, context):
        params = parse_qs(event['body'])
        token = params['token'][0]
        if token != expected_token:
                logger.error("Request token (%s) does not match expected", token)
                return respond(Exception('Invalid request token'))
              
        user = params['user_name'][0]
        command = params['command'][0]
        channel = params['channel_name'][0]
        command_text = params['text'][0]

        return respond(None, "%s: %s" % (command_text, bot.respond(command_text)))
        
'''
------------ Testing -------------
'''
                                                          
sentence = "When is Florence Nightingale available on 2018-02-27"      

print(bot.respond(sentence))

sentence2 = "Who is available at 10 on date 2018-02-27"

print(bot.respond(sentence2))

sentence3 = "What is the last name of Florence"

print(bot.respond(sentence3))

sentence4 = "When is Joe Shmoe available on 2018-03-06"

print(bot.respond(sentence4))

sentence5 = "Who is available at 4 on date 2018-03-06"

print(bot.respond(sentence5))

sentence6 = "What is the last name of Joe"

print(bot.respond(sentence6))
