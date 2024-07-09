import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Handling GET request for {self.path}")  # Log the path being requested
        super().do_GET()
        
    def send_response(self, code, message=None):
        print(f"Response code: {code}")  # Log the response code
        super().send_response(code, message)

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8888, directory=None):
    if directory:
        os.chdir(directory)
        print(f"Changed directory to {os.getcwd()}")
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on http://localhost:{port} from directory '{os.getcwd()}'...")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument("--dir", type=str, help="Directory to serve files from", default="public")
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=8888)
    args = parser.parse_args()

    run(port=args.port, directory=args.dir)