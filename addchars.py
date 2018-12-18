#!/bin/python

import os
import os.path
import sys

from wscript import *

charis_dir = '../../../latn/fonts/charis_local/5.000/zip/unhinted/'
charis_ttf = '/CharisSIL'
gentium_dir = '../../../latn/fonts/gentium_local/basic/1.102/zip/unhinted/'
sophia_dir = '../../../copt/fonts/sophia_nubian/1.000/zip/unhinted/'
sophia_ttf = '/SN'
gentium_ttf = '/GenBkBas'
annapurna_dir = '../../../deva/fonts/annapurna_local/1.203/zip/unhinted/'
annapurna_ttf = '/AnnapurnaSIL-'
panini = '../../../deva/fonts/panini-master/source/Panini'
deva = '../../../deva/fonts/panini/source/'
thiruvalluvar = '../../../taml/fonts/thiruvalluvar/source/ThiruValluvar'
vaigai = '../../../taml/fonts/thiruvalluvar/source/Vaigai'
exo = '../../../latn/fonts/exo/1.500/zip/unhinted/1000/Exo-'

def runCommand(cmd, ifont, ofont):
    cmd = 'ffcopyglyphs' + ' -f ' + cmd + ' ' + ifont + ' ' + ofont
    print cmd
    os.system(cmd)

def findFile(filename):
    return os.path.join(sys.argv[1], filename)

def modifyFile(cmd, filename):
    tmp = 'tmp.sfd'
    os.rename(findFile(filename), tmp)
    runCommand(cmd, tmp, findFile(filename))
    os.remove(tmp)

def modifySource(sfd, f, s, sn):
    print sfd

    if f == 'Nirmal':
        emsize = '1000'
        emext = '.sfd'
        emopt = '-s ' + str(1000.0/2048.0/1.4) + ' '
        devaf = 'Maurya'
    else:
        emsize = '2048'
        emext = '.ttf'
        emopt = '-s ' + str(1/1.4) + ' '
        devaf = 'Panini'

    #cmd = '-i ' + deva + devaf + '-' + sn + '.sfd' + ' --rangefile cs/panini/main4telu.txt'
    #modifyFile(cmd, sfd)

    asn = sn
    asn = asn.replace('BoldItalic', 'Bold')
    asn = asn.replace('Italic', 'Regular')
    cmd = '-s ' + str(1/1.4) + ' ' + '-i ' + annapurna_dir + emsize + annapurna_ttf + asn + emext + ' --rangefile cs/annapurna/main.txt'
    modifyFile(cmd, sfd)

    if f == 'Elur':
        sns = s.replace('-', '')
        cmd = '-s ' + str(2048.0/1000.0/1.4) + ' -i ' + sophia_dir + '1000' + sophia_ttf + sns + '.ttf' + ' --rangefile cs/sophia/main.txt'
        modifyFile(cmd, sfd)
        cmd = emopt + '-i ' + charis_dir + '2048' + charis_ttf + s + '.ttf' + ' --rangefile cs/charis/composite4sophia.txt --rangefile cs/charis/extra4sophia.txt'
        modifyFile(cmd, sfd)
    else:
        gs = s.replace('-', '')
        cmd = emopt + '-i ' + gentium_dir + '2048' + gentium_ttf + gs + '.ttf' + ' --namefile cs/gentium/main_glyphs.txt --rangefile cs/gentium/pre.txt --rangefile cs/gentium/main.txt'
        modifyFile(cmd, sfd)
        cmd = emopt + '-i ' + charis_dir + '2048' + charis_ttf + s + '.ttf' + ' --rangefile cs/charis/composite4gentium.txt --rangefile cs/charis/extra4gentium.txt'
        modifyFile(cmd, sfd)

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        sn = sn.replace(' ', '')
        modifySource(f + '-' + sn + '.sfd', f, s, sn)
