# Github 
## Password
```
git config --global credential.helper store
```
## Submodules
```
git submodule add https://github.com/chaconinc/DbConnector
```
## Reset
```
# Revert all changes on file
git checkout .

# reset changes added
git reset
```
## General
```
git pull

git source url
git status

git diff
git reset

git add
git commit
git push
git LFS
```
## Get original url
```
git config --get remote.origin.url
```
## Add Existing Dir as Repo
* Type git init.
* Type git add to add all of the relevant files.
* You’ll probably want to create a .gitignore file right away, to indicate all of the files you don’t want to track. Use git add .gitignore, too.
* Type git commit

* git remote add origin https://github.com/ychnh/repo_name
* git push -u origin master

