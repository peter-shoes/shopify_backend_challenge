#!/bin/bash

sudo killall -9 xterm &
sudo pkill -f 'app.py' &

PORT=8080
pid=`ps ax | grep $PORT | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "No daemon on port $PORT"
else
  sudo kill -9 $pid
  echo "Killed daemon on port $PORT"
fi &
PORT=5000
pid=`ps ax | grep $PORT | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "No daemon on port $PORT"
else
  sudo kill -9 $pid
  echo "Killed daemon on port $PORT"
fi

PORT=5000
pid=`ps ax | grep $PORT | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "No daemon on port $PORT"
else
  sudo kill -9 $pid
  echo "Killed daemon on port $PORT"
fi &
PORT=5000
pid=`ps ax | grep $PORT | awk '{split($0,a," "); print a[1]}' | head -n 1`
if [ -z "$pid" ]; then
  echo "No daemon on port $PORT"
else
  sudo kill -9 $pid
  echo "Killed daemon on port $PORT"
fi
