#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r backend/requirements.txt

# Create necessary directories
mkdir -p uploads
mkdir -p data
