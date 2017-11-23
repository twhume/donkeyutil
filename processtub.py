#!/usr/bin/python

import json, re, sys
from os import listdir, makedirs
from os.path import isfile, join, exists
import PIL
from PIL import Image, ImageDraw
from shutil import copyfile

def mirror(img, data):
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    data["user/angle"] *= -1
    return (flipped, data)

def blank_horizon(img, data):
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,160,50],(0,0,0,0),(0,0,0,0))
    del draw
    return (img, data)



# Ensure correct arguments passed in

if len(sys.argv) != 4:
    print("Usage: " + sys.argv[0] + " (mirror|blank_horizon) input_tub_dir output_tub_dir")
    sys.exit();
op_name = sys.argv[1]
op = locals()[op_name]

# Make the output directory, fail if it already exists
    
output_dir = sys.argv[3]
if exists(output_dir):
    print(output_dir + " already exists, halting")
    sys.exit();
makedirs(output_dir);

input_dir = sys.argv[2]


copyfile(join(input_dir, "meta.json"), join(output_dir, "meta.json"))
copyfile(join(input_dir, "log_car_controls.txt"), join(output_dir, "log_car_controls.txt"))


jsonfiles = [f for f in listdir(input_dir) if (re.match("record_.*\.json", f) and (isfile(join(input_dir, f))))]
for f in jsonfiles:
    j = json.load(open(join(input_dir, f)))
    img = Image.open(join(input_dir, j["cam/image_array"]))

    (new_img, new_json) = op(img, j);
    new_img.save(join(output_dir, j["cam/image_array"]))
    
    json_data = json.dumps(new_json)
    text_file = open(join(output_dir, f), "w")
    text_file.write(json_data)
    text_file.close()    
    

    
