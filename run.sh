#!/usr/bin/bash
if [ -d venv ]
  then
    source ./venv/bin/activate
    python -B ./hello3.py
fi