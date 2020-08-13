# Author: Shi Jin <jinzishuai@gmail.com>
# Date: August 12, 2020
import argparse
import json


def main(args=None):
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
    parser.add_argument(
        "-s",
        "--s3-bucket",
        type=str,
        help="""
    the S3 bucket used by AWS SageMaker (standard AWS partition only, ie, not working for China or US-Gov).
    It will be replaced to the corresponding https URL""",
        required=True,
    )
    args = parser.parse_args()

    # Constants
    inputFile = args.input
    label = args.label
    outputFile = args.output
    s3bucket = args.s3_bucket

    s3URL = f"s3://{s3bucket}"
    newURL = f"https://{s3bucket}.s3.amazonaws.com"
    via = {}

    with open(inputFile, "r") as f:
        for line in f:
            gtl = json.loads(line)
            url = gtl["source-ref"]
            url = url.replace(s3URL, newURL)
            annotations = gtl[label]["annotations"]
            viaObj = {"filename": url, "size": -1, "regions": [], "file_attributes": {}}
            for anno in annotations:
                region = {
                    "shape_attributes": {
                        "name": "rect",
                        "x": anno["left"],
                        "y": anno["top"],
                        "width": anno["width"],
                        "height": anno["height"],
                    },
                    "region_attributes": {},
                }
                viaObj["regions"].append(region)
            via[f"{url}-1"] = viaObj

    with open(outputFile, "w") as fp:
        json.dump(via, fp)


if __name__ == "__main__":
    main()
