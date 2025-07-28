from flask import Flask, render_template, request, jsonify, redirect, url_for
from .chatbot import SimpleChatbot
from .database import init_db, save_conversation, get_recent_conversations, get_all_conversations
import os

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///chatbot.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    init_db(app)
    
    # Initialize chatbot
    chatbot = SimpleChatbot()
    
    @app.route('/')
    def index():
        """Main chat interface"""
        return render_template('index.html')
    
    @app.route('/chat', methods=['POST'])
    def chat():
        """Handle chat messages via AJAX"""
        try:
            data = request.get_json()
            user_input = data.get('message', '').strip()
            
            if not user_input:
                return jsonify({
                    'success': False,
                    'error': 'Message cannot be empty'
                }), 400
            
            # Get bot response
            bot_response = chatbot.get_response(user_input)
            
            # Save conversation to database
            conversation = save_conversation(user_input, bot_response)
            
            return jsonify({
                'success': True,
                'user_message': user_input,
                'bot_response': bot_response,
                'timestamp': conversation.timestamp.strftime('%H:%M:%S')
            })
            
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Server error: {str(e)}'
            }), 500
    
    @app.route('/history')
    def history():
        """View conversation history"""
        conversations = get_recent_conversations(50)  # Get last 50 conversations
        return render_template('history.html', conversations=conversations)
    
    @app.route('/api/conversations')
    def api_conversations():
        """API endpoint to get all conversations"""
        try:
            conversations = get_all_conversations()
            return jsonify({
                'success': True,
                'conversations': [conv.to_dict() for conv in conversations]
            })
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @app.route('/health')
    def health_check():
        """Health check endpoint for Docker"""
        return jsonify({
            'status': 'healthy',
            'message': 'Chatbot is running successfully!'
        })
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return render_template('error.html', 
                             error_code=404, 
                             error_message="Page not found"), 404
    
    @app.errorhandler(500)
    def server_error(error):
        """Handle 500 errors"""
        return render_template('error.html', 
                             error_code=500, 
                             error_message="Internal server error"), 500
    
    return app