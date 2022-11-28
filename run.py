"""
    it is a connector and used to connect ubuntu machine
    Author: S.Sonia
    
"""
import paramiko
# Paramiko is a Python library that makes a connection with a remote device through SSh

class windowsAgent:
    
    def __init__(self, hostname: str, auth:tuple) -> None:
        self.__user, self.__pwd = auth
        self.hostname = hostname


    def getConfig(self,client):             # connects to ubuntu machine using paramiko 
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname= self.hostname, username= self.__user, password= self.__pwd)
        commands = ['df -H','uname -a','hostname -i']

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read().decode())


if __name__ == "__main__":
    client = paramiko.SSHClient()
    connection = windowsAgent('192.168.1.237',('root','India@123'))
    connection.getConfig(client)

