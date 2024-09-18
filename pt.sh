#!/bin/bash

# Get the current directory
current_dir=$PWD

# Function to create and activate virtual environment
create_and_activate_venv() {
    echo "Creating a fresh virtual environment..."
    # Remove existing .venv if it exists
    rm -rf .venv
    # Create new virtual environment
    python3 -m venv .venv
    # Activate the new virtual environment
    source .venv/bin/activate
    # Install requirements
    if [ -f "requirements.txt" ]; then
        echo "Installing requirements from requirements.txt..."
        pip install -r requirements.txt
    else
        echo "requirements.txt not found. Installing pytest..."
        pip install pytest
    fi
    return 0
}

# Create and activate virtual environment
if create_and_activate_venv; then
    echo "Virtual environment created and activated."
else
    echo "Failed to create or activate virtual environment. Exiting."
    exit 1
fi

# Add the project root to PYTHONPATH
export PYTHONPATH="$current_dir:$PYTHONPATH"

# Run pytest for all files matching the patterns *.test.py and test_*.py
echo "Running Python tests in $current_dir/test directory"
pytest -v "$current_dir/test"

# Store the exit status
exit_status=$?

# Check the exit status
if [ $exit_status -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above for details."
fi

# Deactivate virtual environment
deactivate
echo "Virtual environment deactivated."

# Clean up the virtual environment
rm -rf .venv
echo "Virtual environment removed."

exit $exit_status
