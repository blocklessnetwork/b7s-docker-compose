#!/bin/bash

# Platform and Architecture
PLATFORM=${PLATFORM:-linux}  # default to 'linux' if not set
ARCH=${ARCH:-amd64}          # default to 'amd64' if not set

# URL of the tar.gz file
url="https://github.com/blocklessnetwork/b7s/releases/download/v0.0.23.1/b7s-$PLATFORM.$ARCH.tar.gz"

# Directory to extract the contents
extract_dir="b7s"

# Directory for identities
identities_dir="keys"

# Number of heads and workers to create (read from environment variables)
num_heads=${NUM_HEADS:-5}
num_workers=${NUM_WORKERS:-10}

# Create the directory if it doesn't exist
mkdir -p "$extract_dir"

# Download the tar.gz file
wget "$url" -O "$extract_dir/b7s-$PLATFORM.$ARCH.tar.gz"

# Extract the contents
tar -xzvf "$extract_dir/b7s-$PLATFORM.$ARCH.tar.gz" -C "$extract_dir"

echo "Downloaded and extracted b7s to $extract_dir."

chmod +x "$extract_dir/b7s-keygen"
mkdir -p "$identities_dir"
cd "$identities_dir"

# Create directories for heads
for ((i = 1; i <= num_heads; i++)); do
    head_dir="head$i"
    mkdir -p "$head_dir"
    cd "$head_dir"
    ../../b7s/b7s-keygen
    cd ..
done

# Create directories for workers
for ((i = 1; i <= num_workers; i++)); do
    worker_dir="worker$i"
    mkdir -p "$worker_dir"
    cd "$worker_dir"
    ../../b7s/b7s-keygen
    cd ..
done
