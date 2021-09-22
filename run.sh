#!/bin/bash

cd client
npm install 
npm install @vue/cli

cd ..
xterm -hold -e python app.py &

xterm -hold -e npm run serve


