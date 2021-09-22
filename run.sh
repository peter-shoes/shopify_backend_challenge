#!/bin/bash

cd client
npm install 
npm install @vue/cli

xterm -hold -e python ../app.py &

xterm -hold -e npm run serve