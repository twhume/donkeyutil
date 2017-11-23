#!/usr/bin/python

import json, re, sys
from os import listdir, makedirs
from os.path import isfile, join, exists
import PIL
from PIL import Image
from shutil import copyfile

# Ensure correct arguments passed in

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " input_tub_dir output_tub_dir")
    sys.exit();

# Make the output directory, fail if it already exists
    
output_dir = sys.argv[2]
if exists(output_dir):
    print(output_dir + " already exists, halting")
    sys.exit();
makedirs(output_dir);

input_dir = sys.argv[1]


copyfile(join(input_dir, "meta.json"), join(output_dir, "meta.json"))
copyfile(join(input_dir, "log_car_controls.txt"), join(output_dir, "log_car_controls.txt"))


jsonfiles = [f for f in listdir(input_dir) if (re.match("record_.*\.json", f) and (isfile(join(input_dir, f))))]
for f in jsonfiles:
    j = json.load(open(join(input_dir, f)))
    img = Image.open(join(input_dir, j["cam/image_array"]))
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save(join(output_dir, j["cam/image_array"]))

    j["user/angle"] *= -1;
    json_data = json.dumps(j)
    text_file = open(join(output_dir, f), "w")
    text_file.write(json_data)
    text_file.close()    
    