# Github 
## Password
```
git config --global credential.helper store
git pull

git submodule add https://github.com/chaconinc/DbConnector

git source url
git pull (local branch up to date with remote)
git status

git diff
git reset

git add
git commit
git push
git LFS
```
## Get url
```
git config --get remote.origin.url
```
## Add New
* Type git init.
* Type git add to add all of the relevant files.
* You’ll probably want to create a .gitignore file right away, to indicate all of the files you don’t want to track. Use git add .gitignore, too.
* Type git commit

* git remote add origin https://github.com/ychnh/repo_name
* git push -u origin master

# Reset all changes
git checkout .
## reset changes added
git reset
