#!/bin/python3

def get_output(user_input):
    global size
    size = ""
    variable=[]
    count=0
    portrait=0
    for i in user_input:
        try:
            temp=eval(i)["p"]
            temp1=eval(i)["l"]
        except:
            print(f"dict {i} not found!")
            exit()
        if (int(temp) > portrait):
	        portrait=int(temp)
        variable.append(f"dict{count}")
        exec(f"dict{count}=1")
        count+=1
    del temp1
    text = "| "
    for i in range (1,portrait+1,1):
        temp=0
        for char in user_input:
            exec(f"global size; size=int({variable[temp]})")
            size_landscape=int(size+eval(char)["l"])
            for i in range(size,size_landscape,1):
                if (i in eval(char)):
                    text += eval(char)[i]
                else:
                    text += " "
            exec(f"{variable[temp]}={size_landscape}")
            temp+=1
            text += " "
        text += " |\n| "
    return text

def get_time():
    global date, time_now, time
    while 1:
        tmp = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        time_now = tmp.split(" ")[1]
        date = tmp.split(" ")[0]
        sleep(0.25)


def print_time():
    global date, time_now, time, timezone
    landspace_line = " " + "=" * 46 + " "
    while 1:
        time = ""
        for char in time_now:
            try:
                char = int(char)
            except ValueError:
                pass
            time = time + "{0} ".format(ahihi[char])
        datetimezone_str = "> Date: " + date + " [{0}]".format(timezone)
        datetimezone_str = datetimezone_str + str(" " * int(45 - len(datetimezone_str)))
        output = landspace_line + "\n" + get_output([x for x in time.split(" ") if x]) + datetimezone_str + "|\n" + landspace_line + "\n"
        stdout.clear()
        stdout.write(output)
        sleep(0.25)

if (__name__=="__main__"):
    from dict import ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, HOLYSHIT
    import datetime
    from time import sleep
    from khanhnguyen9872 import stdout
    from threading import Thread
    ahihi = {0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', ':': 'HOLYSHIT'}

    if __import__('os').name == 'nt':
        try:
            __import__('colorama')
        except (ImportError, ModuleNotFoundError):
            __import__('os').system("{0} -m pip install colorama".format(__import__('sys').executable))
        __import__('colorama').just_fix_windows_console()

    timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
    print("")
    stdout = stdout()
    stdout.hide_cursor()
    Thread(target=get_time).start()
    Thread(target=print_time).start()