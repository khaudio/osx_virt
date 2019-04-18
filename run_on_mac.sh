#!/bin/bash

set -e
git clone https://github.com/PassthroughPOST/Hackintosh-KVM
chmod +x Hackintosh-KVM/create_iso_highsierra.sh
./Hackintosh-KVM/create_iso_highsierra.sh
