#!/bin/bash

# Absolute path to this script
SCRIPT=$(readlink -f $0)
# Absolute path this script is in
SCRIPTPATH=`dirname $SCRIPT`
TOPFOLDER=$(dirname $SCRIPTPATH)

pushd $TOPFOLDER

python gtl2via.py  -i test/defect_boxes.manifest -o test/via.json -l zerobox-quick-detection -s zerobox-public

if [[ $(cat test/via.json |wc -m) == 4403 ]]; then
    echo "Correct results"
    exit 0
else
    apt install -y jq
    echo "Wrong results:"    
    cat test/via.json | jq
fi

popd