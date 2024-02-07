#!/bin/bash
mogrify -strip ./*.jpg
jpegoptim --size=900k -s ./*.jpg
