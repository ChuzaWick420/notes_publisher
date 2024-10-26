#!/bin/bash

# Define the parent directory where the search will start
repo_root=$(pwd)

# Debugging runner dir layout
pwd

parentDirectory="$repo_root/notes_publisher/docs/"

# Get all subdirectories named 'figures' within the parent directory, pipe the list into while loop
find "$parentDirectory" -type d -name "figures" | while IFS= read -r dir; do 

# Iterate over each 'figures' directory
    find "$dir" -maxdepth 1 -name "*.py" | python
        # Optionally, check if the Python script ran successfully
        if [[ $? -ne 0 ]]; then
            echo "Failed to run script: $script" >&2
        fi

        # Debug
        echo "$script"
    done

    cd "$repo_root"
    cd ../

echo "All scripts executed."

