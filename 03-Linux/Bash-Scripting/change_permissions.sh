#!/bin/bash

# Check if a folder was provided
if [ $# -ne 1 ]; then
    echo "Usage: ./change_permissions.sh <folder>"
    exit 1
fi

# Change permissions of all objects in the folder
chmod -R 644 "$1"

echo "Permissions changed to -rw-r--r-- for all objects in $1"