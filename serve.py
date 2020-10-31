from http.server import BaseHTTPRequestHandler, HTTPServer

class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    #handle theGET request from the browser
    #self: the instance of the class: HTTPServer_Request
    def do_GET(self):
        self.send_request(200)
        self.send_header("Content-type","text/html")
        self.end_headers();

        self.wfile.write(b"<!DOCTYPE html>");
        self.wfile.write(b"<html lang='en'>");
        self.wfile.write(b"<head>");
        self.wfile.write(b"<title>hello, title</title>");
        self.wfile.write(b"</head>");
        self.wfile.write(b"<body>");
        self.wfile.write(b"hello world");
        self.wfile.write(b"</body>");
        self.wfile.write(b"</html>");

port = 8080
server_address = ("127.0.0.1", port)
httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
httpd.serve_forever()