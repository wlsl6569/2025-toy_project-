import opening
import json

opening.start()


import import_character
from servant import chapter1 as s_ch1
from farmer import chapter1 as f_ch1
from knight import chapter1 as k_ch1
from loyal import chapter1 as l_ch1
from king import chapter1 as ki_ch1


name, job, item = import_character.load_character()

if job == 'servant':
    s_ch1.start()
elif job == 'farmer':
    f_ch1.start()
elif job == 'knight':
    k_ch1.start()
elif job == 'loyal':
    l_ch1.start()
else:
    ki_ch1.start()