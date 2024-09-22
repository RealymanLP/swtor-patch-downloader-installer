from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import tkinter as tkr
import socket
import wget
import json
import time
import os.path
import os
import zipfile, gzip
import urllib
import xml.dom.minidom
import jwt
import base64
import sys
import pathlib
from datetime import datetime
import shutil
import requests
import hashlib
import locale
from threading import Thread
from tkinter.scrolledtext import ScrolledText

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

dir_path = os.path.dirname(os.path.realpath(__file__))
if hasattr(sys, 'frozen'):
    basis = sys.executable
else:
    basis = sys.argv[0]
dir_path = os.path.split(basis)[0]                                    
dirs = os.listdir(dir_path)
for item in dirs:
    if item.endswith(".tmp"):
        os.remove(os.path.join(dir_path, item))
try:
    shutil.rmtree('temp', ignore_errors=True)
except:
    pass

try:
    os.remove(os.path.join(dir_path, "patches_swtor.xml"))
    wget.download("http://realymanlp.de/public/swtor_hashes/patches/patches_swtor.xml", dir_path)
except:
    pass
try:
    os.remove(os.path.join(dir_path, "patches_liveqatest.xml"))
    wget.download("http://realymanlp.de/public/swtor_hashes/patches/patches_liveqatest.xml", dir_path)
except:
    pass
try:
    os.remove(os.path.join(dir_path, "patches_publictest.xml"))
    wget.download("http://realymanlp.de/public/swtor_hashes/patches/patches_publictest.xml", dir_path)
except:
    pass

patches_liveqatest = xml.dom.minidom.parse("patches_liveqatest.xml")
patches_publictest = xml.dom.minidom.parse("patches_publictest.xml")
patches_swtor = xml.dom.minidom.parse("patches_swtor.xml")

itemlist_patches = {}
itemlist_patches["liveqatest"] = patches_liveqatest.getElementsByTagName('patch')
itemlist_patches["publictest"] = patches_publictest.getElementsByTagName('patch')
itemlist_patches["swtor"] = patches_swtor.getElementsByTagName('patch')

global t1
global t2
global zeit1
global zeitx1
global sekunden1
sekunden1 = 0
zeitx1 = ""
global zeit2
global zeitx2
global sekunden2
sekunden2 = 0
zeitx2 = ""
global zeit3
global zeitx3
global sekunden3
sekunden3 = 0
zeitx3 = ""
global zeit4
global zeitx4
global sekunden4
sekunden4 = 0
zeitx4 = ""
global zeit5
global zeitx5
global sekunden5
sekunden5 = 0
zeitx5 = ""
yes = False
t1 = ""
t2 = ""

def close_window():
    CLOSE = True
    print("CLOSE")
    fenster.destroy()
    os._exit(0)

fenster = tkr.Tk()
fenster.title("SWTOR Patch Downloader & Installer")
fenster.protocol("WM_DELETE_WINDOW", close_window)

def txtEvent(event):
    if(event.state==12 and event.keysym=='c' ):
        return
    else:
        return "break"

def autoscroll(event):
    logbox.see(END)
    logbox.edit_modified(0)

logbox = ScrolledText(fenster,width=155,height=17)
logbox.bind("<Key>", lambda e: txtEvent(e))
#logbox.insert(END, "Ready!\n")
logbox.bind('<<Modified>>', autoscroll)
#logbox.config(state=DISABLED)

w = 1300
h = 1000
ws = 0
hs = 0

fenster.geometry(f"{w}x{h}+{ws}+{hs}")
fenster.resizable(False, False)

def set_file_last_modified(file_path, dt):
    t = datetime.fromtimestamp(dt)
    dt_epoch = t.timestamp()
    os.utime(file_path, (dt_epoch, dt_epoch))

