#!/bin/bash
set -e

host="$1"
shift
cmd="$@"

until nc -z -v -w30 "$host" 3306; do
  echo "Waiting for MySQL..."
  sleep 2
done

exec $cmd
