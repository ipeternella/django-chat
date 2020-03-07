console.log("Chat connected!");

let paths = window.location.href.split("/").slice(3,6),
    scheme = "ws://",
    chatHost = window.location.host,
    chatPrefix = "ws/chat",
    chatRoom = paths[1],
    userName = paths[2];

let chatSocket = new WebSocket(
    scheme + chatHost + `/${chatPrefix}` + `/${chatRoom}` + `/${userName}/`
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