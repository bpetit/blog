#!/bin/bash

#set -e

hugo
#echo ".post__content { width: 65%; }" >> docs/css/main.css
#echo ".post__content { width: 65%; }" >> docs/css/main-minimal.css
echo "div .post { width: 65% }" >> docs/css/anatole.css
git add *
git commit -m "New content"
git push -f
