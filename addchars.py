#!/bin/python

from addcharslib import *

def modifySource(sfd, f, s, sn):
    print sfd

    workshop = 1.4
    if f == 'Nirmal':
        upm2048 = 1000.0/2048.0
        upm1000 = 1.0
    else:
        upm2048 = 1.0
        upm1000 = 2048.0/1000.0
    scale2048 = '-s ' + str(upm2048/workshop) + ' '
    scale1000 = '-s ' + str(upm1000/workshop) + ' '

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = scale2048 + '-i ' + annapurna + asn + '.ttf' + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    if f == 'Elur':
        sns = s.replace('-', '')
        cmd = scale1000 + ' -i ' + sophia + sns + '.ttf' + ' --rangefile cs/sophia/main.txt'
        modifyFile(cmd, sfd)
        cmd = scale2048 + '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4sophia.txt --rangefile cs/charis/extra4sophia.txt'
        modifyFile(cmd, sfd)
    else:
        gs = s.replace('-', '')
        cmd = scale2048 + '-i ' + gentium + gs + '.ttf' + ' --namefile cs/gentium/main_glyphs.txt --rangefile cs/gentium/pre.txt --rangefile cs/gentium/main.txt'
        modifyFile(cmd, sfd)
        cmd = scale2048 + '-i ' + charis + s + '.ttf' + ' --rangefile cs/charis/composite4gentium.txt --rangefile cs/charis/extra4gentium.txt'
        modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
