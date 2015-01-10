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
    ID=${ABBYY_XML##*KF_}
    VOL=""
    if [[ $ID =~ ^([0-9]{6})_[0-9]{4}(_([0-9]{2}))? ]]
    then
	    ID=${BASH_REMATCH[1]}
	    VOL=${BASH_REMATCH[3]}
    else
	    echo "Could not extract ID/VOL from $SRC"
        continue
    fi
    if [ -z $VOL ]
    then
        VOL=01
    fi
    $PYTHON ingest_abbyyxml $ID $VOL "$ABBYY_XML"
done

echo "Deriving wellcome player data..."
$PYTHON init_search
$PYTHON init_autocomp

echo "Building search indexes"
$PYTHON rebuild_index
