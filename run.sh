#!/bin/bash

cd client

xterm -hold -e python ../app.py &

xterm -hold -e npm run serve 