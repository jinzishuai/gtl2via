#!/bin/bash

# Absolute path to this script
SCRIPT=$(readlink -f $0)
# Absolute path this script is in
SCRIPTPATH=`dirname $SCRIPT`
TOPFOLDER=$(dirname $SCRIPTPATH)

sudo apt install -y jq
pushd $TOPFOLDER

python -m gtl2via -i test/defect_boxes.manifest -o test/via.json -l zerobox-quick-detection -s zerobox-public

if [[ $(cat test/via.json |wc -m) == 4403 ]]; then
    echo "Correct results"
    exit 0
else
    echo "Wrong results:"    
    cat test/via.json | jq
    exit 1
fi

python -m viapl2rect -i test/polyline.json -o test/rect.json

if [[ $(cat test/rect.json |jq |grep rect|wc -l) == 2 ]]; then
    echo "Correct results"
    exit 0
else
    echo "Wrong results: expected to find two rect"    
    cat test/rect.json |jq
    exit 2
fi
popd