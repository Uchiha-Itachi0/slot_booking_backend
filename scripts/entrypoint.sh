#!/usr/bin/env bash

set -e

RUN_PYTHON_MANGE_PY="poetry run python -m slot_booking_backend.manage"

echo 'Collecting Static files....'
$RUN_PYTHON_MANGE_PY collectstatic --no-input

echo 'Running migrations.....'
$RUN_PYTHON_MANGE_PY migrate --no-input

$RUN_PYTHON_MANGE_PY runserver 0.0.0.0:8000
