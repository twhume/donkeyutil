import argparse
from functools import partial
import glob
import json
import numpy
import os
from PIL import Image
import progressbar as pb
from shutil import copyfile, move
from skimage.util import random_noise
import sys
import tempfile

def blank(coords, image_file, json_file):
    """Blank the input image within supplied coordinates
    """
    image_obj = Image.open(image_file)
    pixels = image_obj.load()
    for x in range (coords[0], coords[2]):
        for y in range(coords[1], coords[3]):
            pixels[x,y] = (0,0,0)
    image_obj.save(image_file)

def crop(coords, image_file, json_file):
    """Crop the input image to supplied coordinates
    """
    image_obj = Image.open(image_file)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(image_file)

def noise(level, image_file, json_file):
    image_obj = Image.open(image_file)
    image_data = numpy.asarray(image_obj)
    noised_image = random_noise(image_data, mode='gaussian', var=level)
    noised_image = (255*noised_image).astype(numpy.uint8)
    image_obj = Image.fromarray(noised_image)
    image_obj.save(image_file)




def flip_h(image_file, json_file):
    """Flip the input image horizontally and invert the steering angle to reflect this
    """
    with open(tmp_json_filename) as json_data:
        j = json.load(json_data)

    steering_angle = float(j["user/angle"])
    steering_angle = steering_angle * -1
    j["user/angle"] = steering_angle

    with open(tmp_json_filename, "w") as outfile:
        json.dump(j, outfile)

    image_obj = Image.open(image_file)
    cropped_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    cropped_image.save(image_file)
 
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Process a Donkey Car tub")
    parser.add_argument("tub_in", help="tub directory to read from")
    parser.add_argument("tub_out", help="new tub directory to write to (must not exist)")
    parser.add_argument("--crop",  help="crop image to x,y,w,h")
    parser.add_argument("--blank",  help="blank image to x,y,w,h")
    parser.add_argument("--flip_h", action="store_true", help="flip image and steering value horizontally")
    parser.add_argument("--noise", type=float, help="add gaussian noise, quantity between 0 .. 1.0")
    args = parser.parse_args()

    in_dir = args.tub_in
    out_dir = args.tub_out

    if not(os.path.isdir(in_dir)):
        print("No such directory " + in_dir)
        exit(0)

    if os.path.exists(sys.argv[2]):
        print("Output directory already exists: " + out_dir)
        exit(0)

    os.mkdir(out_dir)

    operations = [];
    if args.crop:
        coords = args.crop.split(",")
        if len(coords)!=4:
            print("Supply 4 coordinates x1,y1,x2,y2 for crop operation (e.g. 0,56,120,160)")
            exit(0)
        coords = list(map(int, coords))
        operations.append(partial(crop, coords=coords))

    if args.blank:
        coords = args.blank.split(",")
        if len(coords)!=4:
            print("Supply 4 coordinates x1,y1,x2,y2 for blank operation (e.g. 0,56,120,160)")
            exit(0)
        coords = list(map(int, coords))
        operations.append(partial(blank, coords=coords))

    if args.flip_h:
        operations.append(flip_h)

    if args.noise:
        level = float(args.noise)
        operations.append(partial(noise, level=level))

    if len(operations)==0:
        print("No operations specified. Try --crop, --flip_h or --noise")
        exit(0)

    # Copy the meta.json across
    copyfile(os.path.join(in_dir, "meta.json"), os.path.join(out_dir, "meta.json"))

    files = glob.glob(os.path.join(in_dir, "record_*.json"))
    progress = pb.ProgressBar(widgets=[pb.Percentage(), pb.Bar()], maxval = len(files)).start()
    progvar = 0

    tmp_dir = tempfile.mkdtemp()
    for f in files:
        json_filename = f[len(in_dir)+1:]
        tmp_json_filename = os.path.join(tmp_dir, json_filename)

        # Copy the JSON to a temp directory
        copyfile(f, tmp_json_filename)

        # Open the JSON, get the image file
        with open(tmp_json_filename) as json_data:
            j = json.load(json_data)
            image_filename = j["cam/image_array"]

        # Copy this to a temp directory
        tmp_image_filename = os.path.join(tmp_dir, image_filename)
        copyfile(os.path.join(in_dir, image_filename), tmp_image_filename)

        for op in operations:
            op(json_file=tmp_json_filename, image_file=tmp_image_filename)

        # Copy our temporary files to their final location
        move(tmp_json_filename, os.path.join(out_dir, json_filename))
        move(tmp_image_filename, os.path.join(out_dir, image_filename))

        progress.update(progvar + 1)
        progvar += 1

    print()
    os.rmdir(tmp_dir)

