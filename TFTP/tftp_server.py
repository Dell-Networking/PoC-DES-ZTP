import tftpy

print(f"Starting TFTP server...")
server = tftpy.TftpServer('/home/ben/Downloads/Dell-N1108P-ON/v6.7.1.13')
server.listen('0.0.0.0', 69)

