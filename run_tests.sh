#!/bin/bash

# Exit immediately if a command fails
set -e

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest

# If pytest exits successfully, script exits with code 0
# If pytest fails, script exits with code 1 automatically
