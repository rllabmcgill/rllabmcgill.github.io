#!/bin/bash
rm -rf $1/tmp
mkdir $1/tmp
tar -xzvf $1/tar/build.tar.gz -C $1/tmp
rsync -Pav --delete-after $1/tmp/ $1
