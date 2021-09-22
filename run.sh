#!/bin/bash

cd client

xterm -hold -e python ../app.py &

xterm -hold -e npm install & npm install @vue/cli & npm run serve 