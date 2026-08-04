#!/bin/bash

#set -e

hugo
echo ".post__content { width: 65%; }" >> docs/css/main.css
git add *
git commit -m "New content"
git push -f
