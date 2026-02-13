import time 
from clockdeco_param import clock


@clock('{name}: {elapsed:0.5f}s')
def snooze(seconds):
    time.sleep(seconds)
    
    
    
@clock("{name}: {elapsed:0.5f}")
def snooze_test(seconds):
    time.sleep(seconds)

for i in range(3):
    snooze(.123)
    '''
    snooze: 0.1254244900046615s
    snooze: 0.12827817199286073s
    snooze: 0.1276620400021784s
    '''
 

for i in range(5):
    snooze_test(.234)