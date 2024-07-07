from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):    
    def _set_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        self._set_headers(200)        
        response = {
            'message': 'POST request received',
            'data': data
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))
##Sulla funzione precedente va integrata la lettura del path e la gestione di un array la configuraizioedelle porte ecc per pote gestire un temporary inmemory DB
def start_server(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()