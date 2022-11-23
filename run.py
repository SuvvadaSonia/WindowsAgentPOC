"""
    it is a connector and used to connect ubuntu machine
    
"""
import paramiko

class RemoteAgent:
    def __init__(self, hostname, username, password) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password
    def connect_to_remote_host(self,client):
        """        
        It establishes connection with remote device
        """   
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname= self.hostname, username= self.username, password= self.password)
    def execute_commands(self,client):
        """       
        It executes commands in remote device and prints response 
        on local device
        """
        commands = ['df -H','uname -a','hostname -i']

        for command in commands:
            print(command)
            print("\n")
            stdin, stdout, stderr = client.exec_command(command)
            print(stdout.read().decode())

    def close_connection(self,client):
        """
        It closes the established connection with remote device        
        """
        client.close()

if __name__ == "__main__":
    client = paramiko.SSHClient()
    connection = RemoteAgent('192.168.1.237','root','India@123')  
    connection.connect_to_remote_host(client)
    connection.execute_commands(client)
    connection.close_connection(client)