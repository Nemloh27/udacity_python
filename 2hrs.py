import webbrowser
import time

total_breaks = 3
break_count = 0

print ("Time to teak a break!!!" + time.ctime())
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("http://www.espn.com")
    break_count = break_count + 1
