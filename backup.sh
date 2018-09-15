#!/bin/bash


git add --all
read -p 'Enter comment for git commit: ' comment
git commit -m "$comment"
git push origin master