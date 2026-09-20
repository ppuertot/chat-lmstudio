// Simple client-side script for the chat UI
const chatDiv = document.getElementById('chat');
const inputEl = document.getElementById('input');
const sendBtn = document.getElementById('send');

function addMessage(text, type) {
    const msgDiv = document.createElement('div');
    msgDiv.className = 'msg ' + type;
    msgDiv.textContent = text;
    chatDiv.appendChild(msgDiv);
    chatDiv.scrollTop = chatDiv.scrollHeight; // scroll to bottom
}

async function sendMessage() {
    const message = inputEl.value.trim();
    if (!message) return;
    addMessage(message, 'user');
    inputEl.value = '';
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        if (!response.ok) throw new Error('Network error');
        const data = await response.json();
        addMessage(data.response, 'bot');
    } catch (err) {
        addMessage('Error: ' + err.message, 'bot');
    }
}

sendBtn.addEventListener('click', sendMessage);
inputEl.addEventListener('keydown', e => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); } });
