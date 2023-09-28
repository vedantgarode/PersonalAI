// Get references to HTML elements
const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.getElementById('chat-messages');

// Function to append a message to the chat
function appendMessage(sender, message) {
  const messageElement = document.createElement('div');
  messageElement.className = `message ${sender === 'AI' ? 'ai-message' : 'user-message'}`;
  messageElement.textContent = `${sender}: ${message}`;
  chatMessages.appendChild(messageElement);
}

// Function to send user message to the API
async function sendMessageToAPI(message) {
  try {
    const response = await fetch('https://spartex.pythonanywhere.com/convo', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
    
    if (!response.ok) {
      throw new Error('API request failed');
    }

    const responseData = await response.json();
    return responseData.response;
  } catch (error) {
    console.error(error);
    return 'Error communicating with the API';
  }
}

// Event listener for the send button
sendButton.addEventListener('click', async () => {
  const userMessage = messageInput.value.trim();
  if (userMessage === '') return;

  // Display the user's message
  appendMessage('User', userMessage);

  // Send the user's message to the API and display the AI's response
  const aiResponse = await sendMessageToAPI(userMessage);
  appendMessage('AI', aiResponse);

  // Clear the input field
  messageInput.value = '';
});

// Event listener for the Enter key
messageInput.addEventListener('keydown', async (event) => {
  if (event.key === 'Enter') {
    event.preventDefault();
    sendButton.click();
  }
});
