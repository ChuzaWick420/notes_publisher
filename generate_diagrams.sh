#!/bin/bash

repo_root=$(pwd)
parentDirectory="docs"

find "$parentDirectory" -type d -name "figures" | while IFS= read -r dir; do

    current_dir=$(pwd)

    cd "$dir"


    ls | while IFS= read -r script; do
        python $script
    done

    cd "$current_dir"

done

cd "$repo_root"

echo "All scripts executed."
