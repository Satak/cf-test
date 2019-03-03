from flask import jsonify
import logging


def modify_message(message):
    if not message:
        return 'Your message was empty'
    return f'Your message was {message}'


def main(request):
    logging.info('LOG ENTRY')
    message = request.args.get('message')
    return jsonify({'message': modify_message(message), 'version': 13})
