import opening
opening.start()

from import_character import load_character
name, job, item = load_character()



from farmer import chapter1 as f_ch1
from knight import chapter1 as k_ch1
from loyal import chapter1 as l_ch1
from king import chapter1 as ki_ch1

if job == 'farmer':
    f_ch1.start()
elif job == 'knight':
    k_ch1.start()
elif job == 'loyal':
    l_ch1.start()
else:
    ki_ch1.start()
