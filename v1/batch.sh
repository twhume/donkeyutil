#!/bin/sh

if [ $# -ne 3 ]
  then
    echo "Usage: batch.sh <CSV FILE> <SESSIONS DIRECTORY> <OUTPUT DIRECTORY>"
    exit
fi

CSVFILE=$1
SESSIONDIR=$2
OUTPUTDIR=$3

while IFS=, read session segment start end length
do
    echo $session $segment $start $end
    cutsegment.sh $SESSIONDIR/$session $OUTPUTDIR/$segment $start $end  
done < $CSVFILE

