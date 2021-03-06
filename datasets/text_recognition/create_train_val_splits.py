import argparse
import json
import os

import random


def main(args):
    # with open(args.gt_file) as f:
    #     gt_data = json.load(f)

    with open(args.gt_file) as f:
        gt_data = f.readlines()

    # metadata = None
    # if "file_name" not in gt_data[0]:
    #     # we do not want to distribute the metadata, but we have to save it for later
    #     metadata = gt_data.pop(0)

    number_of_images = len(gt_data)
    num_validation_images = int(number_of_images * args.val_ratio)

    random.shuffle(gt_data)

    validation_images = gt_data[:num_validation_images]
    train_images = gt_data[num_validation_images:]

    gt_dir = os.path.dirname(args.gt_file)

    with open(os.path.join(gt_dir, "validation.txt"), "a") as f:
        # if metadata is not None:
        #     validation_images.insert(0, metadata)
        # json.dump(validation_images, f, indent=2)
        for item in validation_images:
            f.write(item)

    with open(os.path.join(gt_dir, "train.txt"), "a") as f:
        # if metadata is not None:
        #     train_images.insert(0, metadata)
        # json.dump(train_images, f, indent=2)
        for item in train_images:
            f.write(item)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool that takes a gt json file and creates a training, validation and reference gt")
    parser.add_argument("gt_file")
    parser.add_argument("--val-ratio", type=float, default=0.1, help="ratio for validation images")

    args = parser.parse_args()
    main(args)
