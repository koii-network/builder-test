from flask import Blueprint, request, jsonify
from src.controllers.string_controller import StringController

string_bp = Blueprint('string', __name__)

@string_bp.route('/reverse', methods=['POST'])
def reverse_string():
    """
    Route to handle string reversal.
    
    Expects a JSON payload with a 'string' key.
    Returns the reversed string.
    """
    data = request.get_json()
    
    if not data or 'string' not in data:
        return jsonify({'error': 'No string provided'}), 400
    
    try:
        reversed_string = StringController.reverse(data['string'])
        return jsonify({'reversed_string': reversed_string}), 200
    except TypeError as e:
        return jsonify({'error': str(e)}), 400