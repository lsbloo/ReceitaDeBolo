#!/bin/bash

style=$( dialog --stdout --checklist 'Voce gosta de: ' 0 0 0  rock '' OFF samba '' OFF metal '' OFF jazz '' OFF )

echo 'entao voce gosta de '$style
