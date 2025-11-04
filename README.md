# `git` gives you superpowers

(+ licensing your software)

Slides and material for a lesson on Advanced Git, GitHub, and licensing given to the 2025 cohort in the UCL/Imperial [CCMI CDT](https://ccmi-cdt.org/).

[@mscroggs](https://github.com/mscroggs) and [@samcunliffe](https://github.com/samcunlffe)

## Prerequisites

### `git`

We assume all students have installed `git` version 2 or newer, and have run the following commands once or twice before in their lives:

```
git config
git add
git commit
```

If not, please [install `git`] then spend a bit of time search around for what these commands do.

### GitHub

We also assume all students have a [GitHub account] and have browsed around a repository on GitHub before (like this one!)

> [!TIP]
> If you're creating an account for the first time, we recommend adding your university emai _and_ a personal one. You'll want your GitHub account to outlive your PhD.

**Optionally**, you can [install the GitHub CLI] you might find it easier to authenticate, and it's pretty useful to have it around when working with GitHub.

Finally, if you've not already done so, configure `git` so it:

1. knows your [name (or username)](https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git#about-git-usernames);
2. knows your [email address](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address); and
3. is [authenticated to push to GitHub](https://docs.github.com/en/get-started/git-basics/set-up-git#authenticating-with-github-from-git).

> [!TIP]
> You can use your real name and email address for 1 and 2, or you can use your GitHub username and [anonymised GitHub "noreply" email](https://docs.github.com/en/account-and-profile/reference/email-addresses-reference#your-noreply-email-address) if you're concerned about privacy.

For thing number 3 you can either use HTTPS (which GitHub recommend) or SSH.
During your PhD you'll probably encounter SSH so there's no harm in doing it that way:

- [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

<details><summary><h3>Example commands</h3></summary>

If you've never done these setup steps before your terminal history should look something like:

```sh
git config --global user.name "Joe Bloggs"
git config --global user.email "jbexample@users.noreply.github.com"

ls ~/.ssh  # check for existing keys and ssh config, then...
ssh-keygen -t ed25519 -C "jbloggs@ucl.ac.uk"
touch ~/.ssh/config
echo """Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519""" > ~/.ssh/config
pbcopy < ~/.ssh/id_ed25519.pub  # copy your public key to the clipboard
```

And then you should have pasted the key into your GitHub account (Settings . SSH and GPG keys . Add new ...).

</details>

### Pre-lesson check

To check you've done all of the technical prerequisite steps please run:

```sh
git --version  # should show version 2.something
git config --global --list # should at least show user.name and user.email
ssh -T git@github.com  # should say "Hi <your GitHub user>! You've successfully authenticated..."
```

[Pro Git]: https://git-scm.com/book/en/v2
[install `git`]: https://git-scm.com/install/
[GitHub account]: https://github.com/signup
[install the GitHub CLI]: https://github.com/cli/cli#installation
[GitHub CLI]: https://github.com/cli/cli#installation

## Reuse

These slides borrow some diagrams and some structure from [Pro Git](https://git-scm.com/book/en/v2).

If any of this is useful to you for teaching or learning or anything else, please feel encouraged to use it!
The material in these slides is licensed under [CC-by-nc-sa 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png" height="31" />

The UCL and CCMI-CDT logos are trademarks and have different [reuse guidelines](https://www.ucl.ac.uk/brand/brand-essentials/ucl-logo).

But we assume you will rebrand for your own organisation and purposes.
