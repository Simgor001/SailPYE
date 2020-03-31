import code
cmd = code.InteractiveInterpreter()
with open('temp.py','r',encoding='UTF-8') as f:
    line = f.readline()
    while line:
        cmd.runsource(line)
        line = f.readline()