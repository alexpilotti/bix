#!/bin/bash

base_dir=$(dirname $(readlink -f "$0"))
python3 $base_dir/cli.py "$@"
