## Building

## Building example

Point CMake to your install of catalyst:
```
$ cmake -G Ninja \
    -DUSE_MPI=ON \    
    -Dcatalyst_DIR=/path/to/catalyst/install/lib/cmake/catalyst-2.0/ \
    ../src
$ cmake --build .
```

Optionally choose the MPI version to use (see `MPI_C_COMPILER` and `MPI_CXX_COMPILER`).

## Running examples

The catalyst implementation used at build time is also used by default
at runtime.

```
$ ./simulator ../src/catalyst_pipeline.py
```

To specify another implementation, use the appropriate environment variables
```
export CATALYST_IMPLEMENTATION_PATHS=/path/to/paraview_513/lib/catalyst:
export CATALYST_IMPLEMENTATION_NAME=paraview
```

To get information about which implementation was actually found, try:
```
export CATALYST_DEBUG=1
```
