from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Conversation(db.Model):
    """Model to store chat conversations"""
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.Text, nullable=False)
    bot_response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Conversation {self.id}: {self.user_input[:30]}...>'
    
    def to_dict(self):
        """Convert conversation to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'user_input': self.user_input,
            'bot_response': self.bot_response,
            'timestamp': self.timestamp.isoformat()
        }

def init_db(app):
    """Initialize database with Flask app"""
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
def save_conversation(user_input, bot_response):
    """Save a conversation to the database"""
    conversation = Conversation(
        user_input=user_input,
        bot_response=bot_response
    )
    db.session.add(conversation)
    db.session.commit()
    return conversation

def get_all_conversations():
    """Retrieve all conversations from the database"""
    return Conversation.query.order_by(Conversation.timestamp.desc()).all()

def get_recent_conversations(limit=10):
    """Get recent conversations with a limit"""
    return Conversation.query.order_by(Conversation.timestamp.desc()).limit(limit).all()