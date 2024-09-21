from tkinter import filedialog
from tkinter import *
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

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

global zeit
global zeitx
zeitx = ""
global sekunden
sekunden = 0
yes = False

def set_file_last_modified(file_path, dt):
    t = datetime.fromtimestamp(dt)
    dt_epoch = t.timestamp()
    os.utime(file_path, (dt_epoch, dt_epoch))

def bar_progress(current, total, width=80):
    global zeit
    global zeitx
    global sekunden
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

def install_files(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    if installloc == None:
        installloc = installzeile.get()
    print("\nStarting installation\nPress CTRL+C to stop.\n")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", "r")
            elif savetype == "subdirectorys":
                alias = open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}_{lwert}.{vwert}"]
        except:
            print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
            try:
                log1_label.config(text="Version not found!")
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
            os.makedirs(f"{installloc}/Movies/{lwert.replace('_', '-')}/")
        except:
            pass
    if savetype == "cdn":
        metafile = open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "subdirectorys":
        metafile = open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "assets":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Assets/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
        elif assets == "movies":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{assets}_{lwert}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
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
                print(text)
            last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
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
                                    print(text)
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except:
                print(f"ERROR: Can't find {saveloc}/{vwert}/{assets}_{lwert}/pieces/{digest[:2]}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
                except:
                    pass
                return
            
        if savetype == "subdirectorys":
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
                print(text)
            last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{vwert}/{assets}_{lwert}/{digest}.solidpiece", 'rb')
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
                                    print(text)
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"

            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except:
                print(f"ERROR: Can't find {saveloc}/{vwert}/{assets}_{lwert}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
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
                                    print(text)
                                last_text = f"Installing: {installloc}/Assets/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except:
                print(f"ERROR: Can't find {saveloc}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
                except:
                    pass
                return

        print("Installation finished!")
        try:
            log1_label.config(text="Installation finished!")
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
            text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
            last_text = f"Installing: {installloc}/Movies/{metafile_content['files'][current_file]['name']}"
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
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
                            target = f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except Exception as e:
                print(f"ERROR: Can't find {saveloc}/{vwert}/{assets}_{lwert}/pieces/{digest[:2]}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
                except:
                    pass
                return
            
        if savetype == "subdirectorys":
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
            text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
            last_text = f"Installing: {installloc}/Movies/{metafile_content['files'][current_file]['name']}"
            
            try:
                for meta_file in metafile_content['pieces']['digests']:
                    digest = base64.b64decode(meta_file).hex()
                    solidpiece = open(f"{saveloc}/{vwert}/{assets}_{lwert}/{digest}.solidpiece", 'rb')
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
                            target = f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"

            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except:
                print(f"ERROR: Can't find {saveloc}/{vwert}/{assets}_{lwert}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
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
            text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
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
                            target = f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/Movies/{lwert.replace('_', '-')}/{file['name']}", scantime)

                            fd = 0
                            fdOffset = 0
                            current_file += 1
                            if (len(metafile_content['files']) > current_file):
                                file = metafile_content['files'][current_file]
                                text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/Movies/{lwert.replace('_', '-')}/{metafile_content['files'][current_file]['name']}"
            except KeyboardInterrupt:
                print("You stopped the installation!")
                try:
                    log1_label.config(text="You stopped the installation!")
                except:
                    pass
                return
            except:
                print(f"ERROR: Can't find {saveloc}/{digest}.solidpiece")
                try:
                    log1_label.config(text="ERROR: Missing files")
                except:
                    pass
                return

        print("Installation finished!")
        try:
            log1_label.config(text="Installation finished!")
        except:
            pass

def install_client(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    if installloc == None:
        installloc = installzeile.get()
    print("\nStarting installation\nPress CTRL+C to stop.\n")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/{vwert}/{assets}/alias.json", "r")
            elif savetype == "subdirectorys":
                alias = open(f"{saveloc}/{assets}/{vwert}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
        except:
            print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
            try:
                log1_label.config(text="Version not found!")
            except:
                pass
            return

    if assets == "retailclient":
        try:
            os.makedirs(f"{installloc}/{vwert}/{assets}/")
        except:
            pass
    else:
        try:
            os.makedirs(f"{installloc}/")
        except:
            pass
    
    if savetype == "cdn":
        metafile = open(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "subdirectorys":
        metafile = open(f"{saveloc}/{assets}/{vwert}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/{assets}/{vwert}/metafile.json", f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{assets}/{vwert}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "retailclient":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
            last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
        else:
            text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
            last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{vwert}/{assets}/pieces/{digest[:2]}/{digest}.solidpiece", 'rb')
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
                                os.makedirs(f"{installloc}/{vwert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{vwert}/{assets}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            print(f"ERROR: Can't find {saveloc}/{vwert}/{assets}/pieces/{digest[:2]}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
            except:
                pass
            return

    elif savetype == "subdirectorys":
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    print(text)
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{assets}/{vwert}/{digest}.solidpiece", 'rb')
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
                                os.makedirs(f"{installloc}/{vwert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{vwert}/{assets}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except:
            print(f"ERROR: Can't find {saveloc}/{assets}/{vwert}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    print(text)
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
                                os.makedirs(f"{installloc}/{vwert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{vwert}/{assets}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            print(f"ERROR: Can't find {saveloc}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
            except:
                pass
            return

    print("Installation finished!")
    try:
        log1_label.config(text="Installation finished!")
    except:
        pass

def install_launcher(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, installloc=None, catalog_metafile_hex=None):
    if installloc == None:
        installloc = installzeile.get()
    print("\nStarting installation\nPress CTRL+C to stop.\n")
    if catalog_metafile_hex == None:
        try:
            if savetype == "cdn":
                alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
            elif savetype == "subdirectorys":
                alias = open(f"{saveloc}/{assets}/{vwert}/alias.json", "r")
            elif savetype == "root":
                alias = open(f"{saveloc}/alias.json", "r")
            alias_c = alias.read()
            alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
            catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
        except:
            print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
            try:
                log1_label.config(text="Version not found!")
            except:
                pass
            return

    if assets == "retailclient":
        try:
            os.makedirs(f"{installloc}/{vwert}/{assets}/")
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
            shutil.copyfile(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{installloc}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"))
    elif savetype == "subdirectorys":
        metafile = open(f"{saveloc}/{assets}/{vwert}/metafile.json", "r")
        if assets == "launcher":
            shutil.copyfile(f"{saveloc}/{assets}/{vwert}/metafile.json", f"{installloc}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/{assets}/{vwert}/metafile.json"))
    elif savetype == "root":
        metafile = open(f"{saveloc}/metafile.json", "r")
        if assets == "launcher":
            shutil.copyfile(f"{saveloc}/metafile.json", f"{installloc}/{assets}.{vwert}.metafile.json")
            set_file_last_modified(f"{installloc}/{assets}.{vwert}.metafile.json", os.path.getmtime(f"{saveloc}/metafile.json"))
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
            last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
        else:
            text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"

        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            print(f"ERROR: Can't find {saveloc}/swtor/{assets}/pieces/{digest[:2]}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
            except:
                pass
            return

    elif savetype == "subdirectorys":
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    print(text)
                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        try:
            for meta_file in metafile_content['pieces']['digests']:
                digest = base64.b64decode(meta_file).hex()
                solidpiece = open(f"{saveloc}/{assets}/{vwert}/{digest}.solidpiece", 'rb')
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
                                os.makedirs(f"{installloc}/{vwert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{vwert}/{assets}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except:
            print(f"ERROR: Can't find {saveloc}/{assets}/{vwert}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
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
            text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            if not text == last_text:
                print(text)
                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
            else:
                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                if not text == last_text:
                    print(text)
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
                                os.makedirs(f"{installloc}/{vwert}/{assets}/")
                            except:
                                pass
                            target = f"{installloc}/{vwert}/{assets}/{file['name']}"
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
                            set_file_last_modified(f"{installloc}/{vwert}/{assets}/{file['name']}", scantime)
                        else:
                            set_file_last_modified(f"{installloc}/{file['name']}", scantime)

                        fd = 0
                        fdOffset = 0
                        current_file += 1
                        if (len(metafile_content['files']) > current_file):
                            file = metafile_content['files'][current_file]
                            if assets == "retailclient":
                                text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{vwert}/{assets}/{metafile_content['files'][current_file]['name']}"
                            else:
                                text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
                                if not text == last_text:
                                    print(text)
                                last_text = f"Installing: {installloc}/{metafile_content['files'][current_file]['name']}"
        except KeyboardInterrupt:
            print("You stopped the installation!")
            try:
                log1_label.config(text="You stopped the installation!")
            except:
                pass
            return
        except Exception as e:
            print(f"ERROR: Can't find {saveloc}/{digest}.solidpiece")
            try:
                log1_label.config(text="ERROR: Missing files")
            except:
                pass
            return

    print("Installation finished!")
    try:
        log1_label.config(text="Installation finished!")
    except:
        pass

def download_client(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global zeitx
    global sekunden
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if True:
        if catalog_metafile_hex is None:
            if savetype == "cdn":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{vwert}/{assets}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{vwert}/{assets}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{vwert}/{assets}/alias.json", f"{saveloc}/{vwert}/{assets}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            elif savetype == "subdirectorys":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                try:
                    os.makedirs(f"{saveloc}/{assets}/{vwert}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{assets}/{vwert}/alias.json", f"{saveloc}/{assets}/{vwert}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{assets}/{vwert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{assets}/{vwert}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return
                        
            elif savetype == "root":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                try:
                    os.makedirs(saveloc)
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
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
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/{vwert}/{assets}/alias.json", "r")
                elif savetype == "subdirectorys":
                    alias = open(f"{saveloc}/{assets}/{vwert}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
            except:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
                except:
                    pass
                return
            
        if savetype == "cdn":
            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
            
        elif savetype == "subdirectorys":
            try:
                os.makedirs(f"{saveloc}/{assets}/{vwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            print(md5_old)
            print(md5_new)
            if not md5_old == md5_new:
                print("!!!!!")
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{assets}/{vwert}/catalog.json", f"{saveloc}/{assets}/{vwert}/catalog_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{assets}/{vwert}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{assets}/{vwert}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{assets}/{vwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{assets}/{vwert}/metafile.json", f"{saveloc}/{assets}/{vwert}/metafile_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{assets}/{vwert}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{assets}/{vwert}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

        elif savetype == "root":
            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
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
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
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
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

        if savetype == "cdn":
            metafile = open(f"{saveloc}/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "subdirectorys":
            metafile = open(f"{saveloc}/{assets}/{vwert}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        print(f"Download of {assets} {vwert} {selected} solidpieces started!\nPress CTRL+C to stop.")
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
            if savetype == "cdn":
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{vwert}/{assets}/pieces/{meta_file[:2]}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}/pieces/{meta_file[:2]}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                            
            elif savetype == "subdirectorys":
                if not os.path.exists(f"{saveloc}/{assets}/{vwert}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{assets}/{vwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{assets}/{vwert}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                            
            elif savetype == "root":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True

def download_launcher(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global zeitx
    global sekunden
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if True:
        if catalog_metafile_hex is None:
            if savetype == "cdn":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
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
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/swtor/{assets}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            elif savetype == "subdirectorys":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                try:
                    os.makedirs(f"{saveloc}/{assets}/{vwert}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                         for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{assets}/{vwert}/alias.json", f"{saveloc}/{assets}/{vwert}/alias_old_{i}.json")
                                break
                if not os.path.exists(f"{saveloc}/{assets}/{vwert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{assets}/{vwert}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return
                        
            elif savetype == "root":
                print(f"Download of {assets} {vwert} {selected} alias.json started!\nPress CTRL+C to stop.")
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
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/swtor/{assets}/alias.json", "r")
                elif savetype == "subdirectorys":
                    alias = open(f"{saveloc}/{assets}/{vwert}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
            except:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
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
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
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
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
            
        elif savetype == "subdirectorys":
            try:
                os.makedirs(f"{saveloc}/{assets}/{vwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{assets}/{vwert}/catalog.json", f"{saveloc}/{assets}/{vwert}/catalog_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{assets}/{vwert}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{assets}/{vwert}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{assets}/{vwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{assets}/{vwert}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{assets}/{vwert}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{assets}/{vwert}/metafile.json", f"{saveloc}/{assets}/{vwert}/metafile_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{assets}/{vwert}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{assets}/{vwert}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
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
            print(f"Download of {assets} {vwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
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
            print(f"Download of {assets} {vwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

        if savetype == "cdn":
            metafile = open(f"{saveloc}/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "subdirectorys":
            metafile = open(f"{saveloc}/{assets}/{vwert}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        print(f"Download of {assets} {vwert} {selected} solidpieces started!\nPress CTRL+C to stop.")
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
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
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                                    
            elif savetype == "subdirectorys":
                if not os.path.exists(f"{saveloc}/{assets}/{vwert}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{assets}/{vwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{assets}/{vwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{assets}/{vwert}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
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
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/swtor/{assets}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                

def download_files(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, catalog_metafile_hex):
    global zeitx
    global sekunden
    try:
        selected = version_box.get(version_box.curselection()[0])
    except:
        selected = ""
    if catalog_metafile_hex is None:
        if not lwert == "client":
            if savetype == "cdn":
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
                try:
                    os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
                except:
                    pass
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", f"{saveloc}/{vwert}/{assets}_{lwert}/alias_old_{i}.json")
                                break
                print(f"Download of {assets} {vwert} {lwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return
                        
            elif savetype == "subdirectorys":
                try:
                    os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
                if allow_newversion_check_f == 1 or allow_newversion_check_f == "true":
                    md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
                    try:
                        md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json").read().encode('utf-8')).hexdigest()
                    except:
                        md5_old = md5_new
                    if not md5_old == md5_new:
                        for i in range(1, 99999):
                            if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/alias_old_{i}.json"):
                                os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", f"{saveloc}/{vwert}/{assets}_{lwert}/alias_old_{i}.json")
                                break
                print(f"Download of {assets} {vwert} {lwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            elif savetype == "root":
                try:
                    os.makedirs(saveloc)
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
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
                print(f"Download of {assets} {vwert} {lwert} {selected} alias.json started!\nPress CTRL+C to stop.")
                if not os.path.exists(f"{saveloc}/alias.json") == True:
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/alias.json", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Version not found!")
                                except:
                                    pass
                                print("\nVersion not found!\n")
                                return

            try:
                if savetype == "cdn":
                    alias = open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", "r")
                elif savetype == "subdirectorys":
                    alias = open(f"{saveloc}/{vwert}/{assets}_{lwert}/alias.json", "r")
                elif savetype == "root":
                    alias = open(f"{saveloc}/alias.json", "r")
                alias_c = alias.read()
                alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                catalog_metafile_hex = alias_content[f"{assets}_{lwert}.{vwert}"]
            except Exception as e:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
                except:
                    pass
                return

    if True:
        if savetype == "cdn":
            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json", f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {lwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {lwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

        elif savetype == "subdirectorys":
            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog.json", f"{saveloc}/{vwert}/{assets}_{lwert}/catalog_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {lwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"
            md5_new = hashlib.md5(requests.get(url).content.decode("utf-8").encode('utf-8')).hexdigest()
            try:
                md5_old = hashlib.md5(open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json").read().encode('utf-8')).hexdigest()
            except:
                md5_old = md5_new
            if not md5_old == md5_new:
                for i in range(1, 99999):
                    if not os.path.isfile(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile_old_{i}.json"):
                        os.rename(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", f"{saveloc}/{vwert}/{assets}_{lwert}/metafile_old_{i}.json")
                        break
            print(f"Download of {assets} {vwert} {lwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

        elif savetype == "root":
            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json"
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
            print(f"Download of {assets} {vwert} {lwert} {selected} catalog.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/catalog.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/catalog.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/catalog/{catalog_metafile_hex}/catalog.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return

            try:
                os.makedirs(saveloc)
            except:
                pass
            url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"
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
            print(f"Download of {assets} {vwert} {lwert} {selected} metafile.json started!\nPress CTRL+C to stop.")
            if not os.path.exists(f"{saveloc}/metafile.json") == True:
                lost = False
                while True:
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, saveloc, bar=bar_progress)
                        creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                        set_file_last_modified(f"{saveloc}/metafile.json", creation_time)
                        print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json\n")
                        break
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            if not lost:
                                print("\nConnection lost.\nTrying again...\n")
                                lost = True
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                    

        if savetype == "cdn":
            metafile = open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
        elif savetype == "subdirectorys":
            metafile = open(f"{saveloc}/{vwert}/{assets}_{lwert}/metafile.json", "r")
        elif savetype == "root":
            metafile = open(f"{saveloc}/metafile.json", "r")
        metafile_c = metafile.read()
        metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
        metafiles = metafile_content["pieces"]["digests"]
        print(f"Download of {assets} {vwert} {lwert} {selected} solidpieces started!\nPress CTRL+C to stop.")
        for meta_file in metafiles:
            meta_file = base64.b64decode(meta_file).hex()
            if savetype == "cdn":
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                            
            elif savetype == "subdirectorys":
                if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True
                            
            if savetype == "root":
                if not os.path.exists(f"{saveloc}/{meta_file}.solidpiece") == True:
                    try:
                        os.makedirs(saveloc)
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece"
                    lost = False
                    while True:
                        try:
                            zeitx = int(time.time())
                            sekunden = 0
                            wget.download(url, saveloc, bar=bar_progress)
                            creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                            set_file_last_modified(f"{saveloc}/{meta_file}.solidpiece", creation_time)
                            print(f"\nDownloaded: http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/pieces/{meta_file[:2]}/{meta_file}.solidpiece\n")
                            break
                        except KeyboardInterrupt:
                            print("\nYou stopped the download!")
                            return
                        except Exception as ex:
                            exception = type(ex).__name__
                            argumente = str(ex.args)
                            if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                                if not lost:
                                    print("\nConnection lost.\nTrying again...\n")
                                    lost = True
                                try:
                                    log1_label.config(text="Connection lost!")
                                except:
                                    pass
                                return
                            else:
                                try:
                                    log1_label.config(text="Solidpiece not found!")
                                except:
                                    pass
                                if not lost:
                                    print("\nSolidpiece not found.\nTrying again...\n")
                                    lost = True

dir_path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(dir_path)
for item in dirs:
    if item.endswith(".tmp"):
        os.remove(os.path.join(dir_path, item))
try:
    shutil.rmtree('temp', ignore_errors=True)
except:
    pass

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
            vwert = "swtor"
        if i.lower() == "env=publictest":
            vwert = "publictest"
        if i.lower() == "env=launcher":
            vwert = "launcher"
        if i.lower() == "env=test_001":
            vwert = "test_001"
        if i.lower() == "env=test_prod":
            vwert = "test_PROD"

        if i.lower() == "lang=shared":
            lwert = "shared"
        if i.lower() == "lang=de_de":
            lwert = "de_de"
        if i.lower() == "lang=en_us":
            lwert = "en_us"
        if i.lower() == "lang=fr_fr":
            lwert = "fr_fr"

        if i.lower() == "structure=cdn":
            savetype = "cdn"
        if i.lower() == "structure=subdirectorys":
            savetype = "subdirectorys"
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
                            download_client(saveloc, lwert, 0, vwert, "0", assets, savetype, allow_newversion_check_f, None)
                            if allow_installation:
                                install_client(saveloc, lwert, 0, vwert, 0, assets, savetype, installloc, None)
                            else:
                                print("Download finished!")
                                try:
                                    log1_label.config(text="Download finished!")
                                except:
                                    pass
                            sys.exit()
                        elif assets == "launcher":
                            download_launcher(saveloc, lwert, 0, vwert, "0", assets, savetype, allow_newversion_check_f, None)
                            if allow_installation:
                                install_launcher(saveloc, lwert, 0, vwert, 0, assets, savetype, installloc, None)
                            else:
                                print("Download finished!")
                                try:
                                    log1_label.config(text="Download finished!")
                                except:
                                    pass
                            sys.exit()
                        if True:
                            if True:
                                download_files(saveloc, lwert, 0, vwert, "0", assets, savetype, allow_newversion_check_f, None)
                                if allow_installation:
                                    install_files(saveloc, lwert, 0, vwert, 0, assets, savetype, installloc, None)
                                else:
                                    print("Download finished!")
                                    try:
                                        log1_label.config(text="Download finished!")
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
                "structure - cdn/subdirectorys/root\n"
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

print("SWTOR Patch Downloader & Installer\n")

def check_date():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
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
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': vwert})
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
            'name': lwert})
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

        try:
            selected = version_box.get(version_box.curselection()[0])
            index = descriptions.index(selected)
            catalog_metafile_hex = ids[index]
            oldversion = True
        except:
            oldversion = False
        if not assets == "launcher" and not assets == "retailclient":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nTrying again...\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}_{lwert}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
				
				
            if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                try:
                    os.makedirs(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nTrying again...\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        print("\nVersion not found!\n")
                        return
						
            metafile = open(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
            metafile_c = metafile.read()
            metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
            scantime = metafile_content["scanTime"]
            dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
            print(f"\nVersion created on: {dt}")
            try:
                log1_label.config(text=f"Version created on: {dt}")
            except:
                pass

        elif assets == "retailclient":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nTrying again...\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
				
				
            if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                try:
                    os.makedirs(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nTrying again...\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        print("\nVersion not found!\n")
                        return
						
            metafile = open(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
            metafile_c = metafile.read()
            metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
            scantime = metafile_content["scanTime"]
            dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
            print(f"\nVersion created on: {dt}")
            try:
                log1_label.config(text=f"Version created on: {dt}")
            except:
                pass

        elif assets == "launcher":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/swtor/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/swtor/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/swtor/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nTrying again...\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/swtor/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
				
				
            if not os.path.exists(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                try:
                    os.makedirs(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/")
                except:
                    pass
                url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nTrying again...\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        print("\nVersion not found!\n")
                        return
						
            metafile = open(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
            metafile_c = metafile.read()
            metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
            scantime = metafile_content["scanTime"]
            dt = datetime.fromtimestamp(scantime).strftime("%d.%m.%Y")
            print(f"\nVersion created on: {dt}")
            try:
                log1_label.config(text=f"Version created on: {dt}")
            except:
                pass
        

def file_save():
    global zeitx
    global sekunden
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        ordnerzeile.delete(0, END)
        ordnerzeile.insert(0, folder_selected)

def install_save():
    global zeitx
    global sekunden
    folder_selected = filedialog.askdirectory()
    folder_selected = str(folder_selected)
    folder_selected = folder_selected.replace("\\", "/")
    if not folder_selected == "":
        installzeile.delete(0, END)
        installzeile.insert(0, folder_selected)

def button_action():
    try:
        selected = version_box.get(version_box.curselection()[0])
        install_old_version()
        return
    except:
        pass
    
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    saveloc = saveloc.rstrip()
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    allow_newversion_check_f = allow_newversion_check_var.get()
    if not os.path.isdir(saveloc):
        try:
            os.makedirs(saveloc)
        except:
            pass
    yes = False
    #if vnummer == "":
    #    log1_label.config(text="Please enter the version number,\nyou want to download!")
    #    return
    if saveloc == "":
        log1_label.config(text="Please enter the location,\nwhere you want to save the files!")
        return
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': vwert})
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
            'name': lwert})
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
        download_client(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, None)
        if allow_installation_check_var.get() == 1:
            install_client(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, None, None)
        else:
            print("Download finished!")
            log1_label.config(text="Download finished!")
        return
    elif assets == "launcher":
        download_launcher(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, None)
        if allow_installation_check_var.get() == 1:
            install_launcher(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, None, None)
        else:
            print("Download finished!")
            log1_label.config(text="Download finished!")
        return
    #if vwert == "swtor" or vwert == "publictest":
    if True:
        #if uwert == "XtoY":
        if True:
            download_files(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, allow_newversion_check_f, None)
            if allow_installation_check_var.get() == 1:
                install_files(saveloc, lwert, vnummerx, vwert, vnummer, assets, savetype, None, None)
            else:
                print("Download finished!")
                log1_label.config(text="Download finished!")
            return
        #if uwert == "0toY":
        #    download_files0(saveloc, lwert, vnummerx, vwert, vnummer)
        #    return
    """
    if vwert == "liveqatest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "betatest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "cstraining":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    if vwert == "liveeptest":
        if uwert == "0toY":
            download_exp_client0(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
        if uwert == "XtoY":
            download_exp_client(saveloc, lwert, vnummerx, vwert, vnummer, vwert)
            return
    """

def search_versions():
    global zeitx
    global sekunden
    global descriptions
    global ids

    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
    assets = varD.get()
    savetype = varE.get()
    vnummer = eingabefeld.get()
    saveloc = ordnerzeile.get()
    saveloc2 = ordnerzeile.get()
    try:
        installloc = installzeile.get()
    except:
        installloc = ""
    installloc = installloc.rstrip()
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': vwert})
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
            'name': lwert})
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
            os.makedirs(f"{saveloc}/{vwert}/{assets}_{lwert}/")
        except:
            pass
        url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json"
        try:
            creation_time_new = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
        except Exception as e:
            try:
                log1_label.config(text="Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            print("\nVersion not found!\n")
            return
        try:
            creation_time_old = os.path.getmtime(f"{saveloc}/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json")
        except:
            creation_time_old = creation_time_new
        if creation_time_old < creation_time_new:
            os.remove(f"{saveloc}/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json")
        if True:
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json") == True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json", creation_time)
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    print(ex)
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nPlease try again!\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        version_box.delete(0, tkr.END)
                        print("\nVersion not found!\n")
                        return
		
            try:
                history = open(f"{saveloc}/{vwert}/{assets}_{lwert}/{assets}_{lwert}.history.json", "r")
                history_c = history.read()
                history_content = jwt.decode(history_c, algorithms=["RS256"], options={"verify_signature": False})
                history_content = history_content['history']

                descriptions = []
                ids = []
                version_box.delete(0, tkr.END)
                for part in history_content:
                    descriptions.append(part["description"])
                    ids.append(part["id"])
                    version_box.insert(tkr.END, part["description"])
                log1_label.config(text="Found previous versions!")
                return
            except Exception as e:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
                except:
                    pass
                version_box.delete(0, tkr.END)
                return


    elif assets == "retailclient":
        try:
            os.makedirs(f"{saveloc}/{vwert}/{assets}/")
        except:
            pass
        url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/{assets}.history.json"
        try:
            creation_time_new = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
        except:
            try:
                log1_label.config(text="Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            print("\nVersion not found!\n")
            return
        try:
            creation_time_old = os.path.getmtime(f"{saveloc}/{vwert}/{assets}/{assets}.history.json")
        except:
            creation_time_old = creation_time_new
        if creation_time_old < creation_time_new:
            os.remove(f"{saveloc}/{vwert}/{assets}/{assets}.history.json")
        if True:
            if not os.path.exists(f"{saveloc}/{vwert}/{assets}/{assets}.history.json") == True:
                try:
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/{vwert}/{assets}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/{vwert}/{assets}/{assets}.history.json", creation_time)
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nPlease try again!\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        version_box.delete(0, tkr.END)
                        print("\nVersion not found!\n")
                        return
				
            try:
                history = open(f"{saveloc}/{vwert}/{assets}/{assets}.history.json", "r")
                history_c = history.read()
                history_content = jwt.decode(history_c, algorithms=["RS256"], options={"verify_signature": False})
                history_content = history_content['history']

                descriptions = []
                ids = []
                version_box.delete(0, tkr.END)
                for part in history_content:
                    descriptions.append(part["description"])
                    ids.append(part["id"])
                    version_box.insert(tkr.END, part["description"])
                log1_label.config(text="Found previous versions!")
                return
            except Exception as e:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
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
                log1_label.config(text="Version not found!")
            except:
                pass
            #version_box.delete(0, tkr.END)
            print("\nVersion not found!\n")
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
                    zeitx = int(time.time())
                    sekunden = 0
                    wget.download(url, f"{saveloc}/swtor/{assets}/", bar=bar_progress)
                    print(f"\nDownloaded: {url}\n")
                    creation_time = datetime.strptime(requests.get(url).headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                    set_file_last_modified(f"{saveloc}/swtor/{assets}/{assets}.history.json", creation_time)
                except KeyboardInterrupt:
                    print("\nYou stopped the download!")
                    return
                except Exception as ex:
                    exception = type(ex).__name__
                    argumente = str(ex.args)
                    if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                        print("\nConnection lost.\nPlease try again!\n")
                        try:
                            log1_label.config(text="Connection lost!")
                        except:
                            pass
                        return
                    else:
                        try:
                            log1_label.config(text="Version not found!")
                        except:
                            pass
                        print("\nVersion not found!\n")
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
                    descriptions.append(part["description"])
                    ids.append(part["id"])
                    version_box.insert(tkr.END, part["description"])
                log1_label.config(text="Found previous versions!")
                return
            except Exception as e:
                print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                try:
                    log1_label.config(text="Version not found!")
                except:
                    pass
                version_box.delete(0, tkr.END)
                return

def check_hex():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
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
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': vwert})
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
            'name': lwert})
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

        try:
            selected = version_box.get(version_box.curselection()[0])
            index = descriptions.index(selected)
            catalog_metafile_hex = ids[index]
            oldversion = True
        except:
            oldversion = False
        if not oldversion:
            if assets == "assets" or assets == "movies":
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}_{lwert}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return

            elif assets == "retailclient":
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return

            elif assets == "launcher":
                if not os.path.exists(f"{saveloc}/temp/swtor/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/swtor/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/swtor/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/swtor/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
                
        log1_label.config(text=f"Hex-id: {catalog_metafile_hex}")
        print(f"\nHex-id: {catalog_metafile_hex}")

def check_size():
    global zeitx
    global sekunden
    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
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
    if True:
        data = {}
        data['version'] = []
        data['version'].append({
        'name': vwert})
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
            'name': lwert})
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

        try:
            selected = version_box.get(version_box.curselection()[0])
            index = descriptions.index(selected)
            catalog_metafile_hex = ids[index]
            oldversion = True
        except:
            oldversion = False
        download_size = 0
        if assets == "assets" or assets == "movies":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}_{lwert}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}_{lwert}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
            if True:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                                    
                metafile = open(f"{saveloc}/temp/{vwert}/{assets}_{lwert}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                for file in metafile_content["files"]:
                    download_size += file["size"]
                download_size = locale.format_string("%d", download_size, grouping=True)
                print(f"\nSize: {download_size} Bytes")
                try:
                    log1_label.config(text=f"Size: {download_size} Bytes")
                except:
                    pass

        elif assets == "retailclient":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/{vwert}/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
				
            if True:
                if not os.path.exists(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                                    
                metafile = open(f"{saveloc}/temp/{vwert}/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                for file in metafile_content["files"]:
                    download_size += file["size"]
                download_size = locale.format_string("%d", download_size, grouping=True)
                print(f"\nSize: {download_size} Bytes")
                try:
                    log1_label.config(text=f"Size: {download_size} Bytes")
                except:
                    pass

        
        elif assets == "launcher":
            if not oldversion:
                if not os.path.exists(f"{saveloc}/temp/swtor/{assets}/alias.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/swtor/{assets}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/alias.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/swtor/{assets}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        print(ex)
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                    
                try:
                    alias = open(f"{saveloc}/temp/swtor/{assets}/alias.json", "r")
                    alias_c = alias.read()
                    alias_content = jwt.decode(alias_c, algorithms=["RS256"], options={"verify_signature": False})
                    catalog_metafile_hex = alias_content[f"{assets}.{vwert}"]
                except:
                    print("\nCan't find your version in alias.json. Please ensure you selected an empty folder for download. Please also check whether the desired product exists.")
                    try:
                        log1_label.config(text="Version not found!")
                    except:
                        pass
                    return
            if True:
                if not os.path.exists(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json") == True:
                    try:
                        os.makedirs(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/")
                    except:
                        pass
                    url = f"http://cdn-d6patch.swtor.com/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json"
                    try:
                        zeitx = int(time.time())
                        sekunden = 0
                        wget.download(url, f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/", bar=bar_progress)
                        print(f"\nDownloaded: {url}\n")
                    except KeyboardInterrupt:
                        print("\nYou stopped the download!")
                        return
                    except Exception as ex:
                        exception = type(ex).__name__
                        argumente = str(ex.args)
                        if "getaddrinfo failed" in argumente or "Verbindung" in argumente or "connection" in argumente or "Netzwerk" in argumente or "network" in argumente:
                            print("\nConnection lost.\nPlease try again!\n")
                            try:
                                log1_label.config(text="Connection lost!")
                            except:
                                pass
                            return
                        else:
                            try:
                                log1_label.config(text="Version not found!")
                            except:
                                pass
                            print("\nVersion not found!\n")
                            return
                                                    
                metafile = open(f"{saveloc}/temp/swtor/{assets}/metafile/{catalog_metafile_hex}/metafile.json", "r")
                metafile_c = metafile.read()
                metafile_content = jwt.decode(metafile_c, algorithms=["RS256"], options={"verify_signature": False})
                for file in metafile_content["files"]:
                    download_size += file["size"]
                download_size = locale.format_string("%d", download_size, grouping=True)
                print(f"\nSize: {download_size} Bytes")
                try:
                    log1_label.config(text=f"Size: {download_size} Bytes")
                except:
                    pass
            
            

fenster = tkr.Tk()
fenster.title("SWTOR Patch Downloader & Installer")
fenster.geometry("900x670")
#fenster.geometry("490x720")
fenster.resizable(False, False)
ordnerzeile = tkr.Entry(fenster,width=50)

def install_old_version():
    global zeitx
    global sekunden

    selected = version_box.get(version_box.curselection()[0])
    index = descriptions.index(selected)
    catalog_metafile_hex = ids[index]

    vwert = varA.get()
    uwert = varB.get()
    lwert = varC.get()
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
        download_client(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, 0, catalog_metafile_hex)
        if allow_installation_check_var.get() == 1:
            install_client(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, None, catalog_metafile_hex)
        else:
            print("Download finished!")
            log1_label.config(text="Download finished!")
        return
    elif assets == "launcher":
        download_launcher(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, 0, catalog_metafile_hex)
        if allow_installation_check_var.get() == 1:
            install_launcher(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, None, catalog_metafile_hex)
        else:
            print("Download finished!")
            log1_label.config(text="Download finished!")
        return
    #if vwert == "swtor" or vwert == "publictest":
    if True:
        #if uwert == "XtoY":
        if True:
            download_files(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, 0, catalog_metafile_hex)
            if allow_installation_check_var.get() == 1:
                install_files(saveloc2, lwert, vnummerx, vwert, vnummer, assets, savetype, None, catalog_metafile_hex)
            else:
                print("Download finished!")
                log1_label.config(text="Download finished!")
            return
        

version_box = tkr.Listbox(fenster, width=63, height=38)
#version_box.bind("<Double-Button-1>", install_old_version)
old_version_button = tkr.Button(fenster, text=f"Search all versions", command=search_versions, bd=3)

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
    else:
        version_box.selection_clear(0, END)
        version_box.config(state=DISABLED)
        old_version_button.config(state=DISABLED)
        allow_newversion_check.config(state=NORMAL)
        #version_box.delete(0, tkr.END)
        

installzeile = tkr.Entry(fenster,width=50)
eingabefeld = tkr.Entry(fenster,width=5, state=DISABLED)
allow_installation_check_var = tkr.IntVar()
allow_installation_check = tkr.Checkbutton(fenster, text="", command=allow_installation_check_switch, variable=allow_installation_check_var)

allow_newversion_check_var = tkr.IntVar()
allow_newversion_check = tkr.Checkbutton(fenster, text="", variable=allow_newversion_check_var)

allow_oldversion_check_var = tkr.IntVar()
allow_oldversion_check = tkr.Checkbutton(fenster, text="", variable=allow_oldversion_check_var, command=allow_oldversion_check_switch)

install_button = tkr.Button(fenster, text="Select Directory", command=install_save)

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

welcom_button = tkr.Button(fenster, text="Download & Install", command=button_action, bd=3)
my_label = tkr.Label(fenster, text="SWTOR Patch Downloader & Installer", font=('ARIAL', 10, 'bold'))
#my_label2 = tkr.Label(fenster, text="Select the Patch Variant: ")
my_label3 = tkr.Label(fenster, text="Type the version number Y: ")
my_label4 = tkr.Label(fenster, text="Select the Language:")
my_label5 = tkr.Label(fenster, text="Choose the saving location: ")
my_label6 = tkr.Label(fenster, text="Select the Download file-structure: ")
my_label7 = tkr.Label(fenster, text="Select the Environment: ")
my_label8 = tkr.Label(fenster, text="Select the Product: ")
my_label9 = tkr.Label(fenster, text="Install files?: ")
my_label10 = tkr.Label(fenster, text="Choose the install location: ")
my_label11 = tkr.Label(fenster, text="(only needed for assets and movies)")
my_label12 = tkr.Label(fenster, text="Search for new version?:")
my_label13 = tkr.Label(fenster, text="Download other version?:")

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
E2 = "subdirectorys"
E3 = "root"
varE = tkr.StringVar()
varE.set(savetype)
set5= tkr.OptionMenu(fenster,varE,E1,E2,E3)
set5.configure(font=("Arial",25))

save_button = tkr.Button(fenster, text="Select Directory", command=file_save)
exit_button = tkr.Button(fenster, text="See creation date", command=check_date, bd=3)
hex_id_button = tkr.Button(fenster, text="See hex-id", command=check_hex, bd=3)
size_button = tkr.Button(fenster, text="See size", command=check_size, bd=3)

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
log1_label.place(x=40, y=620)
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

log1_label.config(text="Ready!")

tkr.mainloop()