def bar1_progress(current, total, width=80):
    global zeit1
    global zeitx1
    global sekunden1
    zeit1 = int(time.time())
    if not zeit1 == zeitx1:
        sekunden1 += 1
    currentx = int(current)
    totalx = int(total)
    try:
        speed = current / sekunden1 / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    if int(currentx / totalx * 100) == 0:
        progress1['value'] = 0
        status1.config(text=f"0%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 1:
        progress1['value'] = 1
        status1.config(text=f"1%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 2:
        progress1['value'] = 2
        status1.config(text=f"2%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 3:
        progress1['value'] = 3
        status1.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 4:
        progress1['value'] = 4
        status1.config(text=f"4%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 5:
        progress1['value'] = 5
        status1.config(text=f"5%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 6:
        progress1['value'] = 6
        status1.config(text=f"6%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 7:
        progress1['value'] = 7
        status1.config(text=f"7%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 8:
        progress1['value'] = 8
        status1.config(text=f"8%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 9:
        progress1['value'] = 9
        status1.config(text=f"9%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 10:
        progress1['value'] = 10
        status1.config(text=f"10%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 11:
        progress1['value'] = 11
        status1.config(text=f"11%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 12:
        progress1['value'] = 12
        status1.config(text=f"12%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 13:
        progress1['value'] = 13
        status1.config(text=f"13%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 14:
        progress1['value'] = 14
        status1.config(text=f"14%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 15:
        progress1['value'] = 15
        status1.config(text=f"15%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 16:
        progress1['value'] = 16
        status1.config(text=f"16%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 17:
        progress1['value'] = 17
        status1.config(text=f"17%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 18:
        progress1['value'] = 18
        status1.config(text=f"18%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 19:
        progress1['value'] = 19
        status1.config(text=f"19%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 20:
        progress1['value'] = 20
        status1.config(text=f"20%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 21:
        progress1['value'] = 21
        status1.config(text=f"21%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 22:
        progress1['value'] = 22
        status1.config(text=f"22%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 23:
        progress1['value'] = 23
        status1.config(text=f"23%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 24:
        progress1['value'] = 24
        status1.config(text=f"24%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 25:
        progress1['value'] = 25
        status1.config(text=f"25%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 26:
        progress1['value'] = 26
        status1.config(text=f"26%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 27:
        progress1['value'] = 27
        status1.config(text=f"27%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 28:
        progress1['value'] = 28
        status1.config(text=f"28%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 29:
        progress1['value'] = 29
        status1.config(text=f"29%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 30:
        progress1['value'] = 30
        status1.config(text=f"30%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 31:
        progress1['value'] = 31
        status1.config(text=f"31%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 32:
        progress1['value'] = 32
        status1.config(text=f"32%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 33:
        progress1['value'] = 33
        status1.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 34:
        progress1['value'] = 34
        status1.config(text=f"34%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 35:
        progress1['value'] = 35
        status1.config(text=f"35%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 36:
        progress1['value'] = 36
        status1.config(text=f"36%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 37:
        progress1['value'] = 37
        status1.config(text=f"37%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 38:
        progress1['value'] = 38
        status1.config(text=f"38%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 39:
        progress1['value'] = 39
        status1.config(text=f"39%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 40:
        progress1['value'] = 40
        status1.config(text=f"40%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 41:
        progress1['value'] = 41
        status1.config(text=f"41%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 42:
        progress1['value'] = 42
        status1.config(text=f"42%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 43:
        progress1['value'] = 43
        status1.config(text=f"43%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 44:
        progress1['value'] = 44
        status1.config(text=f"44%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 45:
        progress1['value'] = 45
        status1.config(text=f"45%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 46:
        progress1['value'] = 46
        status1.config(text=f"46%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 47:
        progress1['value'] = 47
        status1.config(text=f"47%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 48:
        progress1['value'] = 48
        status1.config(text=f"48%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 49:
        progress1['value'] = 49
        status1.config(text=f"49%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 50:
        progress1['value'] = 50
        status1.config(text=f"50%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 51:
        progress1['value'] = 51
        status1.config(text=f"51%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 52:
        progress1['value'] = 52
        status1.config(text=f"52%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 53:
        progress1['value'] = 53
        status1.config(text=f"53%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 54:
        progress1['value'] = 54
        status1.config(text=f"54%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 55:
        progress1['value'] = 55
        status1.config(text=f"55%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 56:
        progress1['value'] = 56
        status1.config(text=f"56%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 57:
        progress1['value'] = 57
        status1.config(text=f"57%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 58:
        progress1['value'] = 58
        status1.config(text=f"58%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 59:
        progress1['value'] = 59
        status1.config(text=f"59%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 60:
        progress1['value'] = 60
        status1.config(text=f"60%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 61:
        progress1['value'] = 61
        status1.config(text=f"61%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 62:
        progress1['value'] = 62
        status1.config(text=f"62%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 63:
        progress1['value'] = 63
        status1.config(text=f"63%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 64:
        progress1['value'] = 64
        status1.config(text=f"64%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 65:
        progress1['value'] = 65
        status1.config(text=f"65%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 66:
        progress1['value'] = 66
        status1.config(text=f"66%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 67:
        progress1['value'] = 67
        status1.config(text=f"67%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 68:
        progress1['value'] = 68
        status1.config(text=f"68%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 69:
        progress1['value'] = 69
        status1.config(text=f"69%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 70:
        progress1['value'] = 70
        status1.config(text=f"70%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 71:
        progress1['value'] = 71
        status1.config(text=f"71%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 72:
        progress1['value'] = 72
        status1.config(text=f"72%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 73:
        progress1['value'] = 73
        status1.config(text=f"73%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 74:
        progress1['value'] = 74
        status1.config(text=f"74%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 75:
        progress1['value'] = 75
        status1.config(text=f"75%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 76:
        progress1['value'] = 76
        status1.config(text=f"76%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 77:
        progress1['value'] = 77
        status1.config(text=f"77%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 78:
        progress1['value'] = 78
        status1.config(text=f"78%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 79:
        progress1['value'] = 79
        status1.config(text=f"79%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 80:
        progress1['value'] = 80
        status1.config(text=f"80%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 81:
        progress1['value'] = 81
        status1.config(text=f"81%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 82:
        progress1['value'] = 82
        status1.config(text=f"82%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 83:
        progress1['value'] = 83
        status1.config(text=f"83%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 84:
        progress1['value'] = 84
        status1.config(text=f"84%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 85:
        progress1['value'] = 85
        status1.config(text=f"85%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 86:
        progress1['value'] = 86
        status1.config(text=f"86%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 87:
        progress1['value'] = 87
        status1.config(text=f"87%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 88:
        progress1['value'] = 88
        status1.config(text=f"88%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 89:
        progress1['value'] = 89
        status1.config(text=f"89%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 90:
        progress1['value'] = 90
        status1.config(text=f"90%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 91:
        progress1['value'] = 91
        status1.config(text=f"91%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 92:
        progress1['value'] = 92
        status1.config(text=f"92%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 93:
        progress1['value'] = 93
        status1.config(text=f"93%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 94:
        progress1['value'] = 94
        status1.config(text=f"94%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 95:
        progress1['value'] = 95
        status1.config(text=f"95%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 96:
        progress1['value'] = 96
        status1.config(text=f"96%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 97:
        progress1['value'] = 97
        status1.config(text=f"97%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 98:
        progress1['value'] = 98
        status1.config(text=f"98%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 99:
        progress1['value'] = 99
        status1.config(text=f"99%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 100:
        progress1['value'] = 100
        status1.config(text=f"100%\n{speed}mb/s")
    zeitx1 = zeit1

def bar2_progress(current, total, width=80):
    global zeit2
    global zeitx2
    global sekunden2
    zeit2 = int(time.time())
    if not zeit2 == zeitx2:
        sekunden2 += 1
    currentx = int(current)
    totalx = int(total)
    try:
        speed = current / sekunden2 / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    if int(currentx / totalx * 100) == 0:
        progress2['value'] = 0
        status2.config(text=f"0%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 1:
        progress2['value'] = 1
        status2.config(text=f"1%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 2:
        progress2['value'] = 2
        status2.config(text=f"2%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 3:
        progress2['value'] = 3
        status2.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 4:
        progress2['value'] = 4
        status2.config(text=f"4%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 5:
        progress2['value'] = 5
        status2.config(text=f"5%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 6:
        progress2['value'] = 6
        status2.config(text=f"6%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 7:
        progress2['value'] = 7
        status2.config(text=f"7%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 8:
        progress2['value'] = 8
        status2.config(text=f"8%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 9:
        progress2['value'] = 9
        status2.config(text=f"9%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 10:
        progress2['value'] = 10
        status2.config(text=f"10%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 11:
        progress2['value'] = 11
        status2.config(text=f"11%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 12:
        progress2['value'] = 12
        status2.config(text=f"12%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 13:
        progress2['value'] = 13
        status2.config(text=f"13%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 14:
        progress2['value'] = 14
        status2.config(text=f"14%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 15:
        progress2['value'] = 15
        status2.config(text=f"15%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 16:
        progress2['value'] = 16
        status2.config(text=f"16%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 17:
        progress2['value'] = 17
        status2.config(text=f"17%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 18:
        progress2['value'] = 18
        status2.config(text=f"18%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 19:
        progress2['value'] = 19
        status2.config(text=f"19%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 20:
        progress2['value'] = 20
        status2.config(text=f"20%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 21:
        progress2['value'] = 21
        status2.config(text=f"21%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 22:
        progress2['value'] = 22
        status2.config(text=f"22%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 23:
        progress2['value'] = 23
        status2.config(text=f"23%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 24:
        progress2['value'] = 24
        status2.config(text=f"24%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 25:
        progress2['value'] = 25
        status2.config(text=f"25%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 26:
        progress2['value'] = 26
        status2.config(text=f"26%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 27:
        progress2['value'] = 27
        status2.config(text=f"27%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 28:
        progress2['value'] = 28
        status2.config(text=f"28%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 29:
        progress2['value'] = 29
        status2.config(text=f"29%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 30:
        progress2['value'] = 30
        status2.config(text=f"30%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 31:
        progress2['value'] = 31
        status2.config(text=f"31%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 32:
        progress2['value'] = 32
        status2.config(text=f"32%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 33:
        progress2['value'] = 33
        status2.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 34:
        progress2['value'] = 34
        status2.config(text=f"34%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 35:
        progress2['value'] = 35
        status2.config(text=f"35%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 36:
        progress2['value'] = 36
        status2.config(text=f"36%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 37:
        progress2['value'] = 37
        status2.config(text=f"37%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 38:
        progress2['value'] = 38
        status2.config(text=f"38%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 39:
        progress2['value'] = 39
        status2.config(text=f"39%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 40:
        progress2['value'] = 40
        status2.config(text=f"40%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 41:
        progress2['value'] = 41
        status2.config(text=f"41%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 42:
        progress2['value'] = 42
        status2.config(text=f"42%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 43:
        progress2['value'] = 43
        status2.config(text=f"43%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 44:
        progress2['value'] = 44
        status2.config(text=f"44%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 45:
        progress2['value'] = 45
        status2.config(text=f"45%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 46:
        progress2['value'] = 46
        status2.config(text=f"46%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 47:
        progress2['value'] = 47
        status2.config(text=f"47%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 48:
        progress2['value'] = 48
        status2.config(text=f"48%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 49:
        progress2['value'] = 49
        status2.config(text=f"49%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 50:
        progress2['value'] = 50
        status2.config(text=f"50%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 51:
        progress2['value'] = 51
        status2.config(text=f"51%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 52:
        progress2['value'] = 52
        status2.config(text=f"52%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 53:
        progress2['value'] = 53
        status2.config(text=f"53%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 54:
        progress2['value'] = 54
        status2.config(text=f"54%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 55:
        progress2['value'] = 55
        status2.config(text=f"55%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 56:
        progress2['value'] = 56
        status2.config(text=f"56%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 57:
        progress2['value'] = 57
        status2.config(text=f"57%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 58:
        progress2['value'] = 58
        status2.config(text=f"58%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 59:
        progress2['value'] = 59
        status2.config(text=f"59%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 60:
        progress2['value'] = 60
        status2.config(text=f"60%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 61:
        progress2['value'] = 61
        status2.config(text=f"61%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 62:
        progress2['value'] = 62
        status2.config(text=f"62%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 63:
        progress2['value'] = 63
        status2.config(text=f"63%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 64:
        progress2['value'] = 64
        status2.config(text=f"64%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 65:
        progress2['value'] = 65
        status2.config(text=f"65%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 66:
        progress2['value'] = 66
        status2.config(text=f"66%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 67:
        progress2['value'] = 67
        status2.config(text=f"67%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 68:
        progress2['value'] = 68
        status2.config(text=f"68%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 69:
        progress2['value'] = 69
        status2.config(text=f"69%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 70:
        progress2['value'] = 70
        status2.config(text=f"70%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 71:
        progress2['value'] = 71
        status2.config(text=f"71%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 72:
        progress2['value'] = 72
        status2.config(text=f"72%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 73:
        progress2['value'] = 73
        status2.config(text=f"73%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 74:
        progress2['value'] = 74
        status2.config(text=f"74%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 75:
        progress2['value'] = 75
        status2.config(text=f"75%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 76:
        progress2['value'] = 76
        status2.config(text=f"76%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 77:
        progress2['value'] = 77
        status2.config(text=f"77%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 78:
        progress2['value'] = 78
        status2.config(text=f"78%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 79:
        progress2['value'] = 79
        status2.config(text=f"79%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 80:
        progress2['value'] = 80
        status2.config(text=f"80%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 81:
        progress2['value'] = 81
        status2.config(text=f"81%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 82:
        progress2['value'] = 82
        status2.config(text=f"82%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 83:
        progress2['value'] = 83
        status2.config(text=f"83%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 84:
        progress2['value'] = 84
        status2.config(text=f"84%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 85:
        progress2['value'] = 85
        status2.config(text=f"85%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 86:
        progress2['value'] = 86
        status2.config(text=f"86%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 87:
        progress2['value'] = 87
        status2.config(text=f"87%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 88:
        progress2['value'] = 88
        status2.config(text=f"88%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 89:
        progress2['value'] = 89
        status2.config(text=f"89%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 90:
        progress2['value'] = 90
        status2.config(text=f"90%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 91:
        progress2['value'] = 91
        status2.config(text=f"91%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 92:
        progress2['value'] = 92
        status2.config(text=f"92%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 93:
        progress2['value'] = 93
        status2.config(text=f"93%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 94:
        progress2['value'] = 94
        status2.config(text=f"94%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 95:
        progress2['value'] = 95
        status2.config(text=f"95%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 96:
        progress2['value'] = 96
        status2.config(text=f"96%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 97:
        progress2['value'] = 97
        status2.config(text=f"97%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 98:
        progress2['value'] = 98
        status2.config(text=f"98%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 99:
        progress2['value'] = 99
        status2.config(text=f"99%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 100:
        progress2['value'] = 100
        status2.config(text=f"100%\n{speed}mb/s")
    zeitx2 = zeit2

def bar3_progress(current, total, width=80):
    global zeit3
    global zeitx3
    global sekunden3
    zeit3 = int(time.time())
    if not zeit3 == zeitx3:
        sekunden3 += 1
    currentx = int(current)
    totalx = int(total)
    try:
        speed = current / sekunden3 / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    if int(currentx / totalx * 100) == 0:
        progress3['value'] = 0
        status3.config(text=f"0%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 1:
        progress3['value'] = 1
        status3.config(text=f"1%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 2:
        progress3['value'] = 2
        status3.config(text=f"2%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 3:
        progress3['value'] = 3
        status3.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 4:
        progress3['value'] = 4
        status3.config(text=f"4%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 5:
        progress3['value'] = 5
        status3.config(text=f"5%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 6:
        progress3['value'] = 6
        status3.config(text=f"6%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 7:
        progress3['value'] = 7
        status3.config(text=f"7%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 8:
        progress3['value'] = 8
        status3.config(text=f"8%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 9:
        progress3['value'] = 9
        status3.config(text=f"9%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 10:
        progress3['value'] = 10
        status3.config(text=f"10%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 11:
        progress3['value'] = 11
        status3.config(text=f"11%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 12:
        progress3['value'] = 12
        status3.config(text=f"12%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 13:
        progress3['value'] = 13
        status3.config(text=f"13%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 14:
        progress3['value'] = 14
        status3.config(text=f"14%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 15:
        progress3['value'] = 15
        status3.config(text=f"15%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 16:
        progress3['value'] = 16
        status3.config(text=f"16%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 17:
        progress3['value'] = 17
        status3.config(text=f"17%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 18:
        progress3['value'] = 18
        status3.config(text=f"18%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 19:
        progress3['value'] = 19
        status3.config(text=f"19%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 20:
        progress3['value'] = 20
        status3.config(text=f"20%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 21:
        progress3['value'] = 21
        status3.config(text=f"21%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 22:
        progress3['value'] = 22
        status3.config(text=f"22%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 23:
        progress3['value'] = 23
        status3.config(text=f"23%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 24:
        progress3['value'] = 24
        status3.config(text=f"24%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 25:
        progress3['value'] = 25
        status3.config(text=f"25%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 26:
        progress3['value'] = 26
        status3.config(text=f"26%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 27:
        progress3['value'] = 27
        status3.config(text=f"27%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 28:
        progress3['value'] = 28
        status3.config(text=f"28%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 29:
        progress3['value'] = 29
        status3.config(text=f"29%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 30:
        progress3['value'] = 30
        status3.config(text=f"30%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 31:
        progress3['value'] = 31
        status3.config(text=f"31%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 32:
        progress3['value'] = 32
        status3.config(text=f"32%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 33:
        progress3['value'] = 33
        status3.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 34:
        progress3['value'] = 34
        status3.config(text=f"34%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 35:
        progress3['value'] = 35
        status3.config(text=f"35%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 36:
        progress3['value'] = 36
        status3.config(text=f"36%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 37:
        progress3['value'] = 37
        status3.config(text=f"37%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 38:
        progress3['value'] = 38
        status3.config(text=f"38%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 39:
        progress3['value'] = 39
        status3.config(text=f"39%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 40:
        progress3['value'] = 40
        status3.config(text=f"40%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 41:
        progress3['value'] = 41
        status3.config(text=f"41%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 42:
        progress3['value'] = 42
        status3.config(text=f"42%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 43:
        progress3['value'] = 43
        status3.config(text=f"43%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 44:
        progress3['value'] = 44
        status3.config(text=f"44%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 45:
        progress3['value'] = 45
        status3.config(text=f"45%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 46:
        progress3['value'] = 46
        status3.config(text=f"46%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 47:
        progress3['value'] = 47
        status3.config(text=f"47%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 48:
        progress3['value'] = 48
        status3.config(text=f"48%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 49:
        progress3['value'] = 49
        status3.config(text=f"49%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 50:
        progress3['value'] = 50
        status3.config(text=f"50%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 51:
        progress3['value'] = 51
        status3.config(text=f"51%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 52:
        progress3['value'] = 52
        status3.config(text=f"52%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 53:
        progress3['value'] = 53
        status3.config(text=f"53%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 54:
        progress3['value'] = 54
        status3.config(text=f"54%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 55:
        progress3['value'] = 55
        status3.config(text=f"55%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 56:
        progress3['value'] = 56
        status3.config(text=f"56%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 57:
        progress3['value'] = 57
        status3.config(text=f"57%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 58:
        progress3['value'] = 58
        status3.config(text=f"58%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 59:
        progress3['value'] = 59
        status3.config(text=f"59%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 60:
        progress3['value'] = 60
        status3.config(text=f"60%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 61:
        progress3['value'] = 61
        status3.config(text=f"61%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 62:
        progress3['value'] = 62
        status3.config(text=f"62%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 63:
        progress3['value'] = 63
        status3.config(text=f"63%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 64:
        progress3['value'] = 64
        status3.config(text=f"64%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 65:
        progress3['value'] = 65
        status3.config(text=f"65%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 66:
        progress3['value'] = 66
        status3.config(text=f"66%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 67:
        progress3['value'] = 67
        status3.config(text=f"67%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 68:
        progress3['value'] = 68
        status3.config(text=f"68%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 69:
        progress3['value'] = 69
        status3.config(text=f"69%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 70:
        progress3['value'] = 70
        status3.config(text=f"70%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 71:
        progress3['value'] = 71
        status3.config(text=f"71%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 72:
        progress3['value'] = 72
        status3.config(text=f"72%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 73:
        progress3['value'] = 73
        status3.config(text=f"73%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 74:
        progress3['value'] = 74
        status3.config(text=f"74%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 75:
        progress3['value'] = 75
        status3.config(text=f"75%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 76:
        progress3['value'] = 76
        status3.config(text=f"76%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 77:
        progress3['value'] = 77
        status3.config(text=f"77%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 78:
        progress3['value'] = 78
        status3.config(text=f"78%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 79:
        progress3['value'] = 79
        status3.config(text=f"79%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 80:
        progress3['value'] = 80
        status3.config(text=f"80%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 81:
        progress3['value'] = 81
        status3.config(text=f"81%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 82:
        progress3['value'] = 82
        status3.config(text=f"82%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 83:
        progress3['value'] = 83
        status3.config(text=f"83%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 84:
        progress3['value'] = 84
        status3.config(text=f"84%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 85:
        progress3['value'] = 85
        status3.config(text=f"85%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 86:
        progress3['value'] = 86
        status3.config(text=f"86%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 87:
        progress3['value'] = 87
        status3.config(text=f"87%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 88:
        progress3['value'] = 88
        status3.config(text=f"88%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 89:
        progress3['value'] = 89
        status3.config(text=f"89%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 90:
        progress3['value'] = 90
        status3.config(text=f"90%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 91:
        progress3['value'] = 91
        status3.config(text=f"91%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 92:
        progress3['value'] = 92
        status3.config(text=f"92%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 93:
        progress3['value'] = 93
        status3.config(text=f"93%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 94:
        progress3['value'] = 94
        status3.config(text=f"94%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 95:
        progress3['value'] = 95
        status3.config(text=f"95%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 96:
        progress3['value'] = 96
        status3.config(text=f"96%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 97:
        progress3['value'] = 97
        status3.config(text=f"97%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 98:
        progress3['value'] = 98
        status3.config(text=f"98%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 99:
        progress3['value'] = 99
        status3.config(text=f"99%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 100:
        progress3['value'] = 100
        status3.config(text=f"100%\n{speed}mb/s")
    zeitx3 = zeit3

def bar4_progress(current, total, width=80):
    global zeit4
    global zeitx4
    global sekunden4
    zeit4 = int(time.time())
    if not zeit4 == zeitx4:
        sekunden4 += 1
    currentx = int(current)
    totalx = int(total)
    try:
        speed = current / sekunden4 / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    if int(currentx / totalx * 100) == 0:
        progress4['value'] = 0
        status4.config(text=f"0%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 1:
        progress4['value'] = 1
        status4.config(text=f"1%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 2:
        progress4['value'] = 2
        status4.config(text=f"2%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 3:
        progress4['value'] = 3
        status4.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 4:
        progress4['value'] = 4
        status4.config(text=f"4%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 5:
        progress4['value'] = 5
        status4.config(text=f"5%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 6:
        progress4['value'] = 6
        status4.config(text=f"6%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 7:
        progress4['value'] = 7
        status4.config(text=f"7%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 8:
        progress4['value'] = 8
        status4.config(text=f"8%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 9:
        progress4['value'] = 9
        status4.config(text=f"9%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 10:
        progress4['value'] = 10
        status4.config(text=f"10%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 11:
        progress4['value'] = 11
        status4.config(text=f"11%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 12:
        progress4['value'] = 12
        status4.config(text=f"12%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 13:
        progress4['value'] = 13
        status4.config(text=f"13%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 14:
        progress4['value'] = 14
        status4.config(text=f"14%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 15:
        progress4['value'] = 15
        status4.config(text=f"15%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 16:
        progress4['value'] = 16
        status4.config(text=f"16%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 17:
        progress4['value'] = 17
        status4.config(text=f"17%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 18:
        progress4['value'] = 18
        status4.config(text=f"18%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 19:
        progress4['value'] = 19
        status4.config(text=f"19%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 20:
        progress4['value'] = 20
        status4.config(text=f"20%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 21:
        progress4['value'] = 21
        status4.config(text=f"21%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 22:
        progress4['value'] = 22
        status4.config(text=f"22%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 23:
        progress4['value'] = 23
        status4.config(text=f"23%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 24:
        progress4['value'] = 24
        status4.config(text=f"24%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 25:
        progress4['value'] = 25
        status4.config(text=f"25%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 26:
        progress4['value'] = 26
        status4.config(text=f"26%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 27:
        progress4['value'] = 27
        status4.config(text=f"27%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 28:
        progress4['value'] = 28
        status4.config(text=f"28%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 29:
        progress4['value'] = 29
        status4.config(text=f"29%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 30:
        progress4['value'] = 30
        status4.config(text=f"30%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 31:
        progress4['value'] = 31
        status4.config(text=f"31%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 32:
        progress4['value'] = 32
        status4.config(text=f"32%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 33:
        progress4['value'] = 33
        status4.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 34:
        progress4['value'] = 34
        status4.config(text=f"34%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 35:
        progress4['value'] = 35
        status4.config(text=f"35%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 36:
        progress4['value'] = 36
        status4.config(text=f"36%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 37:
        progress4['value'] = 37
        status4.config(text=f"37%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 38:
        progress4['value'] = 38
        status4.config(text=f"38%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 39:
        progress4['value'] = 39
        status4.config(text=f"39%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 40:
        progress4['value'] = 40
        status4.config(text=f"40%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 41:
        progress4['value'] = 41
        status4.config(text=f"41%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 42:
        progress4['value'] = 42
        status4.config(text=f"42%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 43:
        progress4['value'] = 43
        status4.config(text=f"43%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 44:
        progress4['value'] = 44
        status4.config(text=f"44%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 45:
        progress4['value'] = 45
        status4.config(text=f"45%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 46:
        progress4['value'] = 46
        status4.config(text=f"46%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 47:
        progress4['value'] = 47
        status4.config(text=f"47%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 48:
        progress4['value'] = 48
        status4.config(text=f"48%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 49:
        progress4['value'] = 49
        status4.config(text=f"49%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 50:
        progress4['value'] = 50
        status4.config(text=f"50%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 51:
        progress4['value'] = 51
        status4.config(text=f"51%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 52:
        progress4['value'] = 52
        status4.config(text=f"52%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 53:
        progress4['value'] = 53
        status4.config(text=f"53%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 54:
        progress4['value'] = 54
        status4.config(text=f"54%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 55:
        progress4['value'] = 55
        status4.config(text=f"55%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 56:
        progress4['value'] = 56
        status4.config(text=f"56%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 57:
        progress4['value'] = 57
        status4.config(text=f"57%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 58:
        progress4['value'] = 58
        status4.config(text=f"58%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 59:
        progress4['value'] = 59
        status4.config(text=f"59%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 60:
        progress4['value'] = 60
        status4.config(text=f"60%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 61:
        progress4['value'] = 61
        status4.config(text=f"61%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 62:
        progress4['value'] = 62
        status4.config(text=f"62%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 63:
        progress4['value'] = 63
        status4.config(text=f"63%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 64:
        progress4['value'] = 64
        status4.config(text=f"64%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 65:
        progress4['value'] = 65
        status4.config(text=f"65%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 66:
        progress4['value'] = 66
        status4.config(text=f"66%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 67:
        progress4['value'] = 67
        status4.config(text=f"67%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 68:
        progress4['value'] = 68
        status4.config(text=f"68%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 69:
        progress4['value'] = 69
        status4.config(text=f"69%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 70:
        progress4['value'] = 70
        status4.config(text=f"70%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 71:
        progress4['value'] = 71
        status4.config(text=f"71%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 72:
        progress4['value'] = 72
        status4.config(text=f"72%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 73:
        progress4['value'] = 73
        status4.config(text=f"73%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 74:
        progress4['value'] = 74
        status4.config(text=f"74%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 75:
        progress4['value'] = 75
        status4.config(text=f"75%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 76:
        progress4['value'] = 76
        status4.config(text=f"76%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 77:
        progress4['value'] = 77
        status4.config(text=f"77%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 78:
        progress4['value'] = 78
        status4.config(text=f"78%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 79:
        progress4['value'] = 79
        status4.config(text=f"79%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 80:
        progress4['value'] = 80
        status4.config(text=f"80%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 81:
        progress4['value'] = 81
        status4.config(text=f"81%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 82:
        progress4['value'] = 82
        status4.config(text=f"82%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 83:
        progress4['value'] = 83
        status4.config(text=f"83%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 84:
        progress4['value'] = 84
        status4.config(text=f"84%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 85:
        progress4['value'] = 85
        status4.config(text=f"85%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 86:
        progress4['value'] = 86
        status4.config(text=f"86%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 87:
        progress4['value'] = 87
        status4.config(text=f"87%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 88:
        progress4['value'] = 88
        status4.config(text=f"88%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 89:
        progress4['value'] = 89
        status4.config(text=f"89%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 90:
        progress4['value'] = 90
        status4.config(text=f"90%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 91:
        progress4['value'] = 91
        status4.config(text=f"91%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 92:
        progress4['value'] = 92
        status4.config(text=f"92%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 93:
        progress4['value'] = 93
        status4.config(text=f"93%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 94:
        progress4['value'] = 94
        status4.config(text=f"94%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 95:
        progress4['value'] = 95
        status4.config(text=f"95%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 96:
        progress4['value'] = 96
        status4.config(text=f"96%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 97:
        progress4['value'] = 97
        status4.config(text=f"97%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 98:
        progress4['value'] = 98
        status4.config(text=f"98%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 99:
        progress4['value'] = 99
        status4.config(text=f"99%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 100:
        progress4['value'] = 100
        status4.config(text=f"100%\n{speed}mb/s")
    zeitx4 = zeit4

def bar5_progress(current, total, width=80):
    global zeit5
    global zeitx5
    global sekunden5
    zeit5 = int(time.time())
    if not zeit5 == zeitx5:
        sekunden5 += 1
    currentx = int(current)
    totalx = int(total)
    try:
        speed = current / sekunden5 / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    if int(currentx / totalx * 100) == 0:
        progress5['value'] = 0
        status5.config(text=f"0%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 1:
        progress5['value'] = 1
        status5.config(text=f"1%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 2:
        progress5['value'] = 2
        status5.config(text=f"2%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 3:
        progress5['value'] = 3
        status5.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 4:
        progress5['value'] = 4
        status5.config(text=f"4%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 5:
        progress5['value'] = 5
        status5.config(text=f"5%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 6:
        progress5['value'] = 6
        status5.config(text=f"6%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 7:
        progress5['value'] = 7
        status5.config(text=f"7%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 8:
        progress5['value'] = 8
        status5.config(text=f"8%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 9:
        progress5['value'] = 9
        status5.config(text=f"9%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 10:
        progress5['value'] = 10
        status5.config(text=f"10%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 11:
        progress5['value'] = 11
        status5.config(text=f"11%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 12:
        progress5['value'] = 12
        status5.config(text=f"12%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 13:
        progress5['value'] = 13
        status5.config(text=f"13%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 14:
        progress5['value'] = 14
        status5.config(text=f"14%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 15:
        progress5['value'] = 15
        status5.config(text=f"15%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 16:
        progress5['value'] = 16
        status5.config(text=f"16%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 17:
        progress5['value'] = 17
        status5.config(text=f"17%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 18:
        progress5['value'] = 18
        status5.config(text=f"18%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 19:
        progress5['value'] = 19
        status5.config(text=f"19%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 20:
        progress5['value'] = 20
        status5.config(text=f"20%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 21:
        progress5['value'] = 21
        status5.config(text=f"21%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 22:
        progress5['value'] = 22
        status5.config(text=f"22%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 23:
        progress5['value'] = 23
        status5.config(text=f"23%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 24:
        progress5['value'] = 24
        status5.config(text=f"24%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 25:
        progress5['value'] = 25
        status5.config(text=f"25%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 26:
        progress5['value'] = 26
        status5.config(text=f"26%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 27:
        progress5['value'] = 27
        status5.config(text=f"27%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 28:
        progress5['value'] = 28
        status5.config(text=f"28%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 29:
        progress5['value'] = 29
        status5.config(text=f"29%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 30:
        progress5['value'] = 30
        status5.config(text=f"30%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 31:
        progress5['value'] = 31
        status5.config(text=f"31%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 32:
        progress5['value'] = 32
        status5.config(text=f"32%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 33:
        progress5['value'] = 33
        status5.config(text=f"3%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 34:
        progress5['value'] = 34
        status5.config(text=f"34%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 35:
        progress5['value'] = 35
        status5.config(text=f"35%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 36:
        progress5['value'] = 36
        status5.config(text=f"36%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 37:
        progress5['value'] = 37
        status5.config(text=f"37%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 38:
        progress5['value'] = 38
        status5.config(text=f"38%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 39:
        progress5['value'] = 39
        status5.config(text=f"39%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 40:
        progress5['value'] = 40
        status5.config(text=f"40%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 41:
        progress5['value'] = 41
        status5.config(text=f"41%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 42:
        progress5['value'] = 42
        status5.config(text=f"42%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 43:
        progress5['value'] = 43
        status5.config(text=f"43%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 44:
        progress5['value'] = 44
        status5.config(text=f"44%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 45:
        progress5['value'] = 45
        status5.config(text=f"45%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 46:
        progress5['value'] = 46
        status5.config(text=f"46%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 47:
        progress5['value'] = 47
        status5.config(text=f"47%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 48:
        progress5['value'] = 48
        status5.config(text=f"48%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 49:
        progress5['value'] = 49
        status5.config(text=f"49%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 50:
        progress5['value'] = 50
        status5.config(text=f"50%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 51:
        progress5['value'] = 51
        status5.config(text=f"51%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 52:
        progress5['value'] = 52
        status5.config(text=f"52%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 53:
        progress5['value'] = 53
        status5.config(text=f"53%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 54:
        progress5['value'] = 54
        status5.config(text=f"54%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 55:
        progress5['value'] = 55
        status5.config(text=f"55%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 56:
        progress5['value'] = 56
        status5.config(text=f"56%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 57:
        progress5['value'] = 57
        status5.config(text=f"57%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 58:
        progress5['value'] = 58
        status5.config(text=f"58%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 59:
        progress5['value'] = 59
        status5.config(text=f"59%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 60:
        progress5['value'] = 60
        status5.config(text=f"60%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 61:
        progress5['value'] = 61
        status5.config(text=f"61%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 62:
        progress5['value'] = 62
        status5.config(text=f"62%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 63:
        progress5['value'] = 63
        status5.config(text=f"63%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 64:
        progress5['value'] = 64
        status5.config(text=f"64%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 65:
        progress5['value'] = 65
        status5.config(text=f"65%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 66:
        progress5['value'] = 66
        status5.config(text=f"66%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 67:
        progress5['value'] = 67
        status5.config(text=f"67%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 68:
        progress5['value'] = 68
        status5.config(text=f"68%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 69:
        progress5['value'] = 69
        status5.config(text=f"69%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 70:
        progress5['value'] = 70
        status5.config(text=f"70%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 71:
        progress5['value'] = 71
        status5.config(text=f"71%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 72:
        progress5['value'] = 72
        status5.config(text=f"72%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 73:
        progress5['value'] = 73
        status5.config(text=f"73%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 74:
        progress5['value'] = 74
        status5.config(text=f"74%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 75:
        progress5['value'] = 75
        status5.config(text=f"75%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 76:
        progress5['value'] = 76
        status5.config(text=f"76%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 77:
        progress5['value'] = 77
        status5.config(text=f"77%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 78:
        progress5['value'] = 78
        status5.config(text=f"78%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 79:
        progress5['value'] = 79
        status5.config(text=f"79%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 80:
        progress5['value'] = 80
        status5.config(text=f"80%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 81:
        progress5['value'] = 81
        status5.config(text=f"81%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 82:
        progress5['value'] = 82
        status5.config(text=f"82%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 83:
        progress5['value'] = 83
        status5.config(text=f"83%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 84:
        progress5['value'] = 84
        status5.config(text=f"84%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 85:
        progress5['value'] = 85
        status5.config(text=f"85%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 86:
        progress5['value'] = 86
        status5.config(text=f"86%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 87:
        progress5['value'] = 87
        status5.config(text=f"87%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 88:
        progress5['value'] = 88
        status5.config(text=f"88%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 89:
        progress5['value'] = 89
        status5.config(text=f"89%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 90:
        progress5['value'] = 90
        status5.config(text=f"90%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 91:
        progress5['value'] = 91
        status5.config(text=f"91%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 92:
        progress5['value'] = 92
        status5.config(text=f"92%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 93:
        progress5['value'] = 93
        status5.config(text=f"93%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 94:
        progress5['value'] = 94
        status5.config(text=f"94%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 95:
        progress5['value'] = 95
        status5.config(text=f"95%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 96:
        progress5['value'] = 96
        status5.config(text=f"96%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 97:
        progress5['value'] = 97
        status5.config(text=f"97%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 98:
        progress5['value'] = 98
        status5.config(text=f"98%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 99:
        progress5['value'] = 99
        status5.config(text=f"99%\n{speed}mb/s")
    if int(currentx / totalx * 100) == 100:
        progress5['value'] = 100
        status5.config(text=f"100%\n{speed}mb/s")
    zeitx5 = zeit5

def bar_progress(current, total, width=80):
    global zeit1
    global zeit2
    global zeit3
    global zeit4
    global zeit5
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    zeit = int(time.time())
    if not zeit == zeitx:
        sekunden += 1
    currentx = int(current)
    totalx = int(total)
    leiste =     "  [                                                   ]"
    if int(currentx / totalx * 100) == 1 or int(currentx / totalx * 100) == 2:
        leiste = "  [.                                                  ]"
    if int(currentx / totalx * 100) == 3 or int(currentx / totalx * 100) == 4:
        leiste = "  [..                                                 ]"
    if int(currentx / totalx * 100) == 5 or int(currentx / totalx * 100) == 6:
        leiste = "  [...                                                ]"
    if int(currentx / totalx * 100) == 7 or int(currentx / totalx * 100) == 8:
        leiste = "  [....                                               ]"
    if int(currentx / totalx * 100) == 9:
        leiste = "  [.....                                              ]"
    if int(currentx / totalx * 100) == 10:
        leiste = " [.....                                              ]"
    if int(currentx / totalx * 100) == 11 or int(currentx / totalx * 100) == 12:
        leiste = " [......                                             ]"
    if int(currentx / totalx * 100) == 13 or int(currentx / totalx * 100) == 14:
        leiste = " [.......                                            ]"
    if int(currentx / totalx * 100) == 15 or int(currentx / totalx * 100) == 16:
        leiste = " [........                                          ]"
    if int(currentx / totalx * 100) == 17 or int(currentx / totalx * 100) == 18:
        leiste = " [.........                                          ]"
    if int(currentx / totalx * 100) == 19 or int(currentx / totalx * 100) == 20:
        leiste = " [..........                                         ]"
    if int(currentx / totalx * 100) == 21 or int(currentx / totalx * 100) == 22:
        leiste = " [...........                                        ]"
    if int(currentx / totalx * 100) == 23 or int(currentx / totalx * 100) == 24:
        leiste = " [............                                       ]"
    if int(currentx / totalx * 100) == 25 or int(currentx / totalx * 100) == 26:
        leiste = " [.............                                      ]"
    if int(currentx / totalx * 100) == 27 or int(currentx / totalx * 100) == 28:
        leiste = " [..............                                     ]"
    if int(currentx / totalx * 100) == 29 or int(currentx / totalx * 100) == 30:
        leiste = " [...............                                    ]"
    if int(currentx / totalx * 100) == 31 or int(currentx / totalx * 100) == 32:
        leiste = " [................                                   ]"
    if int(currentx / totalx * 100) == 33 or int(currentx / totalx * 100) == 34:
        leiste = " [.................                                  ]"
    if int(currentx / totalx * 100) == 35 or int(currentx / totalx * 100) == 36:
        leiste = " [..................                                 ]"
    if int(currentx / totalx * 100) == 37 or int(currentx / totalx * 100) == 38:
        leiste = " [...................                                ]"
    if int(currentx / totalx * 100) == 39 or int(currentx / totalx * 100) == 40:
        leiste = " [....................                               ]"
    if int(currentx / totalx * 100) == 41 or int(currentx / totalx * 100) == 42:
        leiste = " [.....................                              ]"
    if int(currentx / totalx * 100) == 43 or int(currentx / totalx * 100) == 44:
        leiste = " [......................                             ]"
    if int(currentx / totalx * 100) == 45 or int(currentx / totalx * 100) == 46:
        leiste = " [.......................                            ]"
    if int(currentx / totalx * 100) == 47 or int(currentx / totalx * 100) == 48:
        leiste = " [........................                           ]"
    if int(currentx / totalx * 100) == 49 or int(currentx / totalx * 100) == 50:
        leiste = " [.........................                          ]"
    if int(currentx / totalx * 100) == 51 or int(currentx / totalx * 100) == 52:
        leiste = " [..........................                         ]"
    if int(currentx / totalx * 100) == 53 or int(currentx / totalx * 100) == 54:
        leiste = " [...........................                        ]"
    if int(currentx / totalx * 100) == 55 or int(currentx / totalx * 100) == 56:
        leiste = " [............................                       ]"
    if int(currentx / totalx * 100) == 57 or int(currentx / totalx * 100) == 58:
        leiste = " [.............................                      ]"
    if int(currentx / totalx * 100) == 59 or int(currentx / totalx * 100) == 60:
        leiste = " [..............................                     ]"
    if int(currentx / totalx * 100) == 61 or int(currentx / totalx * 100) == 62:
        leiste = " [...............................                    ]"
    if int(currentx / totalx * 100) == 63 or int(currentx / totalx * 100) == 64:
        leiste = " [................................                   ]"
    if int(currentx / totalx * 100) == 65 or int(currentx / totalx * 100) == 66:
        leiste = " [.................................                  ]"
    if int(currentx / totalx * 100) == 67 or int(currentx / totalx * 100) == 68:
        leiste = " [..................................                 ]"
    if int(currentx / totalx * 100) == 69 or int(currentx / totalx * 100) == 70:
        leiste = " [...................................                ]"
    if int(currentx / totalx * 100) == 71 or int(currentx / totalx * 100) == 72:
        leiste = " [....................................               ]"
    if int(currentx / totalx * 100) == 73 or int(currentx / totalx * 100) == 74:
        leiste = " [.....................................              ]"
    if int(currentx / totalx * 100) == 75 or int(currentx / totalx * 100) == 76:
        leiste = " [......................................             ]"
    if int(currentx / totalx * 100) == 77 or int(currentx / totalx * 100) == 78:
        leiste = " [.......................................            ]"
    if int(currentx / totalx * 100) == 79 or int(currentx / totalx * 100) == 80:
        leiste = " [........................................           ]"
    if int(currentx / totalx * 100) == 81 or int(currentx / totalx * 100) == 82:
        leiste = " [.........................................          ]"
    if int(currentx / totalx * 100) == 83 or int(currentx / totalx * 100) == 84:
        leiste = " [..........................................         ]"
    if int(currentx / totalx * 100) == 85 or int(currentx / totalx * 100) == 86:
        leiste = " [...........................................        ]"
    if int(currentx / totalx * 100) == 87 or int(currentx / totalx * 100) == 88:
        leiste = " [............................................       ]"
    if int(currentx / totalx * 100) == 89 or int(currentx / totalx * 100) == 90:
        leiste = " [.............................................      ]"
    if int(currentx / totalx * 100) == 91 or int(currentx / totalx * 100) == 92:
        leiste = " [..............................................     ]"
    if int(currentx / totalx * 100) == 93 or int(currentx / totalx * 100) == 94:
        leiste = " [...............................................    ]"
    if int(currentx / totalx * 100) == 95 or int(currentx / totalx * 100) == 96:
        leiste = " [................................................   ]"
    if int(currentx / totalx * 100) == 97 or int(currentx / totalx * 100) == 98:
        leiste = " [.................................................  ]"
    if int(currentx / totalx * 100) == 99:
        leiste = " [.................................................. ]"
    if int(currentx / totalx * 100) == 100:
        leiste = "[...................................................]"
    try:
        speed = current / sekunden / 1000000
        speed = str(format(speed, '.2f'))
    except:
        speed = 0
    progress_message = f"{int(currentx / totalx * 100)}% {leiste} {current} / {total} [{speed}mb/s]"
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()
    zeitx = zeit

def install_files(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    global t1
    global t2

    log1_label.config(text=f"Installing...")

    if installloc == None:
        installloc = installzeile.get()
    logbox.insert(END, "\nStarting installation\n\n")#Press CTRL+C to stop.\n\n")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
            elif savetype == "backup":
                alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}_{language_wert}.{environment_wert}"]
        except:
            logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            return

    if assets == "assets":
        try:
            os.makedirs(f"{installloc}/Assets/")
        except:
            pass
    elif assets == "movies":
        try:
            os.makedirs(f"{installloc}/Movies/{language_wert.replace('_', '-')}/")
        except:
            pass
    if savetype == "cdn":
        metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "backup":
        metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{assets}_{language_wert}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
    metafile_c = metafile.read()
    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
    metafiles = metafile_content["pieces"]["digests"]
    metafile_filenames = metafile_content["files"]
    metafile_padding = metafile_content["pad"]
    scantime = metafile_content["scanTime"]

    if assets == "assets":
        if savetype == "cdn":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Assets/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Assets/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{digest[:2]}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return
            
        if savetype == "backup":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Assets/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Assets/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return

        if savetype == "root":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Assets/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Assets/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return

        logbox.insert(END, "Installation finished!\n")
        try:
            log1_label.config(text=f"Installation finished!")
        except:
            pass
        return

    elif assets == "movies":
        if savetype == "cdn":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/Movies/{metafile_content['files'][current_file]['name']}"
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except Exception as e:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{digest[:2]}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return
            
        if savetype == "backup":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f""
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return

        if savetype == "root":
            current_file = 0
            current_pad = 0
            file = metafile_filenames[current_file]

            fd = 0
            fdOffset = 0
            target = 0
            partial = 0

            total = 0
            padding = metafile_padding[current_pad]

            last_text = f""
            text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f""
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                    header = solidpiece.read(6)
                    compression = header[5]
                    if (compression == 2): # gzip
                        piece = gzip.decompress(solidpiece.read())
                    else: # no compression
                        piece = solidpiece.read()
                    solidpiece.close()

                    pieceOffset = 0
                    while (len(piece) - pieceOffset > 0):
                        if (fd == 0):
                            target = f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}"
                            partial = target + '.solidpartial'
                            path = pathlib.Path(partial)
                            if (path.parent.exists() != True):
                                os.makedirs(os.path.dirname(path))
                            fd = open(partial, 'wb')
                        
                        size = file['size'] - fdOffset
                        if (size > len(piece) - pieceOffset):
                            size = len(piece) - pieceOffset

                        if (total + size > padding['offset']):
                            diff = padding['offset'] - total
                            size = diff
                            current_pad += 1
                            padding = metafile_content['pad'][current_pad]
                        total += size

                        start = fdOffset
                        remaining = size
                        written = 0
                        while (start + size > fdOffset):
                            written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                            remaining -= written
                            pieceOffset += written
                            fdOffset += written

                        if (fdOffset == file['size']):
                            fd.close()
                            os.replace(partial, target)
                            set_file_last_modified(f"{installloc}/Movies/{language_wert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/Movies/{language_wert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                logbox.insert(END, "You stopped the installation!\n")
                try:
                    log1_label.config(text=f"You stopped the installation!")
                except:
                    pass
                return
            except:
                logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
                try:
                    log1_label.config(text=f"ERROR: Missing files")
                except:
                    pass
                return

        logbox.insert(END, "Installation finished!\n")
        try:
            log1_label.config(text=f"Installation finished!")
        except:
            pass
def install_client(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    global t1
    global t2

    if installloc == None:
        installloc = installzeile.get()
    logbox.insert(END, "\nStarting installation\n\n")#Press CTRL+C to stop.\n\n")
    log1_label.config(text=f"Installing...")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
            elif savetype == "backup":
                alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
        except:
            logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            return

    if assets == "retailclient":
        try:
            os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
        except:
            pass
    else:
        try:
            os.makedirs(f"{installloc}/")
        except:
            pass
    
    if savetype == "cdn":
        metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "backup":
        metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
    metafile_c = metafile.read()
    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
    metafiles = metafile_content["pieces"]["digests"]
    metafile_filenames = metafile_content["files"]
    metafile_padding = metafile_content["pad"]
    scantime = metafile_content["scanTime"]
    
    if savetype == "cdn":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
        else:
            text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{environment_wert}/{assets}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        if assets == "retailclient":
                            try:
                                os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{environment_wert}/{assets}/{file['name']}"
                        else:
                            try:
                                os.makedirs(f"{installloc}/")
                            except:
                                pass
                            target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/{environment_wert}/{assets}/pieces/{digest[:2]}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return

    elif savetype == "backup":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        if assets == "retailclient":
                            try:
                                os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{environment_wert}/{assets}/{file['name']}"
                        else:
                            try:
                                os.makedirs(f"{installloc}/")
                            except:
                                pass
                            target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return
    
    elif savetype == "root":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        if assets == "retailclient":
                            try:
                                os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{environment_wert}/{assets}/{file['name']}"
                        else:
                            try:
                                os.makedirs(f"{installloc}/")
                            except:
                                pass
                            target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return

    logbox.insert(END, "Installation finished!\n")
    try:
        log1_label.config(text=f"Installation finished!")
    except:
        pass
def install_launcher(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    global t1
    global t2
    
    if installloc == None:
        installloc = installzeile.get()
    logbox.insert(END, "\nStarting installation\n\n")#Press CTRL+C to stop.\n\n")
    log1_label.config(text=f"Installing...")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
            elif savetype == "backup":
                alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
        except:
            logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            return

    if assets == "retailclient":
        try:
            os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
        except:
            pass
    else:
        try:
            os.makedirs(f"{installloc}/")
        except:
            pass
    
    if savetype == "cdn":
        metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "launcher":
            shutil.copyfile(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "backup":
        metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "launcher":
            shutil.copyfile(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "launcher":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/{assets}.{environment_wert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{environment_wert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
    metafile_c = metafile.read()
    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
    metafiles = metafile_content["pieces"]["digests"]
    metafile_filenames = metafile_content["files"]
    metafile_padding = metafile_content["pad"]
    scantime = metafile_content["scanTime"]
    
    if savetype == "cdn":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
        else:
            text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
            last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/swtor/{assets}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        try:
                            os.makedirs(f"{installloc}/")
                        except:
                            pass
                        target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/swtor/{assets}/pieces/{digest[:2]}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return

    elif savetype == "backup":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        if assets == "retailclient":
                            try:
                                os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{environment_wert}/{assets}/{file['name']}"
                        else:
                            try:
                                os.makedirs(f"{installloc}/")
                            except:
                                pass
                            target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return
    
    elif savetype == "root":
        current_file = 0
        current_pad = 0
        file = metafile_filenames[current_file]

        fd = 0
        fdOffset = 0
        target = 0
        partial = 0

        total = 0
        padding = metafile_padding[current_pad]

        last_text = ""
        if assets == "retailclient":
            text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    logbox.insert(END, f"{text}\n")
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{digest}.solidpiece", 'rb')
                header = solidpiece.read(6)
                compression = header[5]
                if (compression == 2): # gzip
                    piece = gzip.decompress(solidpiece.read())
                else: # no compression
                    piece = solidpiece.read()
                solidpiece.close()

                pieceOffset = 0
                while (len(piece) - pieceOffset > 0):
                    if (fd == 0):
                        if assets == "retailclient":
                            try:
                                os.makedirs(f"{installloc}/{environment_wert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{environment_wert}/{assets}/{file['name']}"
                        else:
                            try:
                                os.makedirs(f"{installloc}/")
                            except:
                                pass
                            target = f"{installloc}/{file['name']}"
                        partial = target + '.solidpartial'
                        path = pathlib.Path(partial)
                        if (path.parent.exists() != True):
                            os.makedirs(os.path.dirname(path))
                        fd = open(partial, 'wb')
                    
                    size = file['size'] - fdOffset
                    if (size > len(piece) - pieceOffset):
                        size = len(piece) - pieceOffset

                    if (total + size > padding['offset']):
                        diff = padding['offset'] - total
                        size = diff
                        current_pad += 1
                        padding = metafile_content['pad'][current_pad]
                    total += size

                    start = fdOffset
                    remaining = size
                    written = 0
                    while (start + size > fdOffset):
                        written = fd.write(piece[pieceOffset:pieceOffset + remaining])
                        remaining -= written
                        pieceOffset += written
                        fdOffset += written

                    if (fdOffset == file['size']):
                        fd.close()
                        os.replace(partial, target)
                        if assets == "retailclient":
                            set_file_last_modified(f"{installloc}/{environment_wert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{environment_wert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    logbox.insert(END, f"{text}\n")
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            logbox.insert(END, "You stopped the installation!\n")
            try:
                log1_label.config(text=f"You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            logbox.insert(END, f"ERROR: Can't find {saveloc}/{digest}.solidpiece\n")
            try:
                log1_label.config(text=f"ERROR: Missing files")
            except:
                pass
            return

    logbox.insert(END, "Installation finished!\n")
    try:
        log1_label.config(text=f"Installation finished!")
    except:
        pass

def download_client_thr(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles, tn):
    progress1['value'] = 0
    progress2['value'] = 0
    progress3['value'] = 0
    progress4['value'] = 0
    progress5['value'] = 0
    dl_file1.config(text=f"")
    dl_file2.config(text=f"")
    dl_file3.config(text=f"")
    dl_file4.config(text=f"")
    dl_file5.config(text=f"")
    status1.config(text=f"0%\n0mb/s")
    status2.config(text=f"0%\n0mb/s")
    status3.config(text=f"0%\n0mb/s")
    status4.config(text=f"0%\n0mb/s")
    status5.config(text=f"0%\n0mb/s")

    for meta_file in metafiles:
        if True:
            if savetype == "cdn":
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/", bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/", bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/", bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/", bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/", bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                            
            elif savetype == "backup":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                            
            elif savetype == "root":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
    
    
def download_client(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global t1
    global t2
    global td1
    global td2
    global td3
    global td4
    global td5

    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    log1_label.config(text=f"Downloading...")
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if True:
        if catalog_metafile_hex is None:
            if savetype == "cdn":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{environment_wert}/{assets}/alias.json", f"{saveloc}/{environment_wert}/{assets}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            elif savetype == "backup":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{environment_wert}/{assets}/alias.json", f"{saveloc}/{environment_wert}/{assets}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                        
            elif savetype == "root":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                try:
                    os.makedirs(saveloc)
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/alias.json", f"{saveloc}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, saveloc, bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
                elif savetype == "backup":
                    alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
            except:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                return
            
        if savetype == "cdn":
            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
            
        elif savetype == "backup":
            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        elif savetype == "root":
            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/catalog.json", f"{saveloc}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/metafile.json", f"{saveloc}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        if savetype == "cdn":
            metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "backup":
            metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        logbox.insert(END, f"Download of {assets} {environment_wert} {selected} solidpieces started!\n\n")#Press CTRL+C to stop.\n")
        meta_files = []
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
            meta_files.append(meta_file)
        metafiles1 = meta_files[::5]
        metafiles2 = meta_files[1::5]
        metafiles3 = meta_files[2::5]
        metafiles4 = meta_files[3::5]
        metafiles5 = meta_files[4::5]

        td1 = Thread(target=download_client_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles1, 1))
        td1.start()
        td2 = Thread(target=download_client_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles2, 2))
        td2.start()
        td3 = Thread(target=download_client_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles3, 3))
        td3.start()
        td4 = Thread(target=download_client_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles4, 4))
        td4.start()
        td5 = Thread(target=download_client_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles5, 5))
        td5.start()
        td1.join()
        td2.join()
        td3.join()
        td4.join()
        td5.join()

def download_launcher_thr(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles, tn):
    progress1['value'] = 0
    progress2['value'] = 0
    progress3['value'] = 0
    progress4['value'] = 0
    progress5['value'] = 0
    dl_file1.config(text=f"")
    dl_file2.config(text=f"")
    dl_file3.config(text=f"")
    dl_file4.config(text=f"")
    dl_file5.config(text=f"")
    status1.config(text=f"0%\n0mb/s")
    status2.config(text=f"0%\n0mb/s")
    status3.config(text=f"0%\n0mb/s")
    status4.config(text=f"0%\n0mb/s")
    status5.config(text=f"0%\n0mb/s")

    for meta_file in metafiles:
        if True:
            if savetype == "cdn":
                if not os.path.exists(f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                                    
            elif savetype == "backup":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4= int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                            
            elif savetype == "root":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4= int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True

def download_launcher(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global t1
    global t2
    global td1
    global td2
    global td3
    global td4
    global td5
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    log1_label.config(text=f"Downloading...")
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if True:
        if catalog_metafile_hex is None:
            if savetype == "cdn":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/swtor/{assets}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/swtor/{assets}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/swtor/{assets}/alias.json", f"{saveloc}/swtor/{assets}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/swtor/{assets}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/swtor/{assets}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            elif savetype == "backup":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/swtor/{assets}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/swtor/{assets}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/swtor/{assets}/alias.json", f"{saveloc}/swtor/{assets}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/swtor/{assets}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/swtor/{assets}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                        
            elif savetype == "root":
                logbox.insert(END, f"Download of {assets} {environment_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                try:
                    os.makedirs(saveloc)
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/alias.json", f"{saveloc}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, saveloc, bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                elif savetype == "backup":
                    alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
            except:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                return
            
        if savetype == "cdn":
            try:
                os.makedirs(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
            
        elif savetype == "backup":
            try:
                os.makedirs(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        elif savetype == "root":
            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/catalog.json", f"{saveloc}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/metafile.json", f"{saveloc}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        if savetype == "cdn":
            metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "backup":
            metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        logbox.insert(END, f"Download of {assets} {environment_wert} {selected} solidpieces started!\n\n")#Press CTRL+C to stop.\n")
        meta_files = []
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
            meta_files.append(meta_file)
        metafiles1 = meta_files[::5]
        metafiles2 = meta_files[1::5]
        metafiles3 = meta_files[2::5]
        metafiles4 = meta_files[3::5]
        metafiles5 = meta_files[4::5]

        td1 = Thread(target=download_launcher_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles1, 1))
        td1.start()
        td2 = Thread(target=download_launcher_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles2, 2))
        td2.start()
        td3 = Thread(target=download_launcher_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles3, 3))
        td3.start()
        td4 = Thread(target=download_launcher_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles4, 4))
        td4.start()
        td5 = Thread(target=download_launcher_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles5, 5))
        td5.start()
        td1.join()
        td2.join()
        td3.join()
        td4.join()
        td5.join()

def download_files_thr(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles, tn):
    progress1['value'] = 0
    progress2['value'] = 0
    progress3['value'] = 0
    progress4['value'] = 0
    progress5['value'] = 0
    dl_file1.config(text=f"")
    dl_file2.config(text=f"")
    dl_file3.config(text=f"")
    dl_file4.config(text=f"")
    dl_file5.config(text=f"")
    status1.config(text=f"0%\n0mb/s")
    status2.config(text=f"0%\n0mb/s")
    status3.config(text=f"0%\n0mb/s")
    status4.config(text=f"0%\n0mb/s")
    status5.config(text=f"0%\n0mb/s")
    for meta_file in metafiles:
        if True:
            if savetype == "cdn":
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/", bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/", bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/", bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/", bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/", bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                            
            elif savetype == "backup":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True
                            
            if savetype == "root":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            if tn == 1:
                                dl_file1.config(text=f"Downloading:\n{url}")
                                zeitx1 = int(time.time())
                                sekunden1 = 0
                                wget.download(url, saveloc, bar=bar1_progress)
                            if tn == 2:
                                dl_file2.config(text=f"Downloading:\n{url}")
                                zeitx2 = int(time.time())
                                sekunden2 = 0
                                wget.download(url, saveloc, bar=bar2_progress)
                            if tn == 3:
                                dl_file3.config(text=f"Downloading:\n{url}")
                                zeitx3 = int(time.time())
                                sekunden3 = 0
                                wget.download(url, saveloc, bar=bar3_progress)
                            if tn == 4:
                                dl_file4.config(text=f"Downloading:\n{url}")
                                zeitx4 = int(time.time())
                                sekunden4 = 0
                                wget.download(url, saveloc, bar=bar4_progress)
                            if tn == 5:
                                dl_file5.config(text=f"Downloading:\n{url}")
                                zeitx5 = int(time.time())
                                sekunden5 = 0
                                wget.download(url, saveloc, bar=bar5_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    logbox.insert(END, "\nSolidpiece not found.\nTrying again...\n\n")
                                    lost = True

def download_files(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global t1
    global t2
    global td1
    global td2
    global td3
    global td4
    global td5
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    log1_label.config(text=f"Downloading...")
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if catalog_metafile_hex is None:
        if not language_wert == "client":
            if savetype == "cdn":
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json")
                                break
                logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                        
            elif savetype == "backup":
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json")
                                break
                logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            elif savetype == "root":
                try:
                    os.makedirs(saveloc)
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/alias.json", f"{saveloc}/alias_old_{i}.json")
                                break
                logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} alias.json started!\n\n")#Press CTRL+C to stop.\n")
                if not os.path.exists(f"{saveloc}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, saveloc, bar=bar1_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json\n\n")
                            log1_label.config(text=f"Downloading...")
                            break
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                    lost = True
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
                elif savetype == "backup":
                    alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}_{language_wert}.{environment_wert}"]
            except Exception as e:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                return

    if True:
        if savetype == "cdn":
            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        elif savetype == "backup":
            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/", bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/", bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

        elif savetype == "root":
            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/catalog.json", f"{saveloc}/catalog_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} catalog.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar2_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/catalog/{catalog_metafile_hex}/catalog.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return

            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/metafile.json", f"{saveloc}/metafile_old_{i}.json")
                        break
            logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} metafile.json started!\n\n")#Press CTRL+C to stop.\n")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx3 = int(time.time())
                        sekunden3 = 0
                        dl_file3.config(text=f"Downloading:\n{url}")
                        wget.download(url, saveloc, bar=bar3_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        logbox.insert(END, f"\nDownloaded: http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json\n\n")
                        log1_label.config(text=f"Downloading...")
                        break
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                lost = True
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                    

        if savetype == "cdn":
            metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "backup":
            metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        #complete_size = 0
        #for file in metafile_content["files"]:
        #    complete_size += file["size"]
        #print(complete_size)
        logbox.insert(END, f"Download of {assets} {environment_wert} {language_wert} {selected} solidpieces started!\n\n")#Press CTRL+C to stop.\n")
        meta_files = []
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
            meta_files.append(meta_file)
        metafiles1 = meta_files[::5]
        metafiles2 = meta_files[1::5]
        metafiles3 = meta_files[2::5]
        metafiles4 = meta_files[3::5]
        metafiles5 = meta_files[4::5]

        td1 = Thread(target=download_files_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles1, 1))
        td1.start()
        td2 = Thread(target=download_files_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles2, 2))
        td2.start()
        td3 = Thread(target=download_files_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles3, 3))
        td3.start()
        td4 = Thread(target=download_files_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles4, 4))
        td4.start()
        td5 = Thread(target=download_files_thr, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex, metafiles5, 5))
        td5.start()
        td1.join()
        td2.join()
        td3.join()
        td4.join()
        td5.join()

if len(sys.argv) > 1:
    for i in sys.argv:
        if i.lower() == "product=assets":
            assets = "assets"
        if i.lower() == "product=movies":
            assets = "movies"
        if i.lower() == "product=retailclient":
            assets = "retailclient"
        if i.lower() == "product=launcher":
            assets = "launcher"

        if i.lower() == "env=swtor":
            environment_wert = "swtor"
        if i.lower() == "env=publictest":
            environment_wert = "publictest"
        if i.lower() == "env=launcher":
            environment_wert = "launcher"
        if i.lower() == "env=test_001":
            environment_wert = "test_001"
        if i.lower() == "env=test_prod":
            environment_wert = "test_PROD"

        if i.lower() == "lang=shared":
            language_wert = "shared"
        if i.lower() == "lang=de_de":
            language_wert = "de_de"
        if i.lower() == "lang=en_us":
            language_wert = "en_us"
        if i.lower() == "lang=fr_fr":
            language_wert = "fr_fr"

        if i.lower() == "structure=cdn":
            savetype = "cdn"
        if i.lower() == "structure=backup":
            savetype = "backup"
        if i.lower() == "structure=root":
            savetype = "root"

        if i.lower() == "checknew=true":
            allow_newversion_check_f = 1
        if i.lower() == "checknew=false":
            allow_newversion_check_f = 0

        if i.lower().startswith("save="):
            saveloc = i.lower().replace("save=","")

        installloc = ""
        if i.lower().startswith("install="):
            installloc = i.lower().replace("install=","")

    allow_installation = False
    if not installloc == "":
        allow_installation = True            

    try:
        if True:
            if True:
                if True:
                    if True:
                        if assets == "retailclient":
                            t1 = Thread(target=download_client, args=(saveloc, language_wert, 0, environment_wert, "0", assets, savetype, allow_newversion_check_f, None))
                            t1.start()
                            t1.join()
                            if allow_installation:
                                t2 = Thread(target=install_client, args=(saveloc, language_wert, 0, environment_wert, 0, assets, savetype, installloc, None))
                                t2.start()
                                t2.join()
                            else:
                                while t1.is_alive():
                                    pass
                                print("Download finished!\n")
                                try:
                                    log1_label.config(text=f"Download finished!")
                                except:
                                    pass
                            sys.exit()
                        elif assets == "launcher":
                            t1 = Thread(target=download_launcher, args=(saveloc, language_wert, 0, environment_wert, "0", assets, savetype, allow_newversion_check_f, None))
                            t1.start()
                            t1.join()
                            if allow_installation:
                                t2 = Thread(target=install_launcher, args=(saveloc, language_wert, 0, environment_wert, 0, assets, savetype, installloc, None))
                                t2.start()
                                t2.join()
                            else:
                                while t1.is_alive():
                                    pass
                                print("Download finished!\n")
                                try:
                                    log1_label.config(text=f"Download finished!")
                                except:
                                    pass
                            sys.exit()
                        if True:
                            if True:
                                t1 = Thread(target=download_files, args=(saveloc, language_wert, 0, environment_wert, "0", assets, savetype, allow_newversion_check_f, None))
                                t1.start()
                                t1.join()
                                if allow_installation:
                                    t2 = Thread(target=install_files, args=(saveloc, language_wert, 0, environment_wert, 0, assets, savetype, installloc, None))
                                    t2.start()
                                    t2.join()
                                else:
                                    while t1.is_alive():
                                        pass
                                    print("Download finished!\n")
                                    try:
                                        log1_label.config(text=f"Download finished!")
                                    except:
                                        pass
                                sys.exit()
                sys.exit()
    except Exception as e:
        print(f"{os.path.basename(sys.argv[0])} [product=] [env=] [lang=] [structure=] [save=] ([install=])"
                "\n\n"
                "SWTOR Patch Downloader & Installer\n"
                "product - assets/movies/retailclient/launcher\n"
                "env - swtor/publictest/launcher/test_001/test_prod\n"
                "lang - shared/en_us/de_de/fr_fr\n"
                "checknew - true/false"
                "structure - cdn/backup/root\n"
                "save - Location to save (use / instead of \\)\n"
                "install - OPTIONAL Location to install (use / instead of \\)\n"
                f"\nExample: {os.path.basename(sys.argv[0])} product=assets env=swtor lang=shared checknew=true structure=cdn save=d:/temp install=d:/install")
    sys.exit()
#data = {}
#data['version'] = []
#data['version'].append({
#    'name': "publictest"})
#data['build'] = []
#data['build'].append({
#    'name': 'XtoY'})
#data['saveto'] = []
#data['saveto'].append({
#    'name': 'd:\temp'})
#data['lang'] = []
#data['lang'].append({
#    'name': 'shared'})

#with open('settings.json', 'w') as outfile:
#    json.dump(data, outfile)

#data = {}
#data['devmode'] = []
#data['devmode'].append({
#    'name': 'true'})

#with open('devmode.json', 'w') as outfile:
#    json.dump(data, outfile)

logbox.insert(END, "SWTOR Patch Downloader & Installer\n\n")

def check_date():
    global t1
    global t2
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    allow_newversion_check_f = allow_newversion_check_var.get()
    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    #saveloc = os.getcwd()
    saveloc = ordnerzeile.get()
    saveloc = saveloc.rstrip()
    saveloc2 = ordnerzeile.get()
    if saveloc == "":
        try:
            log1_label.config(text=f"Please enter a save-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter a save-path!\n\n")
        return
    if not os.path.exists(saveloc):
        try:
            log1_label.config(text=f"This save-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis save-path doesn't exist!\n\n")
        return
    if allow_custom_hex_var.get() == 1:
        catalog_metafile_hex = hex_zeile.get()
        oldversion = True
    else:
        catalog_metafile_hex = None
        oldversion = False
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': environment_wert})
        data['build'] = []
        data['build'].append({
            'name': uwert})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        data['assets'] = []
        data['assets'].append({
            'name': assets})
        data['lang'] = []
        data['lang'].append({
            'name': language_wert})
        data['save_type'] = []
        data['save_type'].append({
            'name': savetype})
        data['allow_installation_check'] = []
        data['allow_installation_check'].append({
            'name': bool(allow_installation_check_var.get())})
        data['allow_newversion_check'] = []
        data['allow_newversion_check'].append({
            'name': bool(allow_newversion_check_var.get())})
        data['installto'] = []
        data['installto'].append({
            'name': installloc})
        
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
        if not oldversion:
            try:
                selected = version_box.get(version_box.curselection()[0])
                index = descriptions.index(selected)
                catalog_metafile_hex = ids[index]
                oldversion = True
            except:
                oldversion = False

        if True:#if savetype == "cdn" or savetype == "backup":
            if not assets == "launcher" and not assets == "retailclient":
                if not oldversion:
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                    if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                        md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                        try:
                            md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json").read().encode('utf-8')).hexdigest()
                        except:
                            md5_old = md5_new
                        if not md5_old == md5_new:
                            for i in range(1, 99999):
                                if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json"):
                                    os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json")
                                    break
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
                        except:
                            pass
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}_{language_wert}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                                    
                                    
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/", bar=bar2_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                                    
                metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                scantime = metafile_content["scanTime"]
                dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
                logbox.insert(END, f"\nVersion created on: {dt}\n")
                try:
                    log1_label.config(text=f"Version created on: {dt}")
                except:
                    pass

            elif assets == "retailclient":
                if not oldversion:
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                                    
                                    
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar2_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                                    
                metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                scantime = metafile_content["scanTime"]
                dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
                logbox.insert(END, f"\nVersion created on: {dt}\n")
                try:
                    log1_label.config(text=f"Version created on: {dt}")
                except:
                    pass

            elif assets == "launcher":
                if not oldversion:
                    if not os.path.exists(f"{saveloc}/swtor/{assets}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/swtor/{assets}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                                    
                                    
                if not os.path.exists(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx2 = int(time.time())
                        sekunden2 = 0
                        dl_file2.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar2_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nTrying again...\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                                    
                metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                scantime = metafile_content["scanTime"]
                dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
                logbox.insert(END, f"\nVersion created on: {dt}\n")
                try:
                    log1_label.config(text=f"Version created on: {dt}")
                except:
                    pass
        
def check_date_thr():
    t1 = Thread(target=check_date)
    t1.start()

def file_save():
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        ordnerzeile.delete(0, END)
        ordnerzeile.insert(0, folder_selected)

def install_save():
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        installzeile.delete(0, END)
        installzeile.insert(0, folder_selected)

def button_action():
    global t1
    global t2
    try:
        selected = version_box.get(version_box.curselection()[0])
        install_old_version()
        return
    except:
        pass
    
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    saveloc = saveloc.rstrip()
    will_install = allow_installation_check_var.get()
    if saveloc == "":
        try:
            log1_label.config(text=f"Please enter a save-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter a save-path!\n\n")
        return
    if not os.path.exists(saveloc):
        try:
            log1_label.config(text=f"This save-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis save-path doesn't exist!\n\n")
        return
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if installloc == "" and will_install:
        try:
            log1_label.config(text=f"Please enter an installation-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter an installation-path!\n\n")
        return
    if not os.path.exists(installloc) and will_install:
        try:
            log1_label.config(text=f"This installation-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis installation-path doesn't exist!\n\n")
        return
    allow_newversion_check_f = allow_newversion_check_var.get()
    if allow_custom_hex_var.get() == 1:
        catalog_metafile_hex = hex_zeile.get()
    else:
        catalog_metafile_hex = None
    if not os.path.isdir(saveloc):
        try:
            os.makedirs(saveloc)
        except:
            pass
    yes = False
    #if vnummer == "":
    #    log1_label.config(text=f"Please enter the version number,\nyou want to download!")
    #    return
    if saveloc == "":
        log1_label.config(text=f"Please enter the location,\nwhere you want to save the files!")
        return
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': environment_wert})
        data['build'] = []
        data['build'].append({
            'name': uwert})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc})
        data['assets'] = []
        data['assets'].append({
            'name': assets})
        data['lang'] = []
        data['lang'].append({
            'name': language_wert})
        data['save_type'] = []
        data['save_type'].append({
            'name': savetype})
        data['allow_installation_check'] = []
        data['allow_installation_check'].append({
            'name': bool(allow_installation_check_var.get())})
        data['allow_newversion_check'] = []
        data['allow_newversion_check'].append({
            'name': bool(allow_newversion_check_var.get())})
        data['installto'] = []
        data['installto'].append({
            'name': installloc})
        
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    
    vnummerx = 0
    if assets == "retailclient":
        t1 = Thread(target=download_client, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex))
        t1.start()
        t1.join()
        if allow_installation_check_var.get() == 1:
            t2 = Thread(target=install_client, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
            t2.start()
            t2.join()
        else:
            logbox.insert(END, "Download finished!\n")
            log1_label.config(text=f"Download finished!")
        return
    elif assets == "launcher":
        t1 = Thread(target=download_launcher, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex))
        t1.start()
        t1.join()
        if allow_installation_check_var.get() == 1:
            t2 = Thread(target=install_launcher, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
            t2.start()
            t2.join()
        else:
            logbox.insert(END, "Download finished!\n")
            log1_label.config(text=f"Download finished!")
        return
    if True:
        if True:
            t1 = Thread(target=download_files, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex))
            t1.start()
            t1.join()
            if allow_installation_check_var.get() == 1:
                try:
                    t2 = Thread(target=install_files, args=(saveloc, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
                    t2.start()
                    t2.join()
                except:
                    pass
            else:
                logbox.insert(END, "Download finished!\n")
                log1_label.config(text=f"Download finished!")
            return

def button_action_thr():
    t1 = Thread(target=button_action)
    t1.start()

def search_versions():
    global t1
    global t2
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    global descriptions
    global ids

    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    saveloc2 = ordnerzeile.get()
    if saveloc == "":
        try:
            log1_label.config(text=f"Please enter a save-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter a save-path!\n\n")
        return
    if not os.path.exists(saveloc):
        try:
            log1_label.config(text=f"This save-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis save-path doesn't exist!\n\n")
        return
    
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': environment_wert})
        data['build'] = []
        data['build'].append({
            'name': uwert})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        data['assets'] = []
        data['assets'].append({
            'name': assets})
        data['lang'] = []
        data['lang'].append({
            'name': language_wert})
        data['save_type'] = []
        data['save_type'].append({
            'name': savetype})
        data['allow_installation_check'] = []
        data['allow_installation_check'].append({
            'name': bool(allow_installation_check_var.get())})
        data['allow_newversion_check'] = []
        data['allow_newversion_check'].append({
            'name': bool(allow_newversion_check_var.get())})
        data['installto'] = []
        data['installto'].append({
            'name': installloc})
        
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
    
    if assets == "assets" or assets == "movies":
        try:
            os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
        except:
            pass
        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json"
        try:
            creation_time_new = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
        except Exception as e:
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            logbox.insert(END, "\nVersion not found!\n\n")
            return
        try:
            creation_time_old = os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json")
        except:
            creation_time_old = creation_time_new
        if creation_time_old < creation_time_new:
            os.remove(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json")
        if True:
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json") == True:
                try:
                    zeitx1 = int(time.time())
                    sekunden1 = 0
                    dl_file1.config(text=f"Downloading:\n{url}")
                    wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                    logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json", creation_time)
                except KeyboardInterrupt:
                    logbox.insert(END, "\nYou stopped the download!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                        try:
                            log1_label.config(text=f"Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        version_box.delete(0, tkr.END)
                        logbox.insert(END, "\nVersion not found!\n\n")
                        return
		
            try:
                history = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/{assets}_{language_wert}.history.json", "r")
                history_c = history.read()
                history_content = jwt.decode(history_c, algorithms=["RS256"], options={"verify_signature": False})
                history_content = history_content['history']

                descriptions = []
                ids = []
                version_box.delete(0, tkr.END)
                for part in history_content:
                    version_number = ""
                    for item in itemlist_patches[environment_wert]:
                        if item.attributes["version"].value == part["version"]:
                            version_number = f' - {item.attributes["version_number"].value}'
                            if version_number == f' - -':
                                version_number = ""
                    descriptions.append(f'{part["description"]}{version_number}')
                    ids.append(part["id"])
                    version_box.insert(tkr.END, f'{part["description"]}{version_number}')
                log1_label.config(text=f"Found previous versions!")
                return
            except Exception as e:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                version_box.delete(0, tkr.END)
                return


    elif assets == "retailclient":
        try:
            os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
        except:
            pass
        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/{assets}.history.json"
        try:
            creation_time_new = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
        except:
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            logbox.insert(END, "\nVersion not found!\n\n")
            return
        try:
            creation_time_old = os.path.getmtime(f"{saveloc}/{environment_wert}/{assets}/{assets}.history.json")
        except:
            creation_time_old = creation_time_new
        if creation_time_old < creation_time_new:
            os.remove(f"{saveloc}/{environment_wert}/{assets}/{assets}.history.json")
        if True:
            if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/{assets}.history.json") == True:
                try:
                    zeitx1 = int(time.time())
                    sekunden1 = 0
                    dl_file1.config(text=f"Downloading:\n{url}")
                    wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                    logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/{environment_wert}/{assets}/{assets}.history.json", creation_time)
                except KeyboardInterrupt:
                    logbox.insert(END, "\nYou stopped the download!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                        try:
                            log1_label.config(text=f"Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        version_box.delete(0, tkr.END)
                        logbox.insert(END, "\nVersion not found!\n\n")
                        return
				
            try:
                history = open(f"{saveloc}/{environment_wert}/{assets}/{assets}.history.json", "r")
                history_c = history.read()
                history_content = jwt.decode(history_c, algorithms=["RS256"], options={"verify_signature": False})
                history_content = history_content['history']

                descriptions = []
                ids = []
                version_box.delete(0, tkr.END)
                for part in history_content:
                    version_number = ""
                    for item in itemlist_patches[environment_wert]:
                        if item.attributes["version"].value == part["version"]:
                            version_number = f' - {item.attributes["version_number"].value}'
                            if version_number == f' - -':
                                version_number = ""
                    descriptions.append(f'{part["description"]}{version_number}')
                    ids.append(part["id"])
                    version_box.insert(tkr.END, f'{part["description"]}{version_number}')
                log1_label.config(text=f"Found previous versions!")
                return
            except Exception as e:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                version_box.delete(0, tkr.END)
                return

    elif assets == "launcher":
        try:
            os.makedirs(f"{saveloc}/swtor/{assets}/")
        except:
            pass
        url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/{assets}.history.json"
        try:
            creation_time_new = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
        except:
            try:
                log1_label.config(text=f"Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            logbox.insert(END, "\nVersion not found!\n\n")
            return
        try:
            creation_time_old = os.path.getmtime(f"{saveloc}/swtor/{assets}/{assets}.history.json")
        except Exception as e:
            creation_time_old = creation_time_new
        if creation_time_old < creation_time_new:
            os.remove(f"{saveloc}/swtor/{assets}/{assets}.history.json")
        if True:
            if not os.path.exists(f"{saveloc}/swtor/{assets}/{assets}.history.json") == True:
                try:
                    zeitx1 = int(time.time())
                    sekunden1 = 0
                    dl_file1.config(text=f"Downloading:\n{url}")
                    wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                    logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/swtor/{assets}/{assets}.history.json", creation_time)
                except KeyboardInterrupt:
                    logbox.insert(END, "\nYou stopped the download!\n")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                        try:
                            log1_label.config(text=f"Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        logbox.insert(END, "\nVersion not found!\n\n")
                        return
				
            try:
                history = open(f"{saveloc}/swtor/{assets}/{assets}.history.json", "r")
                history_c = history.read()
                history_content = jwt.decode(history_c, algorithms=["RS256"], options={"verify_signature": False})
                history_content = history_content['history']

                descriptions = []
                ids = []
                version_box.delete(0, tkr.END)
                for part in history_content:
                    version_number = ""
                    for item in itemlist_patches[environment_wert]:
                        if item.attributes["version"].value == part["version"]:
                            version_number = f' - {item.attributes["version_number"].value}'
                            if version_number == f' - -':
                                version_number = ""
                    descriptions.append(f'{part["description"]}{version_number}')
                    ids.append(part["id"])
                    version_box.insert(tkr.END, f'{part["description"]}{version_number}')
                log1_label.config(text=f"Found previous versions!")
                return
            except Exception as e:
                logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                try:
                    log1_label.config(text=f"Version not found!")
                except:
                    pass
                version_box.delete(0, tkr.END)
                return

def search_versions_thr():
    t1 = Thread(target=search_versions)
    t1.start()

def check_hex():
    global t1
    global t2
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    allow_newversion_check_f = allow_newversion_check_var.get()
    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    #saveloc = os.getcwd()
    saveloc = ordnerzeile.get()
    saveloc2 = ordnerzeile.get()
    if saveloc == "":
        try:
            log1_label.config(text=f"Please enter a save-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter a save-path!\n\n")
        return
    if not os.path.exists(saveloc):
        try:
            log1_label.config(text=f"This save-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis save-path doesn't exist!\n\n")
        return
    if allow_custom_hex_var.get() == 1:
        catalog_metafile_hex = hex_zeile.get()
        oldversion = True
    else:
        catalog_metafile_hex = None
        oldversion = False
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': environment_wert})
        data['build'] = []
        data['build'].append({
            'name': uwert})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        data['assets'] = []
        data['assets'].append({
            'name': assets})
        data['lang'] = []
        data['lang'].append({
            'name': language_wert})
        data['save_type'] = []
        data['save_type'].append({
            'name': savetype})
        data['allow_installation_check'] = []
        data['allow_installation_check'].append({
            'name': bool(allow_installation_check_var.get())})
        data['allow_newversion_check'] = []
        data['allow_newversion_check'].append({
            'name': bool(allow_newversion_check_var.get())})
        data['installto'] = []
        data['installto'].append({
            'name': installloc})
        
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
        if not oldversion:
            try:
                selected = version_box.get(version_box.curselection()[0])
                index = descriptions.index(selected)
                catalog_metafile_hex = ids[index]
                oldversion = True
            except:
                oldversion = False
        if not oldversion:
            if assets == "assets" or assets == "movies":
                url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
                    except:
                        pass
                    try:
                        zeitx1 = int(time.time())
                        sekunden1 = 0
                        dl_file1.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}_{language_wert}.{environment_wert}"]
                except:
                    logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                    try:
                        log1_label.config(text=f"Version not found!")
                    except:
                        pass
                    return

            elif assets == "retailclient":
                if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                    try:
                        zeitx1 = int(time.time())
                        sekunden1 = 0
                        dl_file1.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                except:
                    logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                    try:
                        log1_label.config(text=f"Version not found!")
                    except:
                        pass
                    return

            elif assets == "launcher":
                if not os.path.exists(f"{saveloc}/swtor/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/swtor/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                    try:
                        zeitx1 = int(time.time())
                        sekunden1 = 0
                        dl_file1.config(text=f"Downloading:\n{url}")
                        wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                        logbox.insert(END, f"\nDownloaded: {url}\n\n")
                    except KeyboardInterrupt:
                        logbox.insert(END, "\nYou stopped the download!\n")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                            try:
                                log1_label.config(text=f"Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text=f"Version not found!")
                            except:
                                pass
                            logbox.insert(END, "\nVersion not found!\n\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                except:
                    logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                    try:
                        log1_label.config(text=f"Version not found!")
                    except:
                        pass
                    return
                
        log1_label.config(text=f"Hex-id: {catalog_metafile_hex}")
        logbox.insert(END, f"\nHex-id: {catalog_metafile_hex}\n")

def check_hex_thr():
    t1 = Thread(target=check_hex)
    t1.start()

def check_size():
    global t1
    global t2
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5
    allow_newversion_check_f = allow_newversion_check_var.get()
    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    #saveloc = os.getcwd()
    saveloc = ordnerzeile.get().rstrip()
    saveloc2 = ordnerzeile.get()
    if saveloc == "":
        try:
            log1_label.config(text=f"Please enter a save-path!")
        except:
            pass
        logbox.insert(END, "\nPlease enter a save-path!\n\n")
        return
    if not os.path.exists(saveloc):
        try:
            log1_label.config(text=f"This save-path doesn't exist!")
        except:
            pass
        logbox.insert(END, "\nThis save-path doesn't exist!\n\n")
        return
    if allow_custom_hex_var.get() == 1:
        catalog_metafile_hex = hex_zeile.get()
        oldversion = True
    else:
        catalog_metafile_hex = None
        oldversion = False
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': environment_wert})
        data['build'] = []
        data['build'].append({
            'name': uwert})
        data['saveto'] = []
        data['saveto'].append({
            'name': saveloc2})
        data['assets'] = []
        data['assets'].append({
            'name': assets})
        data['lang'] = []
        data['lang'].append({
            'name': language_wert})
        data['save_type'] = []
        data['save_type'].append({
            'name': savetype})
        data['allow_installation_check'] = []
        data['allow_installation_check'].append({
            'name': bool(allow_installation_check_var.get())})
        data['allow_newversion_check'] = []
        data['allow_newversion_check'].append({
            'name': bool(allow_newversion_check_var.get())})
        data['installto'] = []
        data['installto'].append({
            'name': installloc})
        
        with open('settings.json', 'w') as outfile:
            json.dump(data, outfile)
        if not oldversion:
            try:
                selected = version_box.get(version_box.curselection()[0])
                index = descriptions.index(selected)
                catalog_metafile_hex = ids[index]
                oldversion = True
            except:
                oldversion = False
        download_size = 0
        if True:#if savetype == "cdn" or savetype == "backup":
            if assets == "assets" or assets == "movies":
                if not oldversion:
                    url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/alias.json"
                    if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                        md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                        try:
                            md5_old = hashlib.md5(open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json").read().encode('utf-8')).hexdigest()
                        except:
                            md5_old = md5_new
                        if not md5_old == md5_new:
                            for i in range(1, 99999):
                                if not os.path.isfile(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json"):
                                    os.rename(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias_old_{i}.json")
                                    break
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/")
                        except:
                            pass
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}_{language_wert}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                if True:
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                                        
                    metafile = open(f"{saveloc}/{environment_wert}/{assets}_{language_wert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                    metafile_c = metafile.read()
                    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                    for file in metafile_content["files"]:
                        download_size += file["size"]
                    download_size = locale.format_string("%d", download_size, grouping=True)
                    logbox.insert(END, f"\nSize: {download_size} Bytes\n")
                    try:
                        log1_label.config(text=f"Size: {download_size} Bytes")
                    except:
                        pass

            elif assets == "retailclient":
                if not oldversion:
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/alias.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/{environment_wert}/{assets}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                                    
                if True:
                    if not os.path.exists(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                                        
                    metafile = open(f"{saveloc}/{environment_wert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                    metafile_c = metafile.read()
                    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                    for file in metafile_content["files"]:
                        download_size += file["size"]
                    download_size = locale.format_string("%d", download_size, grouping=True)
                    logbox.insert(END, f"\nSize: {download_size} Bytes\n")
                    try:
                        log1_label.config(text=f"Size: {download_size} Bytes")
                    except:
                        pass

            
            elif assets == "launcher":
                if not oldversion:
                    if not os.path.exists(f"{saveloc}/swtor/{assets}/alias.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/swtor/{assets}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                        
                    try:
                        alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                        alias_c = alias.read()
                        alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                        catalog_metafile_hex = alias_content[f"{assets}.{environment_wert}"]
                    except:
                        logbox.insert(END, "\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.\n")
                        try:
                            log1_label.config(text=f"Version not found!")
                        except:
                            pass
                        return
                if True:
                    if not os.path.exists(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                        try:
                            os.makedirs(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/")
                        except:
                            pass
                        url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                        try:
                            zeitx1 = int(time.time())
                            sekunden1 = 0
                            dl_file1.config(text=f"Downloading:\n{url}")
                            wget.download(url, f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar1_progress)
                            logbox.insert(END, f"\nDownloaded: {url}\n\n")
                        except KeyboardInterrupt:
                            logbox.insert(END, "\nYou stopped the download!\n")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                logbox.insert(END, "\nConnection lost.\nPlease try again!\n\n")
                                try:
                                    log1_label.config(text=f"Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text=f"Version not found!")
                                except:
                                    pass
                                logbox.insert(END, "\nVersion not found!\n\n")
                                return
                                                        
                    metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                    metafile_c = metafile.read()
                    metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                    for file in metafile_content["files"]:
                        download_size += file["size"]
                    download_size = locale.format_string("%d", download_size, grouping=True)
                    logbox.insert(END, f"\nSize: {download_size} Bytes\n")
                    try:
                        log1_label.config(text=f"Size: {download_size} Bytes")
                    except:
                        pass
            
            
def check_size_thr():
    t1 = Thread(target=check_size)
    t1.start()

def check_if_running():
    global t1
    global t2
    while True:
        time.sleep(0.25)
        try:
            if t1.is_alive() or t2.is_alive():
                welcom_button.config(state=DISABLED)
                exit_button.config(state=DISABLED)
                hex_id_button.config(state=DISABLED)
                size_button.config(state=DISABLED)
            else:
                welcom_button.config(state=NORMAL)
                exit_button.config(state=NORMAL)
                hex_id_button.config(state=NORMAL)
                size_button.config(state=NORMAL)
                progress1['value'] = 0
                progress2['value'] = 0
                progress3['value'] = 0
                progress4['value'] = 0
                progress5['value'] = 0
                dl_file1.config(text=f"")
                dl_file2.config(text=f"")
                dl_file3.config(text=f"")
                dl_file4.config(text=f"")
                dl_file5.config(text=f"")
                status1.config(text=f"0%\n0mb/s")
                status2.config(text=f"0%\n0mb/s")
                status3.config(text=f"0%\n0mb/s")
                status4.config(text=f"0%\n0mb/s")
                status5.config(text=f"0%\n0mb/s")
                
        except:
            welcom_button.config(state=NORMAL)
            exit_button.config(state=NORMAL)
            hex_id_button.config(state=NORMAL)
            size_button.config(state=NORMAL)
            progress1['value'] = 0
            progress2['value'] = 0
            progress3['value'] = 0
            progress4['value'] = 0
            progress5['value'] = 0
            dl_file1.config(text=f"")
            dl_file2.config(text=f"")
            dl_file3.config(text=f"")
            dl_file4.config(text=f"")
            dl_file5.config(text=f"")
            status1.config(text=f"0%\n0mb/s")
            status2.config(text=f"0%\n0mb/s")
            status3.config(text=f"0%\n0mb/s")
            status4.config(text=f"0%\n0mb/s")
            status5.config(text=f"0%\n0mb/s")

ordnerzeile = tkr.Entry(fenster,width=50)

def install_old_version():
    global t1
    global t2
    global zeitx1
    global zeitx2
    global zeitx3
    global zeitx4
    global zeitx5
    global sekunden1
    global sekunden2
    global sekunden3
    global sekunden4
    global sekunden5

    selected = version_box.get(version_box.curselection()[0])
    index = descriptions.index(selected)
    catalog_metafile_hex = ids[index]

    environment_wert = varA.get()
    uwert = varB.get()
    language_wert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    saveloc = os.getcwd()
    saveloc2 = ordnerzeile.get()
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()

    vnummerx = 0

    if assets == "retailclient":
        t1 = Thread(target=download_client, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, 0, catalog_metafile_hex))
        t1.start()
        t1.join()
        if allow_installation_check_var.get() == 1:
            t2 = Thread(target=install_client, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
            t2.start()
            t2.join()
        else:
            logbox.insert(END, "Download finished!\n")
            log1_label.config(text=f"Download finished!")
        return
    elif assets == "launcher":
        t1 = Thread(target=download_launcher, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, 0, catalog_metafile_hex))
        t1.start()
        t1.join()
        if allow_installation_check_var.get() == 1:
            t2 = Thread(target=install_launcher, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
            t2.start()
            t2.join()
        else:
            logbox.insert(END, "Download finished!\n")
            log1_label.config(text=f"Download finished!")
        return
    #if environment_wert == "swtor" or environment_wert == "publictest":
    if True:
        #if uwert == "XtoY":
        if True:
            t1 = Thread(target=download_files, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, 0, catalog_metafile_hex))
            t1.start()
            t1.join()
            if allow_installation_check_var.get() == 1:
                t2 = Thread(target=install_files, args=(saveloc2, language_wert, vnummerx, environment_wert, vnummer, assets, savetype, None, catalog_metafile_hex))
                t2.start()
                t2.join()
            else:
                logbox.insert(END, "Download finished!\n")
                log1_label.config(text=f"Download finished!")
            return

"""
def stop_all():
    global t1
    global t2
    global td1
    global td2
    global td3
    global td4
    global td5
    try:
        t1.do_run = False
    except:
        pass
    try:
        t2.do_run = False
    except:
        pass
    try:
        td1.do_run = False
    except:
        pass
    try:
        td2.do_run = False
    except:
        pass
    try:
        td3.do_run = False
    except:
        pass
    try:
        td4.do_run = False
    except:
        pass
    try:
        td5.do_run = False
    except:
        pass
"""        

version_box = tkr.Listbox(fenster, width=63, height=35)
#version_box.bind("<Double-Button-1>", install_old_version)
old_version_button = tkr.Button(fenster, text=f"Search all versions", command=search_versions_thr, bd=3)

scrollbar = tkr.Scrollbar(fenster, orient="vertical")
scrollbar.config(command=version_box.yview)
version_box.config(yscrollcommand=scrollbar.set)
scrollbar.place(in_=version_box, relx=1.0, relheight=1.0, bordermode="outside")

def allow_installation_check_switch():
    if allow_installation_check_var.get() == 1:
        installzeile.config(state=NORMAL)
        install_button.config(state=NORMAL)
    else:
        installzeile.config(state=DISABLED)
        install_button.config(state=DISABLED)

def allow_oldversion_check_switch():
    if allow_oldversion_check_var.get() == 1:
        version_box.config(state=NORMAL)
        old_version_button.config(state=NORMAL)
        allow_newversion_check.config(state=DISABLED)
        allow_custom_hex.config(state=DISABLED)
    else:
        version_box.selection_clear(0, END)
        version_box.config(state=DISABLED)
        old_version_button.config(state=DISABLED)
        allow_newversion_check.config(state=NORMAL)
        allow_custom_hex.config(state=NORMAL)

def allow_custom_hex_switch():
    if allow_custom_hex_var.get() == 1:
        hex_zeile.config(state=NORMAL)
        allow_newversion_check.config(state=DISABLED)
        allow_oldversion_check.config(state=DISABLED)
        old_version_button.config(state=DISABLED)
        version_box.selection_clear(0, END)
        version_box.config(state=DISABLED)
    else:
        hex_zeile.config(state=DISABLED)
        allow_newversion_check.config(state=NORMAL)
        allow_oldversion_check.config(state=NORMAL)
        if allow_oldversion_check_var.get() == 1:
            old_version_button.config(state=NORMAL)
            version_box.config(state=NORMAL)
        else:
            old_version_button.config(state=DISABLED)
            version_box.config(state=DISABLED)
        
hex_text = tkr.Label(fenster, text=f"Enter custom HEX-ID:")
hex_zeile = tkr.Entry(fenster,width=65, state=DISABLED)

installzeile = tkr.Entry(fenster,width=50)
eingabefeld = tkr.Entry(fenster,width=5, state=DISABLED)
allow_installation_check_var = tkr.IntVar()
allow_installation_check = tkr.Checkbutton(fenster, text=f"", command=allow_installation_check_switch, variable=allow_installation_check_var)

allow_newversion_check_var = tkr.IntVar()
allow_newversion_check = tkr.Checkbutton(fenster, text=f"", variable=allow_newversion_check_var)

allow_oldversion_check_var = tkr.IntVar()
allow_oldversion_check = tkr.Checkbutton(fenster, text=f"", variable=allow_oldversion_check_var, command=allow_oldversion_check_switch)

allow_custom_hex_var = tkr.IntVar()
allow_custom_hex = tkr.Checkbutton(fenster, text=f"", variable=allow_custom_hex_var, command=allow_custom_hex_switch)

install_button = tkr.Button(fenster, text=f"Select Directory", command=install_save)

#cancel_button = tkr.Button(fenster, text=f"Stop", command=stop_all)

Thread(target=check_if_running).start()

with open('settings.json') as json_file:
    data = json.load(json_file)
    for p in data['version']:
        ptsorlive = p["name"]
    for p in data['build']:
        xtoxy = p["name"]
    for p in data['assets']:
        assets_f = p["name"]
    for p in data['lang']:
        langf = p["name"]
    for p in data['save_type']:
        savetype = p["name"]
    for p in data['saveto']:
        ps = str(p)
        ps = ps.replace("{'name': '", "")
        ps = ps.replace("'}", "")
        ordnerzeile.insert(0, ps)
    for p in data['allow_newversion_check']:
        if p["name"] == True:
            allow_newversion_check_var.set(1)
        else:
            allow_newversion_check_var.set(0)
    for p in data['allow_installation_check']:
        if p["name"] == True:
            allow_installation_check_var.set(1)
        else:
            allow_installation_check_var.set(0)
    for p in data['installto']:
        ps = str(p)
        ps = ps.replace("{'name': '", "")
        ps = ps.replace("'}", "")
        installzeile.insert(0, ps)

welcome_label = tkr.Label(fenster)
log1_label = tkr.Label(fenster)

allow_installation_check_switch()
allow_oldversion_check_switch()

welcom_button = tkr.Button(fenster, text=f"Download & Install", command=button_action_thr, bd=3)
my_label = tkr.Label(fenster, text=f"SWTOR Patch Downloader & Installer", font=('ARIAL', 10, 'bold'))
#my_label2 = tkr.Label(fenster, text=f"Select the Patch Variant: ")
my_label3 = tkr.Label(fenster, text=f"Type the version number Y: ")
my_label4 = tkr.Label(fenster, text=f"Select the Language:")
my_label5 = tkr.Label(fenster, text=f"Choose the saving location: ")
my_label6 = tkr.Label(fenster, text=f"Select the Download file-structure: ")
my_label7 = tkr.Label(fenster, text=f"Select the Environment: ")
my_label8 = tkr.Label(fenster, text=f"Select the Product: ")
my_label9 = tkr.Label(fenster, text=f"Install files?: ")
my_label10 = tkr.Label(fenster, text=f"Choose the install location: ")
my_label11 = tkr.Label(fenster, text=f"(only needed for assets and movies)")
my_label12 = tkr.Label(fenster, text=f"Search for new version?:")
my_label13 = tkr.Label(fenster, text=f"Download other version?:")

A1 = "swtor"
A2 = "publictest"
#A3 = "liveqatest"
#A4 = "betatest"
#A5 = "cstraining"
#A6 = "liveeptest"
A4 = "launcher"
A5 = "test_001"
A6 = "test_PROD"
A7 = "test_release_tracker"
varA = tkr.StringVar()
varA.set(ptsorlive)
set1 = tkr.OptionMenu(fenster,varA,A1,A2,A4,A5,A6,A7)
set1.configure(font=("Arial",25))


B1 = "XtoY"
B2 = "0toY"
varB = tkr.StringVar()
varB.set(xtoxy)
set2 = tkr.OptionMenu(fenster,varB,B1,B2)
set2.configure(font=("Arial",25),state="disabled")

C1 = "shared"
#C2 = "client"
C2 = "en_us"
C3 = "de_de"
C4 = "fr_fr"
varC = tkr.StringVar()
varC.set(langf)
set3 = tkr.OptionMenu(fenster,varC,C1,C2,C3,C4)
set3.configure(font=("Arial",25))

D1 = "assets"
D2 = "movies"
D3 = "retailclient"
D4 = "launcher"
varD = tkr.StringVar()
varD.set(assets_f)
set4 = tkr.OptionMenu(fenster,varD,D1,D2,D3,D4)
set4.configure(font=("Arial",25))

E1 = "cdn"
E2 = "root"
E3 = "backup"

varE = tkr.StringVar()
varE.set(savetype)
set5= tkr.OptionMenu(fenster,varE,E1,E2,E3)
set5.configure(font=("Arial",25))

save_button = tkr.Button(fenster, text=f"Select Directory", command=file_save)
exit_button = tkr.Button(fenster, text=f"See creation date", command=check_date_thr, bd=3)
hex_id_button = tkr.Button(fenster, text=f"See hex-id", command=check_hex_thr, bd=3)
size_button = tkr.Button(fenster, text=f"See size", command=check_size_thr, bd=3)

progress1 = Progressbar(fenster, orient=HORIZONTAL, length=300, mode='determinate')
progress2 = Progressbar(fenster, orient=HORIZONTAL, length=300, mode='determinate')
progress3 = Progressbar(fenster, orient=HORIZONTAL, length=300, mode='determinate')
progress4 = Progressbar(fenster, orient=HORIZONTAL, length=300, mode='determinate')
progress5 = Progressbar(fenster, orient=HORIZONTAL, length=300, mode='determinate')
download1 = tkr.Label(fenster, text=f"Download 1: ")
download2 = tkr.Label(fenster, text=f"Download 2: ")
download3 = tkr.Label(fenster, text=f"Download 3: ")
download4 = tkr.Label(fenster, text=f"Download 4: ")
download5 = tkr.Label(fenster, text=f"Download 5: ")
dl_file1 = tkr.Label(fenster, wraplength=300 - 20, text=f"")
dl_file2 = tkr.Label(fenster, wraplength=300 - 20, text=f"")
dl_file3 = tkr.Label(fenster, wraplength=300 - 20, text=f"")
dl_file4 = tkr.Label(fenster, wraplength=300 - 20, text=f"")
dl_file5 = tkr.Label(fenster, wraplength=300 - 20, text=f"")
status1 = tkr.Label(fenster, text=f"0%\n0mb/s")
status2 = tkr.Label(fenster, text=f"0%\n0mb/s")
status3 = tkr.Label(fenster, text=f"0%\n0mb/s")
status4 = tkr.Label(fenster, text=f"0%\n0mb/s")
status5 = tkr.Label(fenster, text=f"0%\n0mb/s")

progressc = Progressbar(fenster, orient=HORIZONTAL, length=1160, mode='determinate')
downloadc = tkr.Label(fenster, text=f"Download complete: ")
statusc = tkr.Label(fenster, text=f"0%\n0mb/s")

my_label.place(x=110, y=5) 
#my_label2.place(x=23, y=240) 
#my_label3.place(x=23, y=295)
allow_newversion_check.place(x=155, y=245)
my_label12.place(x=23, y=245)
my_label4.place(x=23, y=175)
my_label11.place(x=23, y=195)
my_label5.place(x=23, y=295)
my_label6.place(x=23, y=370)
my_label7.place(x=23, y=115)
my_label8.place(x=23, y=45)
my_label9.place(x=23, y=415)
allow_installation_check.place(x=90, y=415)
my_label10.place(x=23, y=435)
installzeile.place(x=155, y=465)
install_button.place(x=45, y=463)
#eingabefeld.place(x=275, y=300)
save_button.place(x=45, y=317)
ordnerzeile.place(x=155, y=320)
welcom_button.place(x=40, y=535)
#manbutton.place(x=40, y=630)
#solidbutton.place(x=275, y=630)
exit_button.place(x=275, y=535)
log1_label.place(x=40, y=630)
set4.place(x=250, y=35)
set1.place(x=250, y=100) 
set3.place(x=250, y=165)
#set2.place(x=250, y=230)
set5.place(x=250, y=355)
my_label13.place(x=500, y=35)
allow_oldversion_check.place(x=640, y=35)
version_box.place(x=500, y=60)
old_version_button.place(x=670, y=30)
hex_id_button.place(x=60, y=580)
size_button.place(x=295, y=580)
logbox.place(x=23, y=700)
hex_zeile.place(x=500, y=660)
hex_text.place(x=500, y=630)
allow_custom_hex.place(x=617, y=630)
#cancel_button.place(x=1250, y=650)

download1.place(x=900, y=50)
progress1.place(x=903, y=75)
status1.place(x=1210, y=75)
dl_file1.place(x=900, y=100)

download2.place(x=900, y=180)
progress2.place(x=903, y=205)
status2.place(x=1210, y=205)
dl_file2.place(x=900, y=230)

download3.place(x=900, y=310)
progress3.place(x=903, y=335)
status3.place(x=1210, y=335)
dl_file3.place(x=900, y=360)

download4.place(x=900, y=440)
progress4.place(x=903, y=465)
status4.place(x=1210, y=465)
dl_file4.place(x=900, y=490)

download5.place(x=900, y=570)
progress5.place(x=903, y=595)
status5.place(x=1210, y=595)
dl_file5.place(x=900, y=620)

"""
downloadc.place(x=40, y=700)
progressc.place(x=43, y=725)
statusc.place(x=1210, y=725)
"""

log1_label.config(text=f"Ready!")

tkr.mainloop()
