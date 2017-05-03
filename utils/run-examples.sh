#!/usr/bin/env bash
set -ex

docker run --rm -v /:/hostroot jizhilong/docker-wait install_dwait

cd examples

for subdir in `ls`; do
  cd $subdir
  timeout 60s docker-compose up --build --force-recreate --abort-on-container-exit
  cd ..
done
