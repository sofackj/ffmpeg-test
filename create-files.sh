#!/bin/bash

for file in {1..8}
do
    touch test-app/outputs/my-file-${file}.txt
done