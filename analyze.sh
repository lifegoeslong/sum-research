#!/bin/bash

qqmusic &
sleep 60 # begin the app

songs=("RISE" "Victory")
for s in "${songs[@]}"; do

	xdotool mousemove 418 43 # this is the search line
	sleep 0.5
	xdotool click 1
	xdotool type "$s
"
	sleep 1
	xdotool mousemove 844 259 #play the first song
	xdotool click 1
	sleep 5 #end playing

	xdotool mousemove 306 980
	xdotool clcik 1
	sleep 0.5

	xdotool mousemove 954 966 #this is playing button
	xdotool click 1           #stop playing music
	sleep 1

	l=${#s}
	xdotool mousemove 418 45 #ths is deleting line
	xdotool click 1
	for ((c = 1; c <= $l; c++)); do
		echo 1
		xdotool key BackSpace
		sleep 0.5
	done
	echo "one round done"
done
