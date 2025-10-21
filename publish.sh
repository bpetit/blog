#!/bin/bash

#set -e

hugo
git add *
git commit -m "New content"
git push -f
