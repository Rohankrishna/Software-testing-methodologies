import paramiko

def test_dummy():
    print("hello")

    def test_login():
        host = "ssh.pythonanywhere.com"
        client = paramiko.client.SSHClient()
        client.load_system_host_keys()
        client.connect(host, username="Rohankrishna", password="rohan27561")
        stdin, stdout, stderr = client.exec_command('ls -lwhoami')
        output = stdout.read().decode()
        errors = stderr.read().decode()
        client.close()
        print(output)