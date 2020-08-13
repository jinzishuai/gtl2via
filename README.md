# Converter from AWS SageMaker Ground Truth Label Job Manifest file to VGG Image Annotator

## Context 

### AWS SageMaker Ground Truth Label Job (GLT)

* https://docs.aws.amazon.com/sagemaker/index.html

### VGG Image Annotator (VIA)

* project: http://www.robots.ox.ac.uk/~vgg/software/via/
* code repo: https://gitlab.com/vgg/via/-/tree/master

# Usage

```bash
~/src/gtl2via$ python gtl2via.py -h
usage: gtl2via.py [-h] -i INPUT -l LABEL -o OUTPUT

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input manifest file for AWS SageMaker GTL job
  -l LABEL, --label LABEL
                        use the label from the manifest file
  -o OUTPUT, --output OUTPUT
                        output json file of VIA
 ```
 
## Example 
 
```
gtl2via$ python gtl2via.py -i test/defect_boxes.manifest -o test/via.json -l zerobox-quick-detection
```

The output json looks like this
```json
(zerobox) seki@xubuntu-20:~/src/gtl2via$ cat test/via.json |jq |head -n 20
{
  "/home/seki/src/zerobox-v2/output/2020-08-11/good/Camera0_202008111525251_original.png-1": {
    "filename": "/home/seki/src/zerobox-v2/output/2020-08-11/good/Camera0_202008111525251_original.png",
    "size": -1,
    "regions": [
      {
        "shape_attributes": {
          "name": "rect",
          "x": 512,
          "y": 896,
          "width": 519,
          "height": 1024
        },
        "region_attributes": {}
      }
    ],
    "file_attributes": {}
  },
...
```
