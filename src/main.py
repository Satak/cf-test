from flask import jsonify


def modify_message(message):
    if not message:
        return 'Your message was empty'
    return f'Your message was {message}'


def main(request):
    message = request.args.get('message')
    return jsonify({'message': modify_message(message), 'version': 11})
