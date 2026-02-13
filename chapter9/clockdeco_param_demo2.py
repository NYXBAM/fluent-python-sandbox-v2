import time
from clockdeco_param import clock

@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)
    
for _ in range(5):
    snooze(.512)
    
    
'''
snooze(0.512) dt=0.517s
snooze(0.512) dt=0.514s
snooze(0.512) dt=0.513s
snooze(0.512) dt=0.512s
snooze(0.512) dt=0.512s
'''
