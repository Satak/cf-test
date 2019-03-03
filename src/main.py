from flask import jsonify


def main(request):
    message = request.args.get('message')
    return jsonify({'message': message, 'version': 5})
