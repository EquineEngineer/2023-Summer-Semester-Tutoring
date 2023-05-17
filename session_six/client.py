#!/usr/bin/env python3

import socket
import sys


def send(host, port, message: bytes) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message)
        reply = s.recv(1024)
        return repr(reply)


def show_usage():
    print("Usage: client.py <host> <port> <message>")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        show_usage()
        exit(1)

    data = send(sys.argv[1], int(sys.argv[2]), str.encode(sys.argv[3]))
    print("Received", data)
