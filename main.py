#!/usr/bin/env python3
"""
ChatBot Application - Main Entry Point

This is a simple chatbot application built with Flask that provides:
- Web interface for chatting with the bot
- CLI interface for command-line interactions
- SQLite database for conversation persistence
- Docker containerization support

Author: ChatBot Development Team
Date: 2025
"""

import os
import sys
from app.routes import create_app
from app.chatbot import run_cli_chatbot

def main():
    """Main entry point for the application"""
    
    # Check if running in CLI mode
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        print("Starting ChatBot in CLI mode...")
        run_cli_chatbot()
        return
    
    # Create Flask app
    app = create_app()
    
    # Get configuration from environment variables
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print("=" * 60)
    print("🤖 ChatBot Application Starting...")
    print("=" * 60)
    print(f"📱 Web Interface: http://{host}:{port}")
    print(f"📊 Chat History: http://{host}:{port}/history")
    print(f"🔍 Health Check: http://{host}:{port}/health")
    print(f"📋 API Endpoint: http://{host}:{port}/api/conversations")
    print("=" * 60)
    print("💡 Tips:")
    print("   - Try saying 'Hello', 'Help', or 'What time is it?'")
    print("   - All conversations are saved to SQLite database")
    print("   - Use Ctrl+C to stop the server")
    print("=" * 60)
    
    if debug:
        print("⚠️  DEBUG MODE ENABLED - Not for production use!")
        print("=" * 60)
    
    try:
        # Start the Flask development server
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True
        )
    except KeyboardInterrupt:
        print("\n👋 ChatBot shutting down gracefully...")
    except Exception as e:
        print(f"❌ Error starting ChatBot: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()