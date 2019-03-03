from flask import jsonify
import logging

VERSION = 14


def modify_message(message):
    if not message:
        return 'Your message was empty'
    return f'Your message was {message}'


def main(request):
    logging.info('LOG Info ENTRY')
    logging.warning('Warning entry')
    logging.debug('Debug entry')
    logging.error('Error entry')
    message = request.args.get('message')
    return jsonify({'message': modify_message(message), 'version': VERSION})
