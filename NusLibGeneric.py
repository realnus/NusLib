from threading import Thread
from threading import Lock
from datetime import datetime

## Append To Text File Section
## Todo: Create file if it does not exists
locker_AppendToTextFile_v1 = Lock()
def AppendToTextFile_ThreadSafe_v1(FilePath,data):
    with locker_AppendToTextFile_v1:   
        file1 = open(FilePath, "a")  # append mode
        file1.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  + " | " + data)
        file1.close()


def PercentChange(current, previous):
    if current == previous:
        return 0
    try:
        return (current - previous) / previous * 100.0
    except ZeroDivisionError:
        return 0


def CalculateTimeDifference(StartDateTime, EndDateTime):
    diff = EndDateTime - StartDateTime

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    milli_secs = diff.total_seconds() * 1000

    return "days:" +  str(days) + " hours:" + str(hours) + " minutes:" + str(minutes) + " seconds:",str(seconds) + " milli_secs:" + str(milli_secs)


def GetTotalCpuUsage():
    import psutil 
    cpu = psutil.cpu_percent(interval=5)
    return cpu   