# Author: Shi Jin <jinzishuai@gmail.com>
# Date: August 12, 2020
import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--input",
    type=str,
    help="input manifest file for AWS SageMaker GTL job",
    required=True,
)
parser.add_argument(
    "-l",
    "--label",
    type=str,
    help="use the label from the manifest file",
    required=True,
)
parser.add_argument(
    "-o", "--output", type=str, help="output json file of VIA", required=True
)
args = parser.parse_args()

# Constants
inputFile = args.input
label = args.label
outputFile = args.output
via = {}

with open(inputFile, "r") as f:
    for line in f:
        gtl = json.loads(line)
        url = gtl["source-ref"]
        annotations = gtl[label]["annotations"]
        viaObj = {"filename": url, "size": -1, "regions": []}
        for anno in annotations:
            region = {
                "shape_atttributes": {
                    "name": "rect",
                    "x": anno["left"],
                    "y": anno["top"],
                    "width": anno["width"],
                    "heighht": anno["height"],
                }
            }
            viaObj["regions"].append(region)
        via[f"{url}-1"] = viaObj

with open(outputFile, "w") as fp:
    json.dump(via, fp)
