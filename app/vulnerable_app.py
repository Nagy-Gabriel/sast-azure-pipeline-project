import subprocess


def ping_host(host):
    command = "ping -c 1 " + host
    return subprocess.check_output(command, shell=True)