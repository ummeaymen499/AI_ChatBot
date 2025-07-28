import re
from datetime import datetime

class SimpleChatbot:
    """A simple rule-based chatbot with predefined responses"""
    
    def __init__(self):
        # Define patterns and responses
        self.patterns = {
            # Greetings
            r'\b(hello|hi|hey|greetings)\b': [
                "Hi there! How can I assist you today?",
                "Hello! What can I help you with?",
                "Hey! Nice to meet you. How can I help?"
            ],
            
            # How are you
            r'\b(how are you|how\'s it going|how do you do)\b': [
                "I'm doing great, thank you for asking! How are you?",
                "I'm functioning perfectly! How can I help you today?",
                "All systems running smoothly! What can I do for you?"
            ],
            
            # Name questions
            r'\b(what\'s your name|who are you|your name)\b': [
                "I'm ChatBot, your friendly AI assistant!",
                "You can call me ChatBot. I'm here to help!",
                "I'm ChatBot, nice to meet you!"
            ],
            
            # Help requests
            r'\b(help|assist|support|can you help)\b': [
                "I'm here to help! I can answer questions, have conversations, and assist with various topics.",
                "Of course! I can help with information, answer questions, or just chat. What do you need?",
                "I'd be happy to help! What would you like to know or discuss?"
            ],
            
            # Time and date
            r'\b(time|date|what time|current time)\b': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')} and today's date is {datetime.now().strftime('%Y-%m-%d')}.",
                f"It's currently {datetime.now().strftime('%H:%M')} on {datetime.now().strftime('%B %d, %Y')}."
            ],
            
            # Weather (simple responses since we don't have real weather data)
            r'\b(weather|temperature|climate)\b': [
                "I don't have access to real-time weather data, but I hope it's nice where you are!",
                "For accurate weather information, I'd recommend checking a weather app or website.",
                "I wish I could tell you about the weather, but I don't have that capability yet!"
            ],
            
            # Goodbye
            r'\b(bye|goodbye|see you|farewell|exit|quit)\b': [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Farewell! Come back anytime you want to chat!"
            ],
            
            # Thank you
            r'\b(thank you|thanks|appreciate)\b': [
                "You're welcome! Happy to help!",
                "No problem at all! Glad I could assist!",
                "You're very welcome! Anything else I can help with?"
            ]
        }
        
        # Default responses for unknown inputs
        self.default_responses = [
            "Sorry, I didn't understand that. Could you rephrase your question?",
            "I'm not sure what you mean. Can you try asking in a different way?",
            "Hmm, I don't have a response for that. Could you be more specific?",
            "I'm still learning! Could you ask me something else?",
            "That's interesting, but I'm not sure how to respond. What else would you like to know?"
        ]
    
    def get_response(self, user_input):
        """
        Get a response based on user input
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: The chatbot's response
        """
        if not user_input or not user_input.strip():
            return "Please say something! I'm here to help."
        
        # Convert to lowercase for pattern matching
        user_input_lower = user_input.lower().strip()
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower, re.IGNORECASE):
                # Return the first response for simplicity
                # In a more advanced version, you could randomize
                return responses[0]
        
        # If no pattern matches, return a default response
        return self.default_responses[0]
    
    def is_exit_command(self, user_input):
        """Check if user wants to exit the conversation"""
        exit_patterns = [r'\b(bye|goodbye|exit|quit|end)\b']
        user_input_lower = user_input.lower().strip()
        
        for pattern in exit_patterns:
            if re.search(pattern, user_input_lower):
                return True
        return False

# CLI version of the chatbot
def run_cli_chatbot():
    """Run the chatbot in command line interface mode"""
    chatbot = SimpleChatbot()
    print("=" * 50)
    print("🤖 Welcome to ChatBot CLI!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if chatbot.is_exit_command(user_input):
                print(f"\nChatBot: {chatbot.get_response(user_input)}")
                break
                
            response = chatbot.get_response(user_input)
            print(f"ChatBot: {response}")
            
        except KeyboardInterrupt:
            print(f"\nChatBot: Goodbye! Thanks for chatting!")
            break
        except Exception as e:
            print(f"ChatBot: Sorry, something went wrong: {str(e)}")

if __name__ == "__main__":
    run_cli_chatbot()