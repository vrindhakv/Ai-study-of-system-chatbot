from config import load_model

model = load_model()

def get_response(user_input, messages):
    try:
        # Convert our memory format to Gemini's history format
        formatted_history = []
        
        # app.py already added the latest user_input to messages. 
        # So we use all messages EXCEPT the last one as history.
        for msg in messages[:-1]:
            role = "user" if msg["role"] == "user" else "model"
            formatted_history.append({"role": role, "parts": [msg["content"]]})
            
        # Start a chat session with the historical context
        chat = model.start_chat(history=formatted_history)
        
        # Send the newest message
        response = chat.send_message(user_input)
        
        return response.text

    except Exception as e:
        return f"Error: {e}"