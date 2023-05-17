#!/usr/bin/env python3

import socket
import sys


def wait_and_receive(host, port):
    print("Waiting for connections...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Sending back data: ", data)
                conn.sendall(data)


def show_usage():
    print("Usage: server.py <host> <port>")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        show_usage()
        exit(1)

    wait_and_receive(sys.argv[1], int(sys.argv[2]))
