#!/bin/bash

# This runs all synth products.
# Run a single script with yosys -s <script_file>

find ./*.yosys -maxdepth 1 -type f -exec yosys -s {} \;
