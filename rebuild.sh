#!/bin/bash

PYTHON='python manage.py'

MARC_FILE=$1
ABBYY_DIRS=$2

echo "Clearing database..."
$PYTHON flush

echo "Ingesting data..."
$PYTHON ingest_marc $1
cat $ABBYY_DIRS |
while read ABBYY_XML
do
    ID=${ABBYY_XML#*_}
    ID=${ID%%_*}
    $PYTHON ingest_abbyyxml $ID "$ABBYY_XML"
done

echo "Deriving wellcome player data..."
$PYTHON init_search
$PYTHON init_autocomp

echo "Building search indexes"
$PYTHON rebuild_index
