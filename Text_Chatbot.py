import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download required NLTK data (run this once)
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

class SimpleChatbot:
    def __init__(self):
        self.name = "Buddy"
        self.stop_words = set(stopwords.words('english'))
        
        # Predefined responses for different topics
        self.responses = {
            'greeting': [
                "Hello! How are you doing today?",
                "Hi there! Nice to meet you!",
                "Hey! What's up?",
                "Hello! How can I help you today?"
            ],
            'goodbye': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice talking to you!",
                "Farewell! Hope to chat again soon!"
            ],
            'how_are_you': [
                "I'm doing great, thanks for asking! How about you?",
                "I'm good! Just here chatting with awesome people like you!",
                "I'm fantastic! Thanks for asking. How are you feeling?",
                "I'm doing well! What about you?"
            ],
            'name': [
                f"My name is {self.name}! What's your name?",
                f"I'm {self.name}, your friendly chatbot! What should I call you?",
                f"You can call me {self.name}! What's your name?"
            ],
            'weather': [
                "I can't check the weather, but I hope it's nice where you are!",
                "Weather talk, huh? I hope you're having good weather!",
                "I wish I could tell you about the weather! Is it nice outside?"
            ],
            'age': [
                "I'm ageless! I exist in the digital world. How old are you?",
                "Age is just a number for me! I was created recently though.",
                "I don't really have an age, but I'm pretty new to this world!"
            ],
            'hobby': [
                "I love chatting with people! What do you enjoy doing?",
                "Talking to interesting people like you is my favorite thing!",
                "I enjoy learning about people! What are your hobbies?"
            ],
            'compliment': [
                "Thank you! You're very kind!",
                "That's so sweet of you to say!",
                "You're pretty awesome yourself!",
                "Thanks! You made my day!"
            ],
            'help': [
                "I'm here to chat and keep you company! What's on your mind?",
                "I can talk about almost anything! What would you like to discuss?",
                "I'm here to listen and chat! Tell me what's happening with you."
            ],
            'default': [
                "That's interesting! Tell me more about that.",
                "I see! What do you think about that?",
                "Hmm, that sounds cool! Can you explain more?",
                "That's fascinating! I'd love to hear more.",
                "Really? That's quite something! What else?",
                "I understand! What's your opinion on that?"
            ]
        }
        
        # Keywords for pattern matching
        self.patterns = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
            'goodbye': ['bye', 'goodbye', 'see you', 'farewell', 'take care', 'quit', 'exit'],
            'how_are_you': ['how are you', 'how do you feel', 'how are you doing'],
            'name': ['your name', 'who are you', 'what is your name', 'tell me your name'],
            'weather': ['weather', 'sunny', 'rainy', 'cold', 'hot', 'temperature'],
            'age': ['how old', 'your age', 'age'],
            'hobby': ['hobby', 'hobbies', 'what do you like', 'favorite', 'enjoy'],
            'compliment': ['nice', 'good', 'great', 'awesome', 'cool', 'amazing', 'smart'],
            'help': ['help', 'assist', 'support', 'what can you do']
        }

    def clean_text(self, text):
        """Clean and prepare text for processing"""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stop words
        tokens = [word for word in tokens if word not in self.stop_words]
        return tokens

    def find_intent(self, user_input):
        """Find what the user wants to talk about"""
        cleaned_input = user_input.lower()
        
        # Check each pattern category
        for intent, keywords in self.patterns.items():
            for keyword in keywords:
                if keyword in cleaned_input:
                    return intent
        
        return 'default'

    def get_response(self, user_input):
        """Get appropriate response based on user input"""
        intent = self.find_intent(user_input)
        return random.choice(self.responses[intent])

    def chat(self):
        """Main chat function"""
        print(f"Hi! I'm {self.name}, your friendly chatbot!")
        print("Type 'quit' or 'exit' when you want to stop chatting.")
        print("-" * 50)
        
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"{self.name}: {random.choice(self.responses['goodbye'])}")
                break
            
            # Skip empty input
            if not user_input:
                print(f"{self.name}: Please say something! I'm here to chat.")
                continue
            
            # Get and display response
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

# Create and start the chatbot
def main():
    print("Starting chatbot...")
    bot = SimpleChatbot()
    bot.chat()

if __name__ == "__main__":
    main()