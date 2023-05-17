# Sockets

## What is a socket?

A socket is an endpoint for communication between two machines. It is a combination of an IP address and a port number. A socket is identified by an IP address concatenated with a port number.

## The python socket API

Python allows for creating and managing sockets through the `socket` module. The module provides a socket class that implements the socket API.

Keep in mind that this module is quite low level and it is recommended to use a higher level module such as `socketserver` for most applications.

Regardless, the socket module is a good way to learn about sockets and how they work.

### Address Family

Sockets are identified by an address family. The address family is a constant that specifies the type of socket. The most common address families are `AF_INET` and `AF_INET6` which are used for IPv4 and IPv6 respectively.

We will see more in the example code.

### Socket Kind

The socket kind is a constant that specifies the type of communication. The most common socket kinds are `SOCK_STREAM` and `SOCK_DGRAM` which are used for TCP and UDP respectively.

We will see more in the example code.

## A simple server-client communication

Server is [here](./server.py)
Client is [here](./client.py)

Run them like so:

In a terminal:

```bash
python server.py localhost 5821
```

In the other terminal:

```bash
python client.py localhost 5821 "Hello, hello world!"
```
