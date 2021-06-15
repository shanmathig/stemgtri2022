# STEM@GTRI 2021

## Example Circuits

Example circuits and commands to compile them to netlists are located in the
`example_circuits` file. These can all be compiled by running `./build.sh`
or `yosys -s <script_file>` for individual scripts. You can compile a new
circuit by copying an existing .yosys script file and changing the
input/output files and top module.

It is suggest you ssh into `tmpo-wms-d01.ctisl.gtri.org` where yosys and
other SymbiFlow utilities are already installed.

## Server

The Server directory contains the back-end (server) and also the front end (HTML). There is a README in the directory.