#!/usr/bin/env bash
set -ex

cd examples

for subdir in `ls`; do
  cd $subdir
  timeout 60s docker-compose up --build --force-recreate --abort-on-container-exit
  cd ..
done
