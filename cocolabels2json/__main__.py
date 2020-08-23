# Author: Shi Jin <jinzishuai@gmail.com>
# Date: August 22, 2020
import argparse
import json

cocoLabels = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]


def cocolabels2json(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--output", type=str, help="output JSON file", required=True,
    )
    args = parser.parse_args()

    # Constants
    outputFile = args.output
    labels = []
    i = 0
    for label in cocoLabels:
        print(f"{label}")
        labels.append({"name": label, "id": i})
        i += 1

    with open(outputFile, "w") as fpO:
        json.dump(labels, fpO)


if __name__ == "__main__":
    cocolabels2json()
