#!/bin/bash

# Function to display menu of subdirectories
display_menu() {
    clear
    echo "=== Menu ==="
    local index=0
    for subdir in "${subdirs[@]}"; do
        # Extract the base name of the directory
        subdir_name=$(basename "$subdir")
        echo "$((index + 1)). $subdir_name"
        ((index++))
    done
    echo "0. Exit"
    echo "============"
}

# Main script
echo "Starting main script..."

# Define the directory containing subdirectories
BASE_DIR="./cmd"

# Check if the base directory exists
if [ ! -d "$BASE_DIR" ]; then
    echo "Base directory not found!"
    exit 1
fi

# Find all subdirectories
subdirs=($(find "$BASE_DIR" -mindepth 1 -maxdepth 1 -type d))

while true; do
    # Display the menu of subdirectories
    display_menu
    read -rp "Enter your choice: " choice

    # Validate the user's choice
    if [ "$choice" -ge 1 ] && [ "$choice" -le "${#subdirs[@]}" ]; then
        selected_subdir="${subdirs[$((choice - 1))]}"
        # Extract the base name of the selected subdirectory
        selected_subdir_name=$(basename "$selected_subdir")
        echo "Selected directory: $selected_subdir_name"
        #

        main_file="$selected_subdir/__init__.py"
        echo "$main_file"
        if [ -f "$main_file" ]; then
            echo "Executing main.py in $selected_subdir_name"
            echo poetry run python "$selected_subdir"
            poetry install "$main_file"
            poetry run python "$main_file"
        else
            echo "main.py not found in $selected_subdir_name"
        fi
        read -rp "Press Enter to continue..."
    elif [ "$choice" -eq 0 ]; then
        echo "Exiting..."
        exit 0
    else
        echo "Invalid choice!"
        read -rp "Press Enter to continue..."
    fi
done
