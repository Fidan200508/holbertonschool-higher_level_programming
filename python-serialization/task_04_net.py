#!/usr/bin/env python3
"""Client-server application using JSON serialization."""

import socket
import json


def start_server():
    """Start a server to receive serialized data from a client."""
    host = "127.0.0.1"
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, addr = server_socket.accept()

    try:
        data = conn.recv(1024)
        if data:
            deserialized_data = json.loads(data.decode("utf-8"))
            print("Received Dictionary from Client:")
            print(deserialized_data)
    finally:
        conn.close()
        server_socket.close()


def send_data(data):
    """Serialize and send a dictionary to the server."""
    host = "127.0.0.1"
    port = 65432

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        serialized_data = json.dumps(data)
        client_socket.sendall(serialized_data.encode("utf-8"))
    except Exception:
        pass
    finally:
        client_socket.close()
