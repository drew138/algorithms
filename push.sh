#!/bin/sh


git add .
git status -s | sed "s@^[^ ]* @@" | xargs -I file git commit -m "finished file problem."
# git symbolic-ref --short HEAD | xargs git push origin
