#!/bin/sh

if [ $# -ne 4 ]
  then
    echo "Usage: train.sh <DONKEY DIRECTORY> <SESSIONS DIRECTORY> <CSV FILE> <MODEL NAME>"
    exit
fi



CURDIR=$(pwd)
DONKEYHOME=$1
SESSIONS=$2
CSVFILE=$3
MODELNAME=$4

ROOTNAMES=`cat $CSVFILE | cut -f 2 -d "," | grep -v "Track segment" | sort -u`
TMPFILE=/tmp/train-$$
cd $SESSIONS
for i in $ROOTNAMES; do
	ls -1d ${i}_* >> $TMPFILE
done
ALLFILES=`cat $TMPFILE | tr '\n' ','`
cd $DONKEYHOME
python scripts/train.py --sessions=$ALLFILES --name=$MODELNAME
rm $TMPFILE

cd $CURDIR
