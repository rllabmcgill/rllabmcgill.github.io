#!/bin/bash
jekyll build
if [ $? -ne 0 ]; then
    exit 1
fi
mkdir build
tar -czvf build/build.tar.gz -C _site .
cp ci-deploy.sh ./build
