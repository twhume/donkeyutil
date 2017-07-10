#!/bin/sh

if [ $# -ne 2 ]
  then
    echo "Usage: makevideo.sh <SESSION DIRECTORY> <OUTPUT VIDEO>"
    exit
fi

INDIR=$1
if [ ! -d "$DIRECTORY" ]
  then
    echo "Session directory $INDIR does not exist"
    exit
fi

OUTFILE=$(pwd)/$2
CURDIR=$(pwd)
OUTDIR=/tmp/movie-$$
mkdir $OUTDIR
cd $INDIR
for i in `ls -1 `; do cp $i $OUTDIR/`echo $i | cut -f 1-2 -d '_'`.jpg; done
FIRST=`ls -1 | head -1 | cut -f 2 -d '_'`
ffmpeg -r 12.5 -f image2 -s 160x120 -start_number $FIRST -i $OUTDIR/frame_%05d.jpg -vcodec libx264 -crf 25 -vf "drawtext=fontfile=Arial.ttf: text=%{eif\\\:n+$FIRST\\\:d} : x=(w-tw)/2: y=h-(2*lh): fontcolor=white: box=1: boxcolor=0x00000099" -pix_fmt yuv420p $OUTFILE
rm -rf $OUTDIR 
cd $CURDIR

