import ctypes
import ctypes.wintypes
import threading
import win10toast
import requests
import json
import win32com.client

id1 = 999
id2=106
user32 = ctypes.windll.user32
class Hotkey():
    thread_host = threading.Thread()
    toaster = win10toast.ToastNotifier()
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    def __init__(self):
        pass
    def begein_run(self,audio,client):
        self.thread_host = threading.Thread(target=self.run_hostkey, name='hostkey',args=(audio,client))
        self.thread_host.start()
    def run_hostkey(self,audio,client):
        if not user32.RegisterHotKey(None, id1, 0x0001 | 0x0008 ,0):
            print("Unable to register id", id1) # 返回一个错误信息
            print('>>>',end='')
        try:
            msg = ctypes.wintypes.MSG()

            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if audio.Record == True:
                        print(u'stop record \n>>>')
                        text = client[0].asr(audio.stop_record(), 'pcm', 16000, {'dev_pid': 1536})
                        if text['err_msg'] == 'success.' and text['err_no'] == 0:
                            print(text['result'],'\n>>>',end='')

                            userId = '308015'
                            inputText = {'text': str(text['result'])[2:-2]}
                            key = '389db511305d444780a41bb92c72e87b'
                            userInfo = {'apiKey': key, 'userId': userId}
                            perception = {'inputText': inputText}
                            data = {'perception': perception, 'userInfo': userInfo}

                            url = 'http://openapi.tuling123.com/openapi/api/v2'
                            response = requests.post(url=url, data=json.dumps(data))
                            print(response.text)
                            response.encoding = 'utf-8'
                            result = response.json()
                            answer = result['results'][0]['values']['text']
                            self.speaker.Speak(answer)
                            self.toaster.show_toast(threaded=True, msg=answer,title="")

                            print(answer)
                            print(client[1].depParser(str((text['result']))[2:-2]))
                        else:
                            print('err_msg' + text['err_msg'])
                            print('>>>',end='')
                    else:
                        audio.start_record()
                        print(u'start record\n>>>',end='')

                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            user32.UnregisterHotKey(None, id1)
    def Close(self):
        user32.UnregisterHotKey(None, id1)