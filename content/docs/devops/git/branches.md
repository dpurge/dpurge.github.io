# Branches

```sh
git remote rm origin
git remote add origin https://xxxx/xxxx
git push origin --all
```

New branch:

```sh
git checkout -b <branch>
git push -u origin <branch>
```

Merge:

```sh
git checkout master
git merge hotfix
```

List tags:

```sh
git fetch --tags
git push --tags
```
