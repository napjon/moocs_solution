#! /bin/bash

cat aadhaar_data.csv | python aadhaar_generated_mapper.py | sort | python aadhaar_generated_reducer.py
