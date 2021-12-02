from pynput.keyboard import Key, Controller
import psutil
def tab():
    keyborad = Controller()
    keyborad.press(Key.tab)
    keyborad.release(Key.tab)
while(True):

    if("Acrord32.exe" not in (p.name() for p in psutil.process_iter())):
        pass
    else:
        while("Acrord32.exe" in (p.name() for p in psutil.process_iter())):
            pass
        else:
            tab()
