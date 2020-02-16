console.log("Chat connected!");

let roomName = "room_igp";

let chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);

chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    let message = data['message'];

    document.querySelector('#chat-log').value += (message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();

document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    let messageInputDom = document.querySelector('#chat-message-input');
    let message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message
    }));

    messageInputDom.value = '';
};