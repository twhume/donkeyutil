# donkeyutil
Utilities written to help training a Donkey (see diyrobocars.com). These are pretty rough and ready.

# Scripts for Donkey v1 (probably obsolete now)
All the scripts in the v1 subdirectory help extract good training data from sessions, so are all for v1 Donkey

`makevideo.sh <SESSION DIRECTORY> <OUTPUT VIDEO>`  
Turns a session directory into a video with the correct frame-rate, and the actual frame numbers overlaid into the video. See sample output [here](https://goo.gl/photos/h9RzsU8osPy9eHCv7)

`cutsegment.sh <SESSION DIRECTORY> <OUTPUT DIRECTORY ROOT> <START FRAME> <END FRAME>`  
Extract a sequence of frames from a session and save them into a new directory of the form &lt;OUTPUT DIRECTORY ROOT&gt;_&lt;NUMBER&gt;, incrementing NUMBER as necessary. 

`batch.sh <CSV FILE> <SESSION DIRECTORY> <OUTPUT DIRECTORY>`  
Take a CSV file listing sessions and segments, and extract all of them into separate directories using `cutsegment.sh`

`train.sh <DONKEY DIRECTORY> <SESSIONS DIRECTORY> <CSV FILE> <MODEL NAME>`  
Kicks off training a new model using all the segment names in the CSV file

`train.sh <DONKEY DIRECTORY> <SESSIONS DIRECTORY> <CSV FILE> <MODEL NAME>`  
Kicks off training a new model using all the segment names in the CSV file

These scripts support the new v2 Donkey

`python session2tub.py <SESSION DIRECTORY> <TUB DIRECTORY>`  
Converts an old v1 Donkey session to the new v2 tub format

`python processtub.py <OP> <INPUT> <OUTPUT>`  
Takes an input tub, applies the function named <OP> (currently mirror or blank_horizon), outputs a new tub

# My workflow

(Old, for Donkey v1) Using these scripts:

1. Record a training session as per normal
1. Use `makevideo.sh` to turn it into a video
1. Play the video (in Quicktime on Mac) and record start and end frames for each useful segment in a spreadsheet like [this](https://docs.google.com/spreadsheets/d/1OGm7YjxCvQ6SWKb-KafAnEZpwtLmpNko2brxZ1VrZBE/edit?usp=sharing). I have a magic mouse which lets me quickly scrub forwards and backwards through a video.
1. Download the first tab of this spreadsheet as a CSV
1. Use `batch.sh` to extract my selections from my sessions, then copy them into my session directory
1. Use `train.sh` to train a new model

Compared to manually running through sessions using the Donkey web server and deleting individual frames, I find this faster and more accurate.
