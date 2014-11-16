import socket

class Conexao:

   def __init__ (self, sock=None):
      self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
      self.host = socket.gethostbyname (socket.gethostname ())


   ### Getters
   def get_host (self):
      return self.host

   def get_port (self):
      return self.port


   ### Metodos
   # metodo usado para abrir conexao como servidor
   def abrir (self, port = 30000):
      self.port = port
      self.sock.bind (('', port))
      self.sock.listen (1)
      print ('aguardando conexao...')
      self.sock, self.addr = self.sock.accept ()
      print ('conectado a', self.addr)

   # metodo usado para conectar como cliente
   def conectar (self, host, port):
      self.sock.connect ((host, port))

   def enviar (self, data):
      self.sock.send (bytes (data, 'UTF-8'))
      
   def receber (self):
      data = self.sock.recv (5120)
         
      if not data:
         self.encerrar ()
         return -1
      else:
         return data
         
   def encerrar (self):
      self.sock.close ()
