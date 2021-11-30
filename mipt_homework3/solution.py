import socket
import time

class ClientError(Exception):
    pass

class Client():
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def connector(self, data):
        try:
            response = b''
            with socket.create_connection((self.host, self.port), self.timeout) as sock:
                sock.sendall(data.encode())  # отсылаем на сервер
                part_response = sock.recv(1024)  # берем первую часть ответа
                try:
                    while part_response:
                        response += part_response
                        part_response = sock.recv(1024)
                except Exception as err:
                    if response:
                        pass
                    else:
                        raise ClientError(err)

            result, values = response.decode().split('\n', 1)
            if result == 'ok':
                return values.strip()
            else:
                raise ClientError(response.decode())
        except Exception as err:
            raise ClientError(err)

    def put(self, name, val, timestamp=None):
        if not timestamp:
            timestamp = int(time.time())
        send_str = f'put {name} {str(val)} {str(timestamp)}\n'
        self.connector(send_str)

    def get(self, metric_name='*'):
        response_dict = {}
        send_str = f'get {metric_name}\n'
        data = self.connector(send_str)  # получем данные
        if data:
            try:
                for row in data.split('\n'):
                    key, value, timestamp = row.split()
                    if key not in response_dict:
                        response_dict[key] = []
                    response_dict[key].append((int(timestamp), float(value)))
                    response_dict[key].sort(key=lambda x: x[0])
            except Exception as err:
                raise ClientError(err)
        return response_dict