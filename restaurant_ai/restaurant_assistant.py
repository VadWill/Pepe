import nltk
import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from colorama import Fore, Style, init
import re

# Initialize colorama for colored output
init()

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

# Menu data
MENU = {
    "appetizers": {
        "garlic bread": {
            "price": 5.99,
            "description": "Freshly baked bread with garlic butter and herbs",
            "vegetarian": True
        },
        "wings": {
            "price": 10.99,
            "description": "Crispy chicken wings with choice of sauce (buffalo, BBQ, or honey garlic)",
            "vegetarian": False
        },
        "soup": {
            "price": 6.99,
            "description": "Soup of the day served with crackers",
            "vegetarian": True
        }
    },
    "main_courses": {
        "burger": {
            "price": 14.99,
            "description": "1/3 lb beef patty with lettuce, tomato, onion, and special sauce",
            "vegetarian": False
        },
        "pizza": {
            "price": 16.99,
            "description": "12-inch pizza with your choice of 3 toppings",
            "vegetarian": True
        },
        "pasta": {
            "price": 13.99,
            "description": "Spaghetti with marinara sauce and garlic bread",
            "vegetarian": True
        }
    },
    "desserts": {
        "cheesecake": {
            "price": 7.99,
            "description": "New York style cheesecake with berry compote",
            "vegetarian": True
        },
        "ice_cream": {
            "price": 5.99,
            "description": "Three scoops of vanilla, chocolate, or strawberry",
            "vegetarian": True
        }
    }
}

class RestaurantAssistant:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.current_order = []

    def process_input(self, user_input):
        # Tokenize and lemmatize input
        tokens = word_tokenize(user_input.lower())
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token not in self.stop_words]
        
        # Check for common patterns
        if any(word in tokens for word in ['menu', 'offer', 'have']):
            return self.show_menu()
        elif 'order' in tokens:
            return self.process_order(user_input)
        elif 'vegetarian' in tokens:
            return self.show_vegetarian_options()
        elif any(item in ' '.join(tokens) for item in self.get_all_items()):
            return self.item_info(user_input)
        else:
            return self.get_help_message()

    def show_menu(self):
        menu_text = f"{Fore.GREEN}=== MENU ===\n{Style.RESET_ALL}"
        for category, items in MENU.items():
            menu_text += f"\n{Fore.YELLOW}{category.upper()}{Style.RESET_ALL}\n"
            for item_name, details in items.items():
                menu_text += f"{item_name.title()}: ${details['price']:.2f}\n"
                menu_text += f"  {details['description']}\n"
        return menu_text

    def process_order(self, user_input):
        # Extract items from user input
        items = self.get_all_items()
        ordered_items = [item for item in items if item in user_input.lower()]
        
        if not ordered_items:
            return "I couldn't identify what you'd like to order. Please specify items from our menu."
        
        self.current_order.extend(ordered_items)
        return f"I've added {', '.join(ordered_items)} to your order. Would you like anything else?"

    def show_vegetarian_options(self):
        veg_options = f"{Fore.GREEN}Vegetarian Options:{Style.RESET_ALL}\n"
        for category, items in MENU.items():
            for item_name, details in items.items():
                if details['vegetarian']:
                    veg_options += f"{item_name.title()}: {details['description']}\n"
        return veg_options

    def item_info(self, user_input):
        for category, items in MENU.items():
            for item_name, details in items.items():
                if item_name in user_input.lower():
                    return (f"{Fore.CYAN}{item_name.title()}{Style.RESET_ALL}\n"
                           f"Price: ${details['price']:.2f}\n"
                           f"Description: {details['description']}\n"
                           f"Vegetarian: {details['vegetarian']}")
        return "I couldn't find information about that item. Please check our menu."

    def get_all_items(self):
        items = []
        for category in MENU.values():
            items.extend(category.keys())
        return items

    def get_help_message(self):
        return """I can help you with:
1. Showing the menu (try "What's on the menu?")
2. Providing item information (try "Tell me about the pizza")
3. Taking orders (try "I'd like to order a burger")
4. Showing vegetarian options (try "What are your vegetarian options?")"""

def main():
    assistant = RestaurantAssistant()
    print(f"{Fore.GREEN}Welcome to our restaurant! How can I help you today?{Style.RESET_ALL}")
    print(assistant.get_help_message())
    
    while True:
        user_input = input(f"\n{Fore.BLUE}You:{Style.RESET_ALL} ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print(f"{Fore.GREEN}Thank you for visiting! Goodbye!{Style.RESET_ALL}")
            break
            
        response = assistant.process_input(user_input)
        print(f"\n{Fore.GREEN}Assistant:{Style.RESET_ALL} {response}")

if __name__ == "__main__":
    main() 