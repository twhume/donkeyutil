# donkeyutil
Utilities written to help training a Donkey (see diyrobocars.com)

These two scripts help extract good training data from sessions.

makevideo.sh &lt;SESSION DIRECTORY&gt; &lt;OUTPUT VIDEO&gt;
Turns a session directory into a video with the correct frame-rate, and the actual frame numbers overlaid into the video. See sample output at https://goo.gl/photos/h9RzsU8osPy9eHCv7

cutsegment.sh &lt;SESSION DIRECTORY&gt; &lt;OUTPUT DIRECTORY ROOT&gt; &lt;START FRAME&gt; &lt;END FRAME&gt;
Extract a sequence of frames from a session and save them into a new directory of the form &lt;OUTPUT DIRECTORY ROOT&gt;_&lt;NUMBER&gt;,
incrementing NUMBER as necessary. 


