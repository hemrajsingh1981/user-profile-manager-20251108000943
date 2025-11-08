from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from app.models.user import User
from app import db

# Define a Blueprint for API routes
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Define a Marshmallow schema for user data validation
class UserSchema(Schema):
    name = fields.Str(required=True, error_messages={"required": "Name is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required.", "invalid": "Invalid email address."})
    age = fields.Int(required=True, validate=lambda n: n > 0, error_messages={"required": "Age is required.", "validator_failed": "Age must be a positive integer."})

@api_bp.route('/submit_user', methods=['POST'])
def submit_user():
    """Handles the submission of user profile data."""
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    schema = UserSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(json_data)
    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 422

    # Check if user with the same email already exists
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User with this email already exists.'}), 409

    # Create a new User object
    new_user = User(
        name=data['name'],
        email=data['email'],
        age=data['age']
    )

    try:
        # Add the new user to the database session and commit
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User data saved successfully'})
    except Exception as e:
        db.session.rollback()
        # Log the error for debugging purposes
        print(f"Error saving user: {e}")
        return jsonify({'message': 'An error occurred while saving user data.'}), 500

@api_bp.route('/users', methods=['GET'])
def get_users():
    """Fetches all users from the database."""
    try:
        users = User.query.all()
        user_schema = UserSchema(many=True)
        result = user_schema.dump(users)
        return jsonify(result)
    except Exception as e:
        print(f"Error fetching users: {e}")
        return jsonify({'message': 'An error occurred while fetching user data.'}), 500
