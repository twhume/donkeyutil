#!/bin/sh

if [ $# -ne 4 ]
  then
    echo "Usage: cutsegment.sh <SESSION DIRECTORY> <OUTPUT DIRECTORY ROOT> <START FRAME> <END FRAME>"
    exit
fi

INDIR=$1
if [ ! -d "$INDIR" ]
  then
    echo "Session directory $INDIR does not exist"
    exit
fi

OUTDIR=$2
max=`ls -1d $OUTDIR* 2>/dev/null | tr -dc '[0-9\n]' | sort -k 1,1n | tail -1`
OUTDIR=${OUTDIR}_$((max + 1))
mkdir $OUTDIR

STARTFRAME=$3
ENDFRAME=$4
for ((i=$STARTFRAME;i<=$ENDFRAME;i++));
do
	printf -v FRAME "frame_%05d_*" $i
	cp $INDIR/$FRAME $OUTDIR/
done
