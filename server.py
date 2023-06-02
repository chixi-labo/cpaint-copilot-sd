import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

html_root = "./html"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=html_root, **kwargs)

def begin_dummy_server():
    ip = "localhost"
    port = 4212

    httpd = HTTPServer(('', port), Handler)
    print('HTTPServer began -> http://{}:{}'.format(ip, port))
    server_thread = threading.Thread(target=httpd.serve_forever) 
    server_thread.start()

if __name__ == "__main__":
    begin_dummy_server()
    print("start")