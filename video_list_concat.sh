#!/bin/bash
for i in `ls *.ts | sort -V`; do echo "file $i"; done >> videolist.txt
ffmpeg -f concat -i videolist.txt -c copy -bsf:a aac_adtstoasc video.mp4
