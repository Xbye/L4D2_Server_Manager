import threading
import datetime
import time
import pathlib

TIMER_INVALIDATE = 21600    # 6 hours
FORCE_APP_STATUS_ON_UPDATE = False
WORKSHOP_SCRIPT = True
DEBUG_MODE = 1

# Globals
thread_l4d2_autoupdate = True
thread_l4d2_userinput = True

def autoupdateSRCDS():

    start_time = time.time()

    # run this while there is no input
    while thread_l4d2_autoupdate:
        time.sleep(1)

        if time.time() - start_time >= 2:
            start_time = time.time()
            print('Another 2 seconds has passed')

def printDebugMSG(msg, level):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [D{level}] {msg}")

def pathUserInput(filepath : pathlib.Path, file):
    print((f"{file} was not found in:\n"
           f"\t'{filepath.joinpath('...')}'\n"))
    
    filepath = pathlib.Path(input((
           f"Input the location of {file} (Type 'q' to exit):\n"
            "> ")))
    
    return filepath

def main():
    global thread_l4d2_userinput
    global thread_l4d2_autoupdate

    keywords_stop = ("q", "quit")

    path_steamcmd = pathlib.Path.cwd()
    path_l4d2dir = pathlib.Path.cwd().joinpath("")
    path_workshop = pathlib.Path.cwd()

    try:

        while not path_steamcmd.joinpath("steamcmd.sh").exists() and str(path_steamcmd).lower() not in keywords_stop:
            path_steamcmd = pathUserInput(path_steamcmd,"SteamCMD")

        if str(path_steamcmd).lower() in keywords_stop:
            raise KeyboardInterrupt

        if DEBUG_MODE > 0:
            printDebugMSG(path_steamcmd,1)
        
        while not path_l4d2dir.joinpath("srcds_run").exists() and str(path_l4d2dir).lower() not in keywords_stop:
            path_l4d2dir = pathUserInput(path_l4d2dir,"L4D2 SRCDS")

        if str(path_l4d2dir).lower() in keywords_stop:
            raise KeyboardInterrupt

        if DEBUG_MODE > 0:
            printDebugMSG(path_l4d2dir,1)

        if WORKSHOP_SCRIPT:
            while not path_workshop.exists() and str(path_workshop).lower() not in keywords_stop:
                path_workshop = pathUserInput(path_workshop,"Workshop script")
        
        if str(path_workshop).lower() in keywords_stop:
            raise KeyboardInterrupt
        
    except KeyboardInterrupt:
        printDebugMSG("User ended session.", 0)
    
    finally:
        thread_l4d2_userinput = False
        thread_l4d2_autoupdate = False

if __name__ == '__main__':
    main()