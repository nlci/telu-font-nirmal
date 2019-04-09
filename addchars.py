#!/usr/bin/python3

from addcharslib import *

for f in faces:

    workshop = 1.4
    if f == 'Nirmal':
        upm2048 = 1000.0/2048.0
        upm1000 = 1.0
    else:
        upm2048 = 1.0
        upm1000 = 2048.0/1000.0
    scale2048 = str(upm2048/workshop)
    scale1000 = str(upm1000/workshop)

    for sn in stylesName:
        if f == 'Elur':
            modifyFile(scale1000, 'sourcesans', f, sn)
            modifyFile(scale2048, 'charis', f, sn)
        else:
            modifyFile(scale2048, 'gentium', f, sn)
