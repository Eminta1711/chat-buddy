# Calm Chat Frontend

A soothing, emotionally intelligent chatbot web interface built with vanilla HTML, CSS, and JavaScript.

## 📁 Project Structure

```
chatbot/
├── main.py                 # Your existing Python backend (Groq llama-3.3-70b)
├── .venv/                  # Your Python virtual environment
├──
frontend/                  # ← NEW: Frontend folder
│   ├── index.html         # Main chat interface
│   ├── style.css          # Styling & animations
│   ├── script.js          # Interactivity & messaging logic
│   └── README.md          # This file
```

## 🎨 Design Philosophy

The interface is designed to feel **calm, safe, and emotionally supportive**:

- **Color palette**: Soft lavender, light blue, warm beige, gentle pastels
- **Animations**: Smooth, gentle, never jarring
- **Typography**: Clean, readable, friendly but mature
- **Layout**: Minimalist, spacious, no clutter
- **Motion**: Subtle floating elements that don't distract

## ✨ Features

✅ Chat layout (user messages right, bot left)
✅ Smooth message fade-in animations
✅ Typing indicator with bouncing dots
✅ Auto-scroll to newest message
✅ Responsive mobile design
✅ Keyboard shortcut: **Ctrl+Enter** to send
✅ Auto-resizing message input field
✅ Cute emoji decorations with gentle animation
✅ Subtle floating background shapes
✅ Accessibility features (reduced motion support, focus states)

## 🚀 Quick Start

### Option 1: Open in Browser Directly
```bash
# Simply open the file in your browser:
frontend/index.html
```

### Option 2: Local Server (Recommended)
```bash
# Python (built-in):
cd frontend
python -m http.server 8000

# Then visit: http://localhost:8000
```

## 🔗 Connecting to Your Backend

Currently, the frontend uses **mock responses** for testing. To connect to your Python backend:

### Step 1: Set up your backend as a web API

In your `main.py`, add Flask or FastAPI to create an API endpoint:

**Option A: Using Flask** (simple)
```python
from flask import Flask, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ... your existing chatbot code ...

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Your existing chatbot logic here
    bot_response = get_bot_response(user_message)
    
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
```

**Option B: Using FastAPI** (modern)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os

app = FastAPI()

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    # Your existing chatbot logic
    bot_response = get_bot_response(msg.message)
    return {'reply': bot_response}
```

### Step 2: Enable Backend Connection in Frontend

In `script.js`, uncomment the API integration code at the bottom:

```javascript
// Around line 150-180, uncomment the getBackendResponse() function
// Then update sendMessage() to use: 
// const botReply = await getBackendResponse(message);
```

### Step 3: Install Backend Dependencies

```bash
pip install flask flask-cors
# OR
pip install fastapi uvicorn
```

### Step 4: Run Everything

Terminal 1 (Backend):
```bash
python main.py
```

Terminal 2 (Frontend):
```bash
cd frontend
python -m http.server 8000
```

Visit: `http://localhost:8000`

## 📝 Customization Guide

### Change Bot Avatar
In `index.html`, find:
```html
<div class="bot-avatar">🌿</div>
```
Replace `🌿` with any emoji you prefer (e.g., `💚`, `🤖`, `✨`)

### Change Welcome Message
In `index.html`, find the welcome message and edit:
```html
<p>Hello, I'm here to listen. Feel free to share...</p>
```

### Adjust Colors
In `style.css`, modify the gradient colors:
```css
.chat-header {
    background: linear-gradient(135deg, #d4b5f8 0%, #a8d8f0 100%);
}
```

Color palette used:
- Lavender: `#d4b5f8`
- Light Blue: `#a8d8f0`
- Soft Pink: `#ffd4e5`
- Very Light Purple: `#f0e3ff`
- Very Light Blue: `#e8f4f8`

### Adjust Animation Speed
In `style.css`, find animations like:
```css
animation: float 20s infinite ease-in-out;
```
Change `20s` to slower (`30s`) or faster (`10s`)

### Disable Background Animations
In `style.css`, add to `.floating-shapes`:
```css
.floating-shapes {
    display: none;
}
```

## ♿ Accessibility

The interface supports:
- Keyboard navigation (Tab, Enter)
- Focus indicators (visible outlines)
- Reduced motion preferences (users with vestibular issues)
- Screen reader friendly
- High contrast on text

## 🌐 Browser Support

Works on all modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📱 Mobile Responsive

The chat interface adapts to:
- Phones (320px and up)
- Tablets (600px and up)
- Desktops (700px+ optimal width)

On mobile, decorative elements hide automatically for better space.

## 🔒 Security Notes

**Before deploying to production:**

1. **CORS Setup**: Update `allow_origins` in your backend to specific domains
2. **API Key**: Never expose your `GROQ_API_KEY` in frontend code
3. **Rate Limiting**: Add rate limiting on your backend
4. **Input Validation**: Validate/sanitize user messages on backend
5. **HTTPS**: Always use HTTPS in production

## 🐛 Troubleshooting

**Messages not sending?**
- Check browser console for errors (F12)
- Make sure backend is running on correct port
- Check CORS settings in backend

**Styling looks weird?**
- Clear browser cache (Ctrl+F5)
- Try different browser
- Check if CSS file loads (F12 → Network tab)

**Bot responses are slow/timeout?**
- Check your Groq API key is valid
- Check internet connection
- Increase timeout in javascript if needed

## 📚 File Breakdown

### index.html
- Structure for chat interface
- Welcome message
- Input form
- Typing indicator
- Decorative elements
- Semantic HTML5

### style.css (390+ lines)
- Soft color gradients
- Smooth animations (fade-in, floating, bouncing)
- Message bubble styling
- Responsive grid layouts
- Accessibility features
- Mobile-first responsive design

### script.js (130+ lines)
- Message sending logic
- Auto-scroll functionality
- Keyboard shortcuts
- Mock responses (placeholder)
- API integration comments
- DOM manipulation

## 💚 Philosophy

This chatbot interface was built with the understanding that **design is emotional**. Every color, animation, and spacing choice was made to create a space where someone feels:

- **Safe** to share
- **Heard** and validated
- **Calm** and not rushed
- **Supported** without judgment

The interface mirrors your backend's warm, emotionally intelligent personality.

## 🚀 Next Steps

1. ✅ Frontend works with mock responses
2. 🔄 Connect to your Python backend
3. 📱 Deploy to GitHub Pages or a web server
4. 🎯 Add persistent chat history
5. 🔐 Add user authentication (optional)
6. 📊 Add analytics (optional)

## 📄 License

This frontend code is free to use, modify, and distribute. Keep your Python backend and Groq API key secure!

---

**Questions?** This code is designed to be readable and beginner-friendly. Check comments in each file for explanations.

**Want to customize further?** All code is vanilla JS/CSS—no build tools needed. Just edit, refresh, and see changes instantly!

🌿 Made with care for emotional well-being.
