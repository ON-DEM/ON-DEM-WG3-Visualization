# Preconditions:
# - Docker is installed
# - The folder "Exercises" from Kitware training session is in current path, as well as this script

# The commented part below must be executed on the host, the rest is to be executed inside the running container

# Create Docker container with GPU and X11 access for graphics
# docker create -it --device /dev/dri:/dev/dri -v "$PWD":/home/user -w /home/user -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --name ubuntu24 registry.gitlab.com/yade-dev/docker-yade:ubuntu24.04
# Start the container interactively
# docker start -ai ubuntu24

# Clone Catalyst v2.0.0 source code
git clone --branch v2.0.0 https://gitlab.kitware.com/paraview/catalyst.git
# Download ParaView Catalyst binary with MPI and Python support
wget https://www.paraview.org/files/v5.13/ParaView-5.13.3-MPI-Linux-Python3.10-x86_64.tar.gz
# Extract the ParaView archive
tar -xzf ParaView-5.13.3-MPI-Linux-Python3.10-x86_64.tar.gz

# Build Catalyst
cd catalyst/
mkdir build
cd build
cmake ../
make install
cd ../..

# Copy example simulator
cp -r Exercises/Catalyst/Simulator/ Simulator
cd Simulator/
# Clean previous builds
rm -rf build
mkdir build
cd build
# Configure with Catalyst 2 path
cmake -Dcatalyst_DIR=/usr/local/lib/cmake/catalyst-2.0/ ../src
# Build the simulator
make
# First run without env vars
./simulator ../src/catalyst_pipeline.py
# Set Catalyst runtime environment
export CATALYST_IMPLEMENTATION_PATHS=../../ParaView-5.13.3-MPI-Linux-Python3.10-x86_64/lib/catalyst/
export CATALYST_IMPLEMENTATION_NAME=paraview
# Run again with Catalyst activated
./simulator ../src/catalyst_pipeline.py

# After second execution some *.png should be in Simulator/build/png
