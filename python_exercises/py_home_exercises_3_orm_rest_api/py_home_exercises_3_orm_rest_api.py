import os
import logging
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Create the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wishlist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up logging
logging.basicConfig(
    filename='app.log',        # Log file name
    level=logging.DEBUG,       # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s %(levelname)s: %(message)s',  # Log format
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Create a logger for this application
logger = logging.getLogger(__name__)

db = SQLAlchemy(app)

# Define models (Category and VideoGame)
class Category(db.Model):
    __tablename__ = 'categories'
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50), nullable=False, unique=True)
    
    VideoGames = db.relationship('VideoGame', back_populates='Category')

class VideoGame(db.Model):
    __tablename__ = 'videogames'
    Id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    ReleaseYear = db.Column(db.Integer, nullable=False)
    CategoryId = db.Column(db.Integer, db.ForeignKey('categories.Id'), nullable=False)
    
    Category = db.relationship('Category', back_populates='VideoGames')

# Automatically create the database if it doesn't exist
if not os.path.exists('wishlist.db'):
    with app.app_context():
        db.create_all()

# ----- CRUD Endpoints for Categories -----
@app.route('/categories', methods=['GET'])
def get_categories():
    logger.info(f"Received {request.method} request at {request.path}")
    categories = Category.query.all()
    return jsonify([{'Id': category.Id, 'Name': category.Name} for category in categories])

@app.route('/categories/<int:id>', methods=['GET'])
def get_category(id):
    logger.info(f"Received {request.method} request at {request.path}")
    category = Category.query.get_or_404(id)
    return jsonify({'Id': category.Id, 'Name': category.Name})

@app.route('/categories', methods=['POST'])
def add_category():
    logger.info(f"Received {request.method} request at {request.path}")
    data = request.get_json()
    new_category = Category(Name=data['Name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully'}), 201

@app.route('/categories/<int:id>', methods=['PUT'])
def update_category(id):
    logger.info(f"Received {request.method} request at {request.path}")
    category = Category.query.get_or_404(id)
    data = request.get_json()
    category.Name = data['Name']
    db.session.commit()
    return jsonify({'message': 'Category updated successfully'})

@app.route('/categories/<int:id>', methods=['DELETE'])
def delete_category(id):
    logger.info(f"Received {request.method} request at {request.path}")
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'})

# ----- CRUD Endpoints for VideoGames -----
@app.route('/videogames', methods=['GET'])
def get_videogames():
    logger.info(f"Received {request.method} request at {request.path}")
    videogames = VideoGame.query.all()
    return jsonify([
        {
            'Id': game.Id,
            'Title': game.Title,
            'ReleaseYear': game.ReleaseYear,
            'Category': game.Category.Name
        } for game in videogames
    ])

@app.route('/videogames/<int:id>', methods=['GET'])
def get_videogame(id):
    logger.info(f"Received {request.method} request at {request.path}")
    videogame = VideoGame.query.get_or_404(id)
    return jsonify({
        'Id': videogame.Id,
        'Title': videogame.Title,
        'ReleaseYear': videogame.ReleaseYear,
        'Category': videogame.Category.Name
    })

@app.route('/videogames', methods=['POST'])
def add_videogame():
    logger.info(f"Received {request.method} request at {request.path}")
    data = request.get_json()
    category = Category.query.get_or_404(data['CategoryId'])
    new_videogame = VideoGame(
        Title=data['Title'],
        ReleaseYear=data['ReleaseYear'],
        CategoryId=category.Id
    )
    db.session.add(new_videogame)
    db.session.commit()
    return jsonify({'message': 'Video game added successfully'}), 201

@app.route('/videogames/<int:id>', methods=['PUT'])
def update_videogame(id):
    logger.info(f"Received {request.method} request at {request.path}")
    videogame = VideoGame.query.get_or_404(id)
    data = request.get_json()
    videogame.Title = data['Title']
    videogame.ReleaseYear = data['ReleaseYear']
    videogame.CategoryId = data['CategoryId']
    db.session.commit()
    return jsonify({'message': 'Video game updated successfully'})

@app.route('/videogames/<int:id>', methods=['DELETE'])
def delete_videogame(id):
    logger.info(f"Received {request.method} request at {request.path}")
    videogame = VideoGame.query.get_or_404(id)
    db.session.delete(videogame)
    db.session.commit()
    return jsonify({'message': 'Video game deleted successfully'})

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
