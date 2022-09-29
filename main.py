import os
import socketserver as SocketServer
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from urllib.parse import parse_qs


class Listener(BaseHTTPRequestHandler):

    def response(self, tipo):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        if tipo == "Apagar":
            self.wfile.write(bytes("<html><body>Apagando Equipo.</body></html>", "utf-8"))
        elif tipo == "Reiniciar":
            self.wfile.write(bytes("<html><body>Reiniciando Equipo.</body></html>", "utf-8"))
        elif tipo == "Salir":
            self.wfile.write(bytes("<html><body>Cerrando Sesión.</body></html>", "utf-8"))
        elif tipo == "Sleep":
            self.wfile.write(bytes("<html><body>Suspendiendo Equipo.</body></html>", "utf-8"))

    def apagar(self, tiempo):
        self.response("Apagar")
        os.system("shutdown /s /t " + tiempo)

    def reiniciar(self):
        self.response("Reiniciar")
        os.system("shutdown /r /t 3")

    def salir(self):
        self.response("Salir")
        os.system("shutdown -l")

    def sleep(self):
        self.response("Sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    def do_GET(self):
        if "/apagar" in self.path:
            tiempo = 3
            query_components = parse_qs(urlparse(self.path).query)
            if 'tiempo' in query_components:
                tiempo = query_components["tiempo"][0]
                self.apagar(tiempo)
            else:
                self.apagar(tiempo)
        elif self.path == '/reiniciar':
            self.reiniciar()
        elif self.path == '/salir':
            self.salir()
        elif self.path == '/sleep':
            self.sleep()


httpd = SocketServer.TCPServer(("", 80), Listener)
httpd.serve_forever()