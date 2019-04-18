#!/bin/bash

bash <(curl -s https://raw.githubusercontent.com/Benjamin-Dobell/nvidia-update/master/nvidia-update.sh)

wget https://sourceforge.net/projects/cloverefiboot/files/latest/download
mv download clover.zip
unzip clover.zip
