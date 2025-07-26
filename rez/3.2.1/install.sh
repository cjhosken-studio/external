#!/bin/bash

# Exit on error and undefined variables
set -eu

# Get script directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
VERSION=$(basename "$SCRIPT_DIR")
BUILD_DIR="$SCRIPT_DIR/build"
BASHRC_FILE="$HOME/.bashrc"
REZ_BIN_PATH="/opt/rez/bin"
REZ_COMPLETE_PATH="/opt/rez/completion/complete.sh"

echo "=== Rez Installer ==="
echo "Version: $VERSION"
echo "Build directory: $BUILD_DIR"

# Create build directory
mkdir -p "$BUILD_DIR"
cd "$BUILD_DIR"

# Download the package
echo "Downloading Rez $VERSION..."
if ! wget "https://github.com/AcademySoftwareFoundation/rez/archive/refs/tags/$VERSION.tar.gz"; then
    echo "Error: Failed to download Rez $VERSION" >&2
    exit 1
fi

# Extract the package
echo "Extracting package..."
tar -xzf "$VERSION.tar.gz" || {
    echo "Error: Failed to extract package" >&2
    exit 1
}

# Find the extracted directory
EXTRACTED_DIR=$(find . -maxdepth 1 -type d -name "rez-$VERSION*" | head -n 1)
if [ -z "$EXTRACTED_DIR" ]; then
    echo "Error: Could not find extracted Rez directory" >&2
    exit 1
fi

# Run install script with sudo if needed
echo "Installing Rez..."
if [ -f "$EXTRACTED_DIR/install.py" ]; then
    if [ "$(id -u)" -ne 0 ]; then
        echo "Requesting sudo privileges for installation..."
        sudo python "$EXTRACTED_DIR/install.py"
    else
        python "$EXTRACTED_DIR/install.py"
    fi
else
    echo "Error: install.py not found in $EXTRACTED_DIR" >&2
    exit 1
fi

# Configure .bashrc
echo "Configuring .bashrc..."
if ! grep -q "REZ CONFIGURATION" "$BASHRC_FILE"; then
    cat << EOF >> "$BASHRC_FILE"

# REZ CONFIGURATION
export PATH="\$PATH:$REZ_BIN_PATH"
if [ -f "$REZ_COMPLETE_PATH" ]; then
    source "$REZ_COMPLETE_PATH"
fi
EOF
    echo "Added Rez configuration to $BASHRC_FILE"
else
    echo "Rez configuration already exists in $BASHRC_FILE"
fi

echo ""
echo "SUCCESS! Rez $VERSION has been installed and configured."
echo ""
echo "To start using Rez immediately, run:"
echo "source $BASHRC_FILE"
echo ""
echo "Or open a new terminal session."