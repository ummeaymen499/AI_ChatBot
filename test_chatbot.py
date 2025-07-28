#!/usr/bin/env python3
"""
Test script for ChatBot application
"""

import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_chatbot_import():
    """Test importing chatbot modules"""
    try:
        from app.chatbot import SimpleChatbot
        from app.database import Conversation, init_db, save_conversation
        from app.routes import create_app
        print("✅ All modules imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_chatbot_responses():
    """Test chatbot responses"""
    try:
        from app.chatbot import SimpleChatbot
        
        bot = SimpleChatbot()
        
        # Test predefined responses
        test_cases = [
            ("hello", "Hi there! How can I assist you today?"),
            ("how are you", "I'm doing great, thank you for asking! How are you?"),
            ("what's your name", "I'm ChatBot, your friendly AI assistant!"),
            ("help", "I'm here to help! I can answer questions, have conversations, and assist with various topics."),
            ("random unknown input", "Sorry, I didn't understand that. Could you rephrase your question?")
        ]
        
        print("🧪 Testing chatbot responses:")
        for user_input, expected_start in test_cases:
            response = bot.get_response(user_input)
            if response == expected_start:
                print(f"   ✅ '{user_input}' -> Correct response")
            else:
                print(f"   ⚠️  '{user_input}' -> '{response}'")
        
        return True
    except Exception as e:
        print(f"❌ Chatbot test error: {e}")
        return False

def test_flask_app():
    """Test Flask app creation"""
    try:
        from app.routes import create_app
        
        app = create_app()
        print("✅ Flask app created successfully!")
        
        # Test routes exist
        with app.app_context():
            print("✅ App context working!")
            
        return True
    except Exception as e:
        print(f"❌ Flask app test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🤖 ChatBot Application Test Suite")
    print("=" * 40)
    
    tests = [
        test_chatbot_import,
        test_chatbot_responses, 
        test_flask_app
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
    
    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your chatbot is ready to run.")
        print("\n🚀 To start the application:")
        print("   Web interface: python main.py")
        print("   CLI interface: python main.py cli")
        print("   Docker build:  docker build -t chatbot-app .")
        print("   Docker run:    docker run -p 5000:5000 chatbot-app")
    else:
        print("⚠️  Some tests failed. Please check the error messages above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
