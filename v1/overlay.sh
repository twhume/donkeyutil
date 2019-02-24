#!/bin/sh

mkdir overlayed
for i in `ls -1 $1`; do
 echo $i
 mkdir overlayed/$i
 cd $1/$i
 for j in *jpg; do
  convert -composite $j ../../overlay.png ../../overlayed/$i/$j 
  done
 cd ../..
 done

