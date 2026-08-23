#!/bin/bash

# Check if the script is being run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root or with sudo."
    exit 1
fi

echo "Removing unused dependencies..."
apt autoremove -y

echo "Updating software database..."
apt update

echo "Upgrading the system..."
apt upgrade -y

echo "System update complete."