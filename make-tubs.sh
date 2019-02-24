#!/bin/sh


# Usage make-tubs.sh SRC_TUB

if [ "$#" -ne 1 ] || ! [ -d "$1" ]; then
  echo "Usage: $0 DIRECTORY" >&2
  exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo python $DIR/process_tub.py $1 $1.noise=0.001.1 --noise 0.001
python $DIR/process_tub.py $1 $1.noise=0.001.1 --noise 0.001

echo python $DIR/process_tub.py $1 $1.noise=0.001.2 --noise 0.001
python $DIR/process_tub.py $1 $1.noise=0.001.2 --noise 0.001

echo python $DIR/process_tub.py $1 $1.noise=0.002.1 --noise 0.002
python $DIR/process_tub.py $1 $1.noise=0.002.1 --noise 0.002

echo python $DIR/process_tub.py $1 $1.noise=0.002.2 --noise 0.002
python $DIR/process_tub.py $1 $1.noise=0.002.2 --noise 0.002

echo python $DIR/process_tub.py $1 $1.noise=0.004.1 --noise 0.004
python $DIR/process_tub.py $1 $1.noise=0.004.1 --noise 0.004

echo python $DIR/process_tub.py $1 $1.noise=0.004.2 --noise 0.004
python $DIR/process_tub.py $1 $1.noise=0.004.2 --noise 0.004

echo python $DIR/process_tub.py $1 $1.flip_h --flip_h
python $DIR/process_tub.py $1 $1.flip_h --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.001.1 --noise 0.001 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.001.1 --noise 0.001 --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.001.2 --noise 0.001 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.001.2 --noise 0.001 --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.002.1 --noise 0.002 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.002.1 --noise 0.002 --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.002.2 --noise 0.002 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.002.2 --noise 0.002 --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.004.1 --noise 0.004 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.004.1 --noise 0.004 --flip_h

echo python $DIR/process_tub.py $1 $1.flip_h.noise=0.004.2 --noise 0.004 --flip_h
python $DIR/process_tub.py $1 $1.flip_h.noise=0.004.2 --noise 0.004 --flip_h


