#!/bin/bash

face="$1"
style="$2"
ufo="$3"

if [ "${face}" = "Nirmal" ]
then
    devaf="Maurya"
else
    devaf="Panini"
fi

psfcopyglyphs -f --rename rename --unicode usv -i ../cs/panini/main4telu.csv -s "${deva}/${devaf}-${style}.ufo" ${ufo}
