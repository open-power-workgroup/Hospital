#!/usr/bin/env bash

# run this script AFTER "python generate.py [data version]"
git checkout gh-pages && \
rm -rf data/* && \
mv output/* data/ && \
git add . && \
git commit -am "update published website and json api" && \
git pull --rebase && \
git push && \
git checkout master

