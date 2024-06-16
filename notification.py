from gtts import gTTS
from pycall import CallFile, Call, Application
import sys
import os
import shutil
import subprocess

LANG = "en"
ANEXO = "1001"
CALLER_ID = "NOC Notification <9001>"
AUDIO_NAME = "event_generated"
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

def check_sox_installed():
    print("Checking if sox is installed...")
    if shutil.which("sox") is None:
        print("Error: sox is not installed. Please install sox and try again.")
        sys.exit(1)

def mytext(mytext="Hello There General Kenobi"):
    audio = gTTS(text=mytext, lang=LANG, slow=True)
    audio.save(f"{SCRIPT_PATH}/{AUDIO_NAME}.mp3")
    os.system(f"/usr/bin/sox {SCRIPT_PATH}/{AUDIO_NAME}.mp3 -r 8000 -c1 {SCRIPT_PATH}/{AUDIO_NAME}.gsm pad 2 4")
    os.system(f"rm {SCRIPT_PATH}/{AUDIO_NAME}.mp3")
    os.system(f"mv {SCRIPT_PATH}/{AUDIO_NAME}.gsm /var/lib/asterisk/sounds/en/{AUDIO_NAME}.gsm")

def call(number):
    c = Call(f'SIP/{number}', callerid=f"{CALLER_ID}", wait_time=30, retry_time=60, max_retries=3)
    a = Application('Playback', AUDIO_NAME)
    cf = CallFile(c, a, user='asterisk')
    cf.spool()

if __name__ == '__main__':
    check_sox_installed()
    if len(sys.argv) > 1:
        mytext(sys.argv[1])
        call(ANEXO)
    else:
        print("Error: Missing argument")

#  -  Text2Call
#  -  Author: k0jir0900