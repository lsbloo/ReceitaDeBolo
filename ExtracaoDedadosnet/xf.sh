#!/bin/bash

URL="https://www.youtube.com"


curl -sS $URL | grep -i '[A-Z]' | > y.txt

