import socket
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = 8080


def get_status_code(path: str) -> int:
    query = parse_qs(urlparse(path).query)

    status = query.get("status", ["200"])[0]

    try:
        status_code = int(status)

        HTTPStatus(status_code)

        return status_code

    except (ValueError, KeyError):
        return 200


def build_response(request_data: str, client_address) -> bytes:
    lines = request_data.split("\r\n")

    request_line = lines[0]
    method, path, _ = request_line.split()

    status_code = get_status_code(path)
    status_phrase = HTTPStatus(status_code).phrase

    body_lines = [
        f"Request Method: {method}",
        f"Request Source: {client_address}",
        f"Response Status: {status_code} {status_phrase}",
        ""
    ]

    for line in lines[1:]:
        if line == "":
            break
        body_lines.append(line)

    body = "\r\n".join(body_lines)

    response = (
        f"HTTP/1.1 {status_code} {status_phrase}\r\n"
        f"Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        f"\r\n"
        f"{body}"
    )

    return response.encode()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on http://{HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()

        with client_socket:
            request = client_socket.recv(4096).decode()

            print("=== REQUEST ===")
            print(request)

            response = build_response(request, client_address)

            client_socket.sendall(response)