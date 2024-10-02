from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello")

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print("Server running on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
