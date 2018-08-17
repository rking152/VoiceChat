import threading
from pyaudio import PyAudio, paInt16

class MyAudio:
    pa = PyAudio()
    thread = threading.Thread()
    record_data = bytes()
    endslef = True
    Record = False
    stream = pa.open(format=paInt16, channels=1,
                     rate=16000, input=True,
                     frames_per_buffer=1000)

    def __init__(self):
        pass
    def start_record(self):
        self.thread = threading.Thread(target=self.go, name='record')
        self.data = bytes()
        if not self.thread.is_alive():
            self.thread.start()
        self.Record = True
        return
    def go(self):
        global end
        string_audio_data = bytes()
        while self.endslef:
            self.data += self.stream.read(1000)
        self.endslef = True
        return

    def stop_record(self):
        global end
        self.endslef = False
        self.thread.join()
        self.Record = False
        return self.data
