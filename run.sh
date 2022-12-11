#!/usr/bin/bash
if [ -d venv ]
  then
    source ./venv/bin/activate
    python -B ./hello2.py &
fi