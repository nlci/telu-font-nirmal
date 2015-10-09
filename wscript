# nirmal

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='telu'
APPNAME='nlci-' + script
VERSION='0.911'
TTF_VERSION='0.911'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Telugu Unicode font with OT support'
DESC_LONG='''
Pan Telugu font designed to support all the languages using the Telugu script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0c15'

# set fonts to build
#faces = ('Asha', 'Elur', 'Nirmal')
#styles = ('-R', '-B', '-I', '-BI')
#stylesName = ('Regular', 'Bold', 'Italic', 'Bold Italic')

faces = ('Nirmal',)
styles = ('-R',)
stylesName = ('Regular',)

# set build parameters
fontbase = 'source/'
tag = script.upper()

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        font(target = process(tag + f + '-' + sn + '.ttf',
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            sfd_master = fontbase + 'master.sfd',
            opentype = internal(),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-l last --autodefines',
            #    params = '-d'),
            classes = fontbase + 'nirmal_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Nirmal', 'Asha', 'Elur', 'NLCI'),
            woff = woff(),
            script = 'telu',
            fret = fret(params = '-r')
            )
