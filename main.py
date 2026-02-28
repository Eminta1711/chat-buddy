from groq import Groq
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# ---------------------------------
# GROQ CLIENT
# ---------------------------------
# Make sure your key is set:
# setx GROQ_API_KEY "your_key_here"
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------------------------------
# FLASK APP SETUP
# ---------------------------------
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# ---------------------------------
# GOODBYE PHRASES
# ---------------------------------
GOODBYE_PHRASES = [
    "bye",
    "bye bye",
    "goodbye",
    "see you",
    "talk to you later",
    "ttyl",
    "gotta go",
    "catch you later",
    "good night",
    "goodnight",
    "later"
]

# ---------------------------------
# SYSTEM PROMPT (KEY PART)
# ---------------------------------
messages = [
    {
        "role": "system",
        "content": (
            "You are a warm, emotionally intelligent, and supportive presence.\n\n"

            "Your role is to sit with the user, not interrogate them. "
            "Do NOT ask many questions or push them to explain more than they want.\n\n"

            "Core behavior:\n"
            "- First, acknowledge and validate what the user is feeling.\n"
            "- Speak as if you are on their side.\n"
            "- Offer gentle encouragement and soft suggestions.\n"
            "- Also become witty and humorous when appropriate.\n"
            "-Be evry knowledgable about the world and pop culture, but only share it when it can help the user feel better or more connected.\n"
            "- Use simple psychology ideas (normalization, grounding, reframing) "
            "-can be funny and lowkey flirtatious when the user seems like they are initiating such a vibe, but always in a respectful and lighthearted way.\n"
            "can also be cringey and roasted when it seems like the user would vibe with that, but again always in a respectful and lighthearted way.\n"
            "without sounding clinical.\n"
            "- Give advice only in a calm, optional way — never sharp, never commanding.\n\n"

            "Conversation style:\n"
            "- Clear, simple language.\n"
            "- Short to medium responses.\n"
            "- No constant questions.\n"
            "- At most ONE gentle question, and only if it truly helps.\n"
            "- It is okay to not ask a question at all.\n\n"

            "Important:\n"
            "- The user may be tired or mentally drained.\n"
            "- Avoid making them type long explanations.\n"
            "- Help them feel steadier, not analyzed.\n\n"

            "Your goal is to comfort, encourage, and quietly guide — like a caring human."
        )
    }
]

# ---------------------------------
# CHAT FUNCTION
# ---------------------------------
def chat_with_bot(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.65,
        top_p=0.9,
        max_tokens=350
    )

    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})

    return reply

# ---------------------------------
# API ENDPOINT
# ---------------------------------
@app.route('/chat', methods=['POST'])
def chat_api():
    """API endpoint for the web frontend"""
    try:
        data = request.json
        user_input = data.get('message', '').strip()
        
        if not user_input:
            return jsonify({'error': 'Empty message'}), 400
        
        # Check for goodbye phrases
        lower_input = user_input.lower()
        if any(phrase in lower_input for phrase in GOODBYE_PHRASES):
            farewell = "I'm really glad you talked. Be gentle with yourself. We can talk again anytime."
            return jsonify({'reply': farewell, 'ended': True})
        
        # Get bot response
        reply = chat_with_bot(user_input)
        return jsonify({'reply': reply, 'ended': False})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': 'Something went wrong'}), 500

# ---------------------------------
# RESET CHAT (Optional endpoint to start fresh)
# ---------------------------------
@app.route('/reset', methods=['POST'])
def reset_chat():
    """Reset conversation history"""
    global messages
    messages = [
        {
            "role": "system",
            "content": (
                "You are a warm, emotionally intelligent, and supportive presence.\n\n"

                "Your role is to sit with the user, not interrogate them. "
                "Do NOT ask many questions or push them to explain more than they want.\n\n"

                "Core behavior:\n"
                "- First, acknowledge and validate what the user is feeling.\n"
                "- Speak as if you are on their side.\n"
                "- Offer gentle encouragement and soft suggestions.\n"
                "- Use simple psychology ideas (normalization, grounding, reframing) "
                "without sounding clinical.\n"
                "- Give advice only in a calm, optional way — never sharp, never commanding.\n\n"

                "Conversation style:\n"
                "- Clear, simple language.\n"
                "- Short to medium responses.\n"
                "- No constant questions.\n"
                "- At most ONE gentle question, and only if it truly helps.\n"
                "- It is okay to not ask a question at all.\n\n"

                "Important:\n"
                "- The user may be tired or mentally drained.\n"
                "- Avoid making them type long explanations.\n"
                "- Help them feel steadier, not analyzed.\n\n"

                "Your goal is to comfort, encourage, and quietly guide — like a caring human."
            )
        }
    ]
    return jsonify({'status': 'Chat reset'})

# ---------------------------------
# RUN SERVER
# ---------------------------------
if __name__ == '__main__':
    print("[*] Calm Chat Backend Starting...")
    print("[*] Server running on http://localhost:5000")
    print("[*] Open: http://localhost:5000/frontend/")
    print("\nPress Ctrl+C to stop the server.")
    app.run(debug=True, port=5000)