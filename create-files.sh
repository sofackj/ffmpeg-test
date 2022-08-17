#!/bin/bash

for file in {1..8}
do
    touch test-app/entries/my-file-${file}.txt
done