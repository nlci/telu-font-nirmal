#!/bin/bash

face="$1"
style="$2"
ufo="$3"

if [ "${face}" = "Nirmal" ]
then
    devaf="Maurya"
    tamlf="Vaigai"
else
    devaf="Panini"
    tamlf="ThiruValluvar"
fi

psfcopyglyphs -f --rename rename --unicode usv -i ../cs/panini/main4telu.csv -s "${deva}/${devaf}-${style}.ufo" ${ufo}
psfcopyglyphs -f --rename rename --unicode usv -i ../cs/thiruvalluvar/main.csv -s "${taml}/${tamlf}-${style}.ufo" ${ufo}
