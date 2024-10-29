#!/bin/bash

repo_root=$(pwd)

# directory to search for
parentDirectory="docs"

# Find full path for figures
find "$parentDirectory" -type d -name "Figures" | while IFS= read -r dir; do

    # Track where we are currently as a snapshot for reference
    current_dir=$(pwd)

    # change into the directory for Figures
    cd "$dir"


    # Run each python script
    ls | while IFS= read -r script; do
        python $script
    done

    # reset back to the snapshot
    cd "$current_dir"

done

echo "All scripts executed."
