from flask import jsonify
import logging

VERSION = 15
APP_NAME = 'cf-test'


def modify_message(message, request):
    if not message:
        logging.error(f'{APP_NAME}_APP_ERROR: Empty message. IP: {request.remote_addr}')
        return 'Your message was empty'
    logging.info(f'{APP_NAME}_APP_INFO: Message == {message}')
    return f'Your message was {message}'


def main(request):
    message = request.args.get('message')
    return jsonify({'message': modify_message(message, request), 'version': VERSION})
