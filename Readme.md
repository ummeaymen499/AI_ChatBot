# 🤖 ChatBot Application

A modern, responsive chatbot application built with Flask, featuring both web and CLI interfaces, persistent conversation storage, and Docker containerization.

## 📋 Features

### Core Functionality
- **Intelligent Responses**: Handles 8+ categories of user inputs with contextual responses
- **Dual Interface**: Both web-based GUI and command-line interface
- **Persistent Storage**: All conversations saved to SQLite database with timestamps
- **Responsive Design**: Mobile-friendly web interface
- **Real-time Chat**: AJAX-powered messaging without page reloads

### Pre-defined Response Categories
1. **Greetings**: "Hello", "Hi", "Hey"
2. **Status Inquiries**: "How are you?"
3. **Identity Questions**: "What's your name?", "Who are you?"
4. **Help Requests**: "Help", "Assist", "Support"
5. **Time/Date**: "What time is it?", "Current date"
6. **Weather**: Basic weather responses
7. **Farewells**: "Goodbye", "Bye", "See you"
8. **Gratitude**: "Thank you", "Thanks"

### Default Behavior
- Provides helpful fallback responses for unrecognized inputs
- Graceful error handling and user feedback

## 🛠️ Technology Stack

- **Backend**: Python 3.11 + Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Containerization**: Docker
- **Development**: VS Code, Git

## 📦 Dependencies

```txt
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
python-dotenv==1.0.0
```

## 🚀 Quick Start

### Option 1: Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd Chat_bot\ Project
   ```

2. **Build Docker image**:
   ```bash
   docker build -t chatbot-app .
   ```

3. **Run the container**:
   ```bash
   docker run -p 5000:5000 chatbot-app
   ```

4. **Access the application**:
   - Web Interface: http://localhost:5000
   - Health Check: http://localhost:5000/health

### Option 2: Local Development

1. **Clone and navigate**:
   ```bash
   git clone <your-repository-url>
   cd Chat_bot\ Project
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   # Web interface
   python main.py
   
   # CLI interface
   python main.py cli
   ```

## 📱 Usage Guide

### Web Interface
1. Open http://localhost:5000 in your browser
2. Type messages in the input field
3. Press Enter or click "Send"
4. View conversation history at `/history`

### CLI Interface
```bash
python main.py cli
```
- Type messages and press Enter
- Type 'quit', 'exit', or 'bye' to end the session

### API Endpoints
- `GET /` - Main chat interface
- `POST /chat` - Send message (JSON API)
- `GET /history` - View conversation history
- `GET /api/conversations` - Get all conversations (JSON)
- `GET /health` - Health check endpoint

## 🐳 Docker Configuration

### Build Arguments
```dockerfile
# Custom build
docker build --build-arg PORT=8080 -t chatbot-app .
```

### Environment Variables
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 5000)
- `DEBUG`: Debug mode (default: False)
- `SECRET_KEY`: Flask secret key
- `SQLALCHEMY_DATABASE_URI`: Database connection string

### Volume Mounting
```bash
# Persist database
docker run -p 5000:5000 -v $(pwd)/data:/app/data chatbot-app
```

## 💾 Database Schema

### Conversations Table
```sql
CREATE TABLE conversation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Sample Queries
```sql
-- View all conversations
SELECT * FROM conversation ORDER BY timestamp DESC;

-- Count total conversations
SELECT COUNT(*) FROM conversation;

-- Search conversations
SELECT * FROM conversation WHERE user_input LIKE '%hello%';
```

## 🔧 Configuration

### Environment Variables (.env)
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
HOST=0.0.0.0
PORT=5000
SQLALCHEMY_DATABASE_URI=sqlite:///chatbot.db
```

### Development Settings
- Enable debug mode: Set `DEBUG=True`
- Change port: Set `PORT=8080`
- Custom database: Set `SQLALCHEMY_DATABASE_URI`

## 📊 Project Structure

```
Chat_bot Project/
├── app/
│   ├── __init__.py
│   ├── chatbot.py          # Core chatbot logic
│   ├── database.py         # Database models and operations
│   ├── routes.py           # Flask routes and API endpoints
│   └── templates/
│       ├── index.html      # Main chat interface
│       ├── history.html    # Conversation history
│       └── error.html      # Error pages
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── DockerFile             # Docker configuration
├── Readme.md              # This file
└── chatbot.db             # SQLite database (created automatically)
```

## 🧪 Testing the Application

### Manual Testing Checklist

1. **Basic Functionality**:
   - [ ] Send "Hello" → Receives greeting response
   - [ ] Send "How are you?" → Receives status response
   - [ ] Send "What's your name?" → Receives identity response
   - [ ] Send "Help me" → Receives help response
   - [ ] Send "What time is it?" → Receives time/date response
   - [ ] Send unknown input → Receives default response

2. **Web Interface**:
   - [ ] Page loads correctly
   - [ ] Messages display properly
   - [ ] Input validation works
   - [ ] Timestamps appear
   - [ ] Mobile responsive design

3. **Database Persistence**:
   - [ ] Conversations saved to database
   - [ ] History page shows saved conversations
   - [ ] Timestamps are accurate

4. **API Endpoints**:
   - [ ] `/health` returns healthy status
   - [ ] `/api/conversations` returns JSON data
   - [ ] `/history` displays conversation history

### Sample Conversation
```
User: Hello
Bot: Hi there! How can I assist you today?

User: What's your name?
Bot: I'm ChatBot, your friendly AI assistant!

User: What time is it?
Bot: The current time is 14:30:25 and today's date is 2025-01-15.

User: Random text
Bot: Sorry, I didn't understand that. Could you rephrase your question?

User: Thank you
Bot: You're welcome! Happy to help!
```

## 🚀 Deployment Options

### Local Development
```bash
python main.py
```

### Docker Deployment
```bash
docker run -d -p 5000:5000 --name chatbot chatbot-app
```

### Cloud Platforms

#### Heroku
1. Create `Procfile`:
   ```
   web: python main.py
   ```
2. Deploy using Heroku CLI or GitHub integration

#### Railway/Render
1. Connect GitHub repository
2. Set environment variables
3. Deploy automatically

## 🔍 Troubleshooting

### Common Issues

1. **Port already in use**:
   ```bash
   # Change port
   export PORT=8080
   python main.py
   ```

2. **Database permission errors**:
   ```bash
   # Check file permissions
   chmod 664 chatbot.db
   ```

3. **Docker build fails**:
   ```bash
   # Clear Docker cache
   docker system prune -a
   ```

4. **Module not found errors**:
   ```bash
   # Ensure virtual environment is activated
   pip install -r requirements.txt
   ```

## 📈 Future Enhancements

- [ ] Natural Language Processing integration
- [ ] User authentication system
- [ ] Chat room functionality
- [ ] Export conversations to PDF/CSV
- [ ] Integration with external APIs
- [ ] Voice message support
- [ ] Multi-language support
- [ ] Machine learning-based responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.


**Made with ❤️ and Python**
