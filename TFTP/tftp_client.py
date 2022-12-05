import tftpy

client = tftpy.TftpClient('localhost', 69)
client.download('ztp.json', 'tftp_pulled.json')
