#!/bin/sh

set -e

./blockchain_size.py
./blockchain_size_format.py

cp blockchain_size*.txt /var/www/html/bc/
cp index.html /var/www/html/bc/
