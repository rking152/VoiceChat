from aip import AipSpeech
from aip import AipNlp
import record
import hostkey
import os


def init_speeh():
    return (AipSpeech('ID', 'ID', 'ID'),AipNlp('ID', 'ID', 'ID'))


def filetotxt(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()

def main():
    print('Start')

    client = init_speeh()
    audio = record.MyAudio()

    key = hostkey.Hotkey()
    key.begein_run(audio,client)

    while True:
        data = input('>>>')
        if data == "quit":
            key.Close()
            break
    return

if __name__ == '__main__':
    main()
    os._exit(0)