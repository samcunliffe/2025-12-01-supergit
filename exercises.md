# Exercise 1: branches and merge conflicts

1. Read the content of the script below
1. Run it one by one or as a script on your machine. It will create a merge conflict.
1. Resolve the merge conflict so the text in `README.md` is "Hello World".

```bash
cd ~/Desktop/
mkdir merge-conflict-exercise
cd merge-conflict-exercise/
git init
touch README.md
echo "Hello" > README.md
git add README.md
git commit -m "first commit on main"
# if your default is not main; rename master with: git branch -m main
git switch -c new-branch
echo "Hello World" > README.md
git commit -am "first commit on new-branch"
git switch main
echo "Hola Mundo" > README.md
git commit -am "second commit on main: translates it into Spanish"
git merge new-branch
# now fix!
```

<!-- Adapted from UCL-COMP0233 Exercises. David Perez Suarez. CC-BY 4.0. -->

# Exercise 2: rebasing

1. Read the script below
1. Run the commands one by one or as a script.
1. Rebase the `haiku` branch so that there is one commit in the history that adds the haiku.

```bash
cd ~/Desktop/
git clone git@github.com:bast/git-rebase-squash-exercise.git
# --or-- gh repo clone bast/git-rebase-squash-exercise
# --or-- git clone https://github.com/bast/git-rebase-squash-exercise.git
cd git-rebase-squash-exercise/
git switch haiku
python main.py
git log --oneline
git rebase --interactive HEAD~6
# now edit!
```

## Extra credit

What does `HEAD~6` mean?
Have you seen this before?

<!-- Adapted from CodeRefinery Exercise. Radovan Bast. CC-BY 4.0. -->
