css = '''
<style>
    body {
        font-family: 'Lato', sans-serif; /* Use a custom font */
        background-color: #f0f0f0; /* Set a background color for the whole page */
        margin: 0;
        padding: 0;
    }

    .chat-container {
        background-color: #fff; /* Set a background color for the chat container */
        border-radius: 10px; /* Add rounded corners */
        overflow: hidden; /* Hide overflow content */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Add a subtle shadow effect */
    }

    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        animation: fadeIn 0.5s ease; /* Add fadeIn animation */
    }

    .chat-message.user {
        background-color: #2b313e;
        color: #fff; /* Set text color for user messages */
    }

    .chat-message.bot {
        background-color: #475063;
        color: #fff; /* Set text color for bot messages */
    }

    .chat-message .avatar {
        width: 20%;
    }

    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }

    .chat-message .message {
        width: 80%;
        padding: 0 1.5rem;
    }

    /* Keyframe animation for fadeIn effect */
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
</style>

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.pn>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
