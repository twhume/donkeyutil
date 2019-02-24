#!/usr/bin/python

import json, re, sys
from os import listdir, makedirs
from os.path import isfile, join, exists
from shutil import copyfile

# Ensure correct arguments passed in

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " session_dir tub_dir")
    sys.exit();

# Make the output directory, fail if it already exists
    
tub_dir = sys.argv[2]
if exists(tub_dir):
    print(tub_dir + " already exists, halting")
    sys.exit();
makedirs(tub_dir);

# Create a meta.json in the output directory

meta_file = open(join(tub_dir, "meta.json"), "w")
meta_data = {}
meta_data["inputs"] = ["cam/image_array","user/angle","user/throttle","user/mode"]
meta_data["types"] = ["image_array","float","float","str"]
meta_file.write(json.dumps(meta_data))

# Create an empty log_car_controls.txt in the output directory

log_file = open(join(tub_dir, "log_car_controls.txt"), "w")


# Create individual image and JSON record files in the output tub directory,
# based on image files and their names from the input session directory

session_dir = sys.argv[1]
onlyfiles = [f for f in listdir(session_dir) if isfile(join(session_dir, f))]
pattern = re.compile("frame_(?P<n1>.*?)_ttl_(?P<n2>.*?)_agl_(?P<n3>.*?)_mil_(?P<n4>.*?).jpg")

for idx,f in enumerate(onlyfiles):
    
    output_img_file = str(idx)+ "_cam-image_array_.jpg"
    copyfile(join(session_dir, f), join(tub_dir, output_img_file))
    
    match = pattern.match(f);
    frame = int(match.group("n1"))
    throttle = float(match.group("n2"))
    angle = float(match.group("n3"))

    data = {}
    data["cam/image_array"] = output_img_file
    data["user/throttle"] = throttle
    data["user/angle"] = angle
    data["user/mode"] = "user";
    json_data = json.dumps(data);
    
    output_json_file = "record_" + str(idx) + ".json"
    text_file = open(join(tub_dir, output_json_file), "w")
    text_file.write(json_data)
    text_file.close()
    
