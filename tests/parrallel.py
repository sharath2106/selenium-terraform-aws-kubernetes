from subprocess import Popen


processes = []

for counter in range(8):
    chrome_cmd = 'export BROWSER=chrome && python test.py'
    processes.append(Popen(chrome_cmd, shell=True))

for counter in range(8):
    processes[counter].wait()
