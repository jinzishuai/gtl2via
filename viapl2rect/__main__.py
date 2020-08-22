# Author: Shi Jin <jinzishuai@gmail.com>
# Date: August 22, 2020
import argparse
import json


def viapl2rect(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="input VIA JSON file with polyline",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="output jVIA JSON file with rect",
        required=True,
    )
    args = parser.parse_args()

    # Constants
    inputFile = args.input
    outputFile = args.output

    with open(inputFile, "r") as fpI:
        via = json.load(fpI)
    for key in via:
        # print(f"{key}")
        regions = via[key]["regions"]
        for region in regions:
            shape = region["shape_attributes"]
            # print("%s" % (shape["name"]))
            if shape["name"] == "polyline":
                allX = shape["all_points_x"]
                allY = shape["all_points_y"]
                boxLeft = min(allX)
                boxRight = max(allX)
                boxTop = min(allY)
                boxBottom = max(allY)
                region["shape_attributes"] = {
                    "name": "rect",
                    "x": boxLeft,
                    "y": boxTop,
                    "width": boxRight - boxLeft,
                    "height": boxBottom - boxTop,
                }

    with open(outputFile, "w") as fpO:
        json.dump(via, fpO)


if __name__ == "__main__":
    viapl2rect()
