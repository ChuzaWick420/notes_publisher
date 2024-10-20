#!/bin/bash

# Define the parent directory where the search will start
repo_root=$(pwd)
parentDirectory="./docs/"

# Get all subdirectories named 'figures' within the parent directory
figuresDirs=$(find "$parentDirectory" -type d -name "figures")

# Iterate over each 'figures' directory
for dir in $figuresDirs; do
    # Find all Python scripts (.py files) within the current 'figures' directory
    pythonScripts=$(find "$dir" -maxdepth 1 -name "*.py")

    cd "$dir"

    echo "$dir"

    for script in $pythonScripts; do

        # Run each Python script using python command
        echo "Running script: $script"
        python "$script"
        
        # Optionally, check if the Python script ran successfully
        if [[ $? -ne 0 ]]; then
            echo "Failed to run script: $script" >&2
        fi

        # Debug
        echo "$script"
    done

    cd "$repo_root"
    cd ../
done

echo "All scripts executed."

