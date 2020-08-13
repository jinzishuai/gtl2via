# Converter from AWS SageMaker Ground Truth Label Job Manifest file to VGG Image Annotator

## Context 

### AWS SageMaker Ground Truth Label Job (GLT)

* https://docs.aws.amazon.com/sagemaker/index.html

### VGG Image Annotator (VIA)

* project: http://www.robots.ox.ac.uk/~vgg/software/via/
* code repo: https://gitlab.com/vgg/via/-/tree/master

### Why do we need this?

The AWS SageMaker Ground Truth labelling jobs are very nice, especially when we want to out source the tedious labelling job to prepare for machine learning trainings.  It also supports the job of adjust existing boxes, where some code/algorithm is already generating the bounding boxes for certain objects. In this case, we could use the Ground Truth jobs to view existing boxes and adjust them. However, the AWS system currently do not offer an easy way to preview all the existing boxes until all the objects are manually labelled (there is a $0.08/object charge for each labelling operation and it makes business for AWS to want to encourage that).

VIA offers a very powerful way to view all/multiple/selective images with their annotations and it works on any platform out of the box without much installation (just checkout the code and launch the index.html using broswer).

The idea here is to take a already generated AWS SageMaker manifest file and convert it into the annotation json file used by VIA.

# Usage

```bash
usage: gtl2via.py [-h] -i INPUT -l LABEL -o OUTPUT -s S3_BUCKET

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input manifest file for AWS SageMaker GTL job
  -l LABEL, --label LABEL
                        use the label from the manifest file
  -o OUTPUT, --output OUTPUT
                        output json file of VIA
  -s S3_BUCKET, --s3-bucket S3_BUCKET
                        the S3 bucket used by AWS SageMaker (standard AWS partition only, ie, not working for China or US-Gov). It will be replaced to the corresponding https URL
 ```
 
## Example 
 
```
gtl2via$ python gtl2via.py  -i test/defect_boxes.manifest -o test/via.json -l zerobox-quick-detection -s zerobox-images
```

The output json looks like this
```json
seki@seki-Surface-Book:~/src/gtl2via$ cat test/via.json |jq 
{
  "https://zerobox-images.s3.amazonaws.com/test/2020-08-12/good/Camera0_202008121004202_original.png-1": {
    "filename": "https://zerobox-images.s3.amazonaws.com/test/2020-08-12/good/Camera0_202008121004202_original.png",
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
```

# Known Limitations (ToDo)

* It only works with S3 in aws (Standard Regions), not for aws-cn (China Regions) or aws-us-gov (AWS GovCloud [US] Regions).
* It only works with one annotation type: `rect`
* No choice of box color yet for different classes in SageMaker
