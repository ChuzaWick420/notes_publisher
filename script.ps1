# Define the parent directory where the search will start
$parentDirectory = "~/"

# Get all subdirectories named 'figures' within the parent directory
$figuresDirs = Get-ChildItem -Path $parentDirectory -Recurse -Directory | Where-Object { $_.Name -eq 'figures' }

# Iterate over each 'figures' directory
foreach ($dir in $figuresDirs) {
    # Find all Python scripts (.py files) within the current 'figures' directory
    $pythonScripts = Get-ChildItem -Path $dir.FullName -Filter *.py
    
    cd $dir

    foreach ($script in $pythonScripts) {

        # Run each Python script using python command
        Write-Host "Running script: $($script.FullName)"
        python $script.FullName
        
        # Optionally, check if the Python script ran successfully
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Failed to run script: $($script.FullName)" -ForegroundColor Red
        }
    }

    cd $parentDirectory
    cd ../
}

Write-Host "All scripts executed."

