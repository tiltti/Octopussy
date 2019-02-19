import websocket
import json

try:
    import thread
except ImportError:
    import _thread as thread
import time

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKCMD = '\033[37m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

HOST = "ws://octopi.local/sockjs/websocket"
#HOST = "ws://demos.kaazing.com/echo"

def on_message(ws, message):
    MSG = json.loads(message)
    if 'current' in MSG:
        if 'logs' in MSG['current']:
            LOGS = json.dumps(MSG['current']['logs'])
            if len(LOGS) > 2:
                LOGS = LOGS.replace("Send:",(BColors.OKCMD+"Send:"+BColors.OKGREEN))
                LOGS = LOGS.replace("Recv:",(BColors.OKCMD+"Recv:"+BColors.OKGREEN))
                LOGS = LOGS.replace("M105",(BColors.HEADER+"M105"+BColors.OKGREEN))
                LOGS = LOGS.replace(" ok ",(BColors.OKBLUE+" ok "+BColors.OKGREEN))
                print(BColors.OKGREEN + LOGS + BColors.ENDC)
    #print(message)

def on_error(ws, error):
    print("Error:")
    print(BColors.WARNING)
    print(error)
    print(BColors.ENDC)

def on_close(ws):
    print(BColors.OKBLUE + "Closing Socket..." + BColors.ENDC)

def on_open(ws):
    print("Socket Open...")
    ws.send("{\"auth\": \"tiltti:mustekala\"}")
#    ws.send("{'throttle': 3}")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(HOST,
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
