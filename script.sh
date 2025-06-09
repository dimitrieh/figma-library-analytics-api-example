#!/bin/bash

# Check if running on macOS
if [[ "$(uname)" != "Darwin" ]]; then
    echo "This script is intended to run on macOS only."
    exit 1
fi

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "Homebrew is not installed. Please install Homebrew first: https://brew.sh/"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is installed."
fi

# Check for Python3
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Installing with Homebrew..."
    brew install python3
else
    echo "Python3 is installed."
fi

# Check for pip3
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Attempting to install with Homebrew..."
    brew install python  # pip3 comes with Homebrew's python
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 installation failed. Please install pip3 manually."
        exit 1
    fi
else
    echo "pip3 is installed."
fi

echo "Success: Homebrew, Python3, and pip3 are installed. Now going to install pip3 dependencies in a virtual environment."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate it
source venv/bin/activate

# Install dependencies
pip3 install --upgrade pip3
pip3 install requests python-dotenv pandas datetime

# Save dependencies
pip3 freeze > requirements.txt

echo "Now running the Python scripts to extract library data..."

python3 extract-library-data.py

echo "Extraction complete. Please check the output folders for the results."
