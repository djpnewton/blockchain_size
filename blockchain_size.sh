#!/bin/sh

set -e

cd "$(dirname "$0")"

./blockchain_size.py log
./blockchain_size_format.py

cp blockchain_size*.txt /var/www/html/bc/
cp index.html /var/www/html/bc/

./upload.sh
