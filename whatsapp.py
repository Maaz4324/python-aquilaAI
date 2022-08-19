import pywhatkit
import datetime

def send_msg(results):
      rishi = '+91 8961502488'
      mom = '+91 8582941433'
      me = '+91 9831169844'
      hour = datetime.datetime.now().hour
      timeMin = datetime.datetime.now().minute+1
      # print(t+":"+tm)
      try:
            pywhatkit.sendwhatmsg(mom, results, hour, timeMin)
            print("Successfully Sent!")

      except: 
            # handling exception  
            # and printing error message 
            print("An Unexpected Error!")