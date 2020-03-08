# Django Chat!

Django Chat is a project built with Daphne and Channels to demonstrate Django capabilities beyond the HTTP protocol! It
contains a real-time chatting application via sockets protocol. Moreover, it also brings a CHAT BOT logic so that user
can use some commands!

## Application Demo

![Alt text](docs/django_chat_demonstration.gif?raw=true)

## Chat Rooms and Users

Since this is a demo application, to create and join a chat room, just follow the appropriate endpoints:

`/chat/<chat_room>/<chat_user_name>` 

Hence, to join a room named `myroom` with your username being `conker`, just go to the url:

`/chat/myroom/conker`

And all the messages will be sent with the username `conker`! Hyphens are NOT supported yet in the `chat_room`
and `chat_user_name`.

PS: This a demo application just to show Django Channels and chatting logic, so no real user authentication, login
and other security enforcements were developed (not yet... at least!).

## Chat BOT commands

To use a command, start the sentence with a slash `/`! Hence, the syntax to use a command is as follows:

`/command arg1 arg2`

where command is the desired command, and arg1, arg2, etc. are the arguments for such command.

Currently two commands available:

- `/now`: prints the current server datetime;
- `/sms <user_name>`: fakely sends an SMS to the user

`/now`

## Running locally

To run the app, just start it with `docker-compose`:

```bash
docker-compose up
```

This will start Django's development server on `localhost` listening on port `8080`.

## Running tests

Soon to come!
