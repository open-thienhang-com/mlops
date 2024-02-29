# Description: Hướng dẫn sử dụng 
# Author: thienhang.com
# Date: Feb 1, 2024

echo "test"

#!/bin/bash

# Check if README.md exists
if [ -f "README.md" ]; then
    # Print the contents of README.md
    cat README.md
else
    echo "README.md not found."
fi
