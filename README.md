# 🌿 Calm Chat - Emotionally Intelligent Chatbot

A warm, supportive chatbot powered by Groq's Llama 3.3-70B with a beautiful, calm web interface. Designed to make users feel heard, validated, and emotionally safe.

## ✨ Features

- **Emotionally Intelligent**: System-prompt based to be warm, validating, and supportive
- **Modern Web Interface**: Beautiful, minimal design with smooth animations
- **Real-time Responses**: Uses Groq API (llama-3.3-70b-versatile)
- **Conversation Memory**: Remembers context across messages
- **Responsive Design**: Works on desktop, tablet, and mobile
- **No Framework Bloat**: Vanilla HTML, CSS, JavaScript frontend

## 🎯 Design Philosophy

The interface is built to feel **calm, safe, and non-judgmental**:
- Soft pastel colors (lavender, light blue, warm beige)
- Gentle animations (floating shapes, smooth fades)
- Rounded message bubbles with soft shadows
- Cute decorative elements that feel comforting
- Zero aggressive motion or pop-ups

## 📁 Project Structure

```
chatbot/
├── main.py                      # Flask backend + Groq integration
├── frontend/
│   ├── index.html              # Chat interface
│   ├── style.css               # Styling & animations
│   ├── script.js               # Frontend logic
│   └── README.md               # Frontend docs
├── .gitignore                  # Git ignore rules
└── requirements.txt            # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- GROQ API Key ([Get one free here](https://console.groq.com))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/chatbot.git
cd chatbot
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**
```bash
pip install groq flask flask-cors
```

4. **Set your Groq API Key** (Windows)
```bash
setx GROQ_API_KEY "your_actual_key_here"
```

Or (Mac/Linux):
```bash
export GROQ_API_KEY="your_actual_key_here"
```

### Running the Application

**Terminal 1 - Start Backend (Port 8000)**
```bash
python main.py
```

You should see:
```
🌿 Calm Chat Backend Starting...
📍 Server running on http://localhost:8000
```

**Terminal 2 - Start Frontend (Port 8001)**
```bash
cd frontend
python -m http.server 8001
```

**Then open your browser:**
- Visit: `http://localhost:8001`

## 💬 Usage

1. Type your message in the text field
2. Press **Ctrl+Enter** or click **Send**
3. The bot responds with warm, validating messages
4. Conversation history is maintained across messages
5. Type "bye" or "goodbye" to end the session

## 🤖 How It Works

### Backend (`main.py`)
- **Flask API**: Exposes `/chat` endpoint for frontend requests
- **Groq Integration**: Uses llama-3.3-70b-versatile for responses
- **System Prompt**: Carefully crafted to be emotionally intelligent
- **Conversation Memory**: Maintains message history for context

### Frontend
- **HTML**: Semantic structure with welcome message and typing indicator
- **CSS**: Gradient backgrounds, smooth animations, responsive design
- **JavaScript**: Async API calls, auto-scroll, keyboard shortcuts

## 📝 System Prompt (The Heart of It)

The bot is configured with a detailed system prompt that ensures:
- ✅ Validation of user feelings
- ✅ Warm, supportive tone
- ✅ Minimal questioning (max 1 gentle question)
- ✅ Simple, clear language
- ✅ No clinical or interrogative approach
- ✅ Optional, never commanding advice

## 🎨 Customization

### Change Bot Avatar
Edit `frontend/index.html` line ~41:
```html
<div class="bot-avatar">🌿</div>  <!-- Change emoji here -->
```

### Change Colors
Edit `frontend/style.css` and modify the gradient colors:
```css
.chat-header {
    background: linear-gradient(135deg, #d4b5f8 0%, #a8d8f0 100%);
}
```

### Adjust System Prompt
Edit `main.py` lines 37-60 to modify bot personality and behavior.

### Disable Background Animations
Edit `frontend/style.css` and hide `.floating-shapes`:
```css
.floating-shapes {
    display: none;
}
```

## 🔐 Security

**Before deploying to production:**

1. **Secure API Key**: Never commit your GROQ_API_KEY
2. **CORS Configuration**: Restrict origins to your domain
3. **Rate Limiting**: Add rate limits on the `/chat` endpoint
4. **Input Validation**: Validate/sanitize user messages
5. **HTTPS**: Always use HTTPS in production

## 📦 API Endpoints

### `/chat` (POST)
Send a message and get a bot response.

**Request:**
```json
{
  "message": "I'm feeling tired"
}
```

**Response:**
```json
{
  "reply": "That sounds really exhausting. It's okay to feel this way.",
  "ended": false
}
```

### `/reset` (POST)
Clear conversation history and start fresh.

**Response:**
```json
{
  "status": "Chat reset"
}
```

## 🌐 Deployment Options

### Option 1: Heroku
```bash
# Create Procfile in root
echo "web: python main.py" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Option 2: PythonAnywhere
Upload project and configure WSGI file to run Flask app.

### Option 3: Your Own Server
Use Gunicorn for production:
```bash
pip install gunicorn
gunicorn main:app
```

## 🐛 Troubleshooting

**Backend won't start?**
- ✅ Check API key is set: `echo $GROQ_API_KEY`
- ✅ Ensure Flask is installed: `pip install flask flask-cors`
- ✅ Port 8000 not in use

**Frontend shows connection error?**
- ✅ Verify backend is running
- ✅ Check both servers running in separate terminals
- ✅ Clear browser cache (Ctrl+F5)

**Slow responses?**
- ✅ Groq API latency (usually 1-3 seconds)
- ✅ Check internet connection
- ✅ Verify API quota not exceeded

**Messages not sending?**
- ✅ Open F12 developer console, check errors
- ✅ Ensure `/chat` endpoint running
- ✅ Check CORS enabled in Flask

## 📚 Technologies Used

- **Backend**: Python, Flask, Groq API
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **LLM**: Llama 3.3-70B (via Groq)
- **Styling**: CSS Gradients, Keyframe Animations

## 📄 License

MIT License - Feel free to use, modify, and distribute.

## 💚 Philosophy

This project exists on the belief that **AI should make us feel better, not worse**. Every design choice—from soft colors to gentle animations to warm system prompts—was made with the goal of creating a space where people feel:

- **Safe** to share what's on their mind
- **Heard** without being judged
- **Calm** without being rushed
- **Supported** in a human way

## 🤝 Contributing

Feel free to fork, modify, and improve! Suggestions for better system prompts, UI improvements, or features are welcome.

## 👋 Questions?

Check the `frontend/README.md` for more details about the web interface.

---

Made with 💚 for emotional well-being.

**Visit**: `http://localhost:8001` to chat!
