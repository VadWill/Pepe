# Restaurant AI Assistant

A Streamlit web application that serves as an AI assistant for restaurants, capable of answering questions about the menu and taking orders.

## Features
- Interactive chat interface
- Menu item information lookup
- Order taking functionality
- Natural language processing for customer interactions
- Vegetarian options filtering

## Local Development
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app locally:
```bash
streamlit run app.py
```

## Deployment to Streamlit.io
1. Create a GitHub repository and push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. Go to [Streamlit.io](https://streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository and branch
6. Set the main file path to `app.py`
7. Click "Deploy"

## Usage
The assistant can handle queries such as:
- "What's on the menu?"
- "Tell me about the pizza"
- "I'd like to order a burger"
- "What are your vegetarian options?"

## Note
This is a simple demonstration project. The menu and responses are predefined for demonstration purposes. 