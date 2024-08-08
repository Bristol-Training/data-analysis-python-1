#!/bin/bash
for filename in *.ipynb; do
    quarto convert $filename
done
