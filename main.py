import time
import os
from datetime import datetime 
import pytz 
i=5
GMT = pytz.timezone('America/Sao_paulo')
while i==5:
    datetime_gmt = datetime.now(GMT)
    print("horario de Brasília: ", datetime_gmt.strftime('%H:%M:%S'))
    time.sleep(1)
    os.system('clear')
