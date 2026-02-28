/* ========================================
   CALM CHAT - INTERACTIVE SCRIPT
   Handles messaging, animations, and user interaction
   ======================================== */

// DOM Elements
const messagesContainer = document.getElementById('messagesContainer');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');
const typingIndicator = document.getElementById('typingIndicator');

// Backend API URL
const BACKEND_URL = 'https://chatbuddy-7i8s.onrender.com';

// ========================================
// EVENT LISTENERS
// ========================================

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', handleKeyPress);
userInput.addEventListener('input', autoResizeTextarea);

// ========================================
// SEND MESSAGE FUNCTION (ASYNC)
// ========================================

async function sendMessage() {
    const message = userInput.value.trim();

    if (message === '') return;

    // Disable input while sending
    sendBtn.disabled = true;
    userInput.disabled = true;

    // Display user message
    displayUserMessage(message);

    // Clear input
    userInput.value = '';
    userInput.style.height = 'auto';

    // Show typing indicator
    showTypingIndicator();

    try {
        // Call actual backend API
        const response = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        hideTypingIndicator();
        displayBotMessage(data.reply);

    } catch (error) {
        hideTypingIndicator();
        console.error('Error:', error);
        displayBotMessage(
            "I'm having a moment of difficulty connecting. Please check if the backend is running and try again."
        );
    } finally {
        // Re-enable input
        sendBtn.disabled = false;
        userInput.disabled = false;
        userInput.focus();
    }
}

// ========================================
// DISPLAY MESSAGES
// ========================================

function displayUserMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'user-messages-wrapper';
    
    const bubble = document.createElement('div');
    bubble.className = 'message-bubble user-message';
    bubble.textContent = message;
    
    messageDiv.appendChild(bubble);
    messagesContainer.appendChild(messageDiv);
    
    scrollToBottom();
}

function displayBotMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'welcome-message';
    
    const avatar = document.createElement('div');
    avatar.className = 'bot-avatar';
    avatar.textContent = '🌿';
    
    const bubble = document.createElement('div');
    bubble.className = 'message-bubble bot-message';
    bubble.textContent = message;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(bubble);
    messagesContainer.appendChild(messageDiv);
    
    scrollToBottom();
}

function showTypingIndicator() {
    typingIndicator.style.display = 'flex';
    scrollToBottom();
}

function hideTypingIndicator() {
    typingIndicator.style.display = 'none';
}

// ========================================
// KEYBOARD SHORTCUTS
// ========================================

function handleKeyPress(event) {
    // Ctrl+Enter to send (Windows/Linux)
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
}

// ========================================
// AUTO-RESIZE TEXTAREA
// ========================================

function autoResizeTextarea() {
    userInput.style.height = 'auto';
    const newHeight = Math.min(userInput.scrollHeight, 120);
    userInput.style.height = newHeight + 'px';
}

// ========================================
// AUTO-SCROLL TO BOTTOM
// ========================================

function scrollToBottom() {
    setTimeout(() => {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 0);
}

// ========================================
// KEYBOARD SHORTCUTS
// ========================================

function handleKeyPress(event) {
    // Ctrl+Enter to send (Windows/Linux)
    if ((event.ctrlKey || event.metaKey) && event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
}

// ========================================
// AUTO-RESIZE TEXTAREA
// ========================================

function autoResizeTextarea() {
    userInput.style.height = 'auto';
    const newHeight = Math.min(userInput.scrollHeight, 120);
    userInput.style.height = newHeight + 'px';
}

// ========================================
// AUTO-SCROLL TO BOTTOM
// ========================================

function scrollToBottom() {
    setTimeout(() => {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }, 0);
}

// ========================================
// INITIALIZATION
// ========================================

// Focus on input field when page loads
window.addEventListener('load', () => {
    userInput.focus();
    console.log('💚 Calm Chat connected to:', BACKEND_URL);
});

// Prevent text selection of decorative elements
document.querySelectorAll('.decoration').forEach(el => {
    el.style.userSelect = 'none';
});

console.log('💚 Calm Chat is ready. Backend: ' + BACKEND_URL);
