# Github 
* https://danielmiessler.com/study/git/
* git diff -- . ':(exclude)*.ipynb'

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
To remove files from stage use reset HEAD where HEAD is the last commit of the current branch. This will unstage the file but maintain the modifications.
git reset HEAD <file>

To revert the file back to the state it was in before the changes we can use:
git checkout -- <file>


To remove a file from disk and repo use git rm and to remove a directory use the -r flag:
git rm '*.txt'
git rm -r <dirname>
If we want to remove a file from the repository but keep it on disk, say we forgot to add it to our .gitignore file then use --cache:
git rm <filename> --cache
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

# Quick guide on branching #################
https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
############################################
git branch hotfix
git checkout hotfix
git commit -a -m 'Fix broken email address'
git checkout master
git merge hotfix
git branch -d hotfix
```
## UNDO REVERT
* https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit
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

