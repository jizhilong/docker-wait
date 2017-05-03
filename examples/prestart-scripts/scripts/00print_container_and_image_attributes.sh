#!/usr/bin/env bash

echo "hostname: $CONTAINER_HOSTNAME"
echo "image: $IMAGE_NAME"
echo "image author: $IMAGE_AUTHOR"

echo "container labels:"

while IFS='=' read -r name value ; do
  if [[ $name == 'CONTAINER_LABEL_'* ]]; then
	echo "$name=$value"
  fi
done < <(env)
