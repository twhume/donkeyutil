# donkeyutil
Utilities written to help training a Donkey (see diyrobocars.com)

These two scripts aim to ease the process of extracting good training data from sessions.

makevideo.sh <SESSION DIRECTORY> <OUTPUT VIDEO>
Turns a session directory into a video with the correct frame-rate, and the actual frame numbers overlaid into the video.

cutsegment.sh <SESSION DIRECTORY> <OUTPUT DIRECTORY ROOT> <START FRAME> <END FRAME>
Extract a sequence of frames from a session and save them into a new directory of the form <OUTPUT DIRECTORY ROOT>_<NUMBER>,
incrementing NUMBER as necessary. 


