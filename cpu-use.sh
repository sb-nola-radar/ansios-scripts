#!/bin/bash

# Note: change '-bn1' to 'bn4' if you have 4 CPUs

top -bn 1 | awk '{print $9}' | tail -n +8 | awk '{s+=$1} END {print s}'
