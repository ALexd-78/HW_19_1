from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        cont_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(cont_len)
        print(client_data.decode())

        self.send_response(200)
        self.send_header('Content-type', 'application\text')
        self.end_headers()
        self.wfile.write(bytes('', 'utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application\text')
        self.end_headers()
        self.wfile.write(bytes('Hello, World wide web!', 'utf-8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))


    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")