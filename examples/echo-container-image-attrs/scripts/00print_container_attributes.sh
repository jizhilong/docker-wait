#!/usr/bin/env bash

echo "hostname: $CONTAINER_HOSTNAME"
echo "container labels:"

while IFS='=' read -r name value ; do
  if [[ $name == 'CONTAINER_LABEL_'* ]]; then
	echo "$name=$value"
  fi
done < <(env)
