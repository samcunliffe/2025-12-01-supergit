---
marp: true
theme: default
---

![bg fit](assets/ucl-banner.png)

<br/><br/><br/><br/><!-- aesthetic vspace so the title isn't too close to the UCL banner -->

# `git` gives you superpowers

## (+ licensing your software)

[@samcunliffe] and [@mscroggs]

CDT CCMI Software Engineering Fundamentals, 90 High Holborn. 2025-12-01.

![h:31](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-nc-sa.png)

[@mscroggs]: https://github.com/mscroggs
[@samcunliffe]: https://github.com/samcunlffe

---

<!--
paginate: true
footer: `git` superpowers and licensing, 2025-12-01.
-->

# Our plan

<!-- prettier-ignore-start -->

* A tour of the most useful features.
  * Log, checkout.
  * Branching, rebasing.
  * Revert, soft reset.
  * Collaboration, pull requests, bug reports, ettiquette.
* This is not really an introduction to `git` (sorry!)

<!-- prettier-ignore-end -->

---

# Our plan

- A tour of the most useful features.
  - Time travelling.
  - Parallel universe management.
  - Saving cats from a burning building.
  - Superhero teamup.
- This is not really an introduction to `git` (sorry!)

---

# Time travelling

---

<!--
_footer: Image: [Faces Of Open Source](https://www.facesofopensource.com) / Peter Adams. CC BY-NC-SA 4.0.
-->

![bg left:40%](assets/linus.jpg)

<!-- prettier-ignore-start -->

* This is Linus.
* He started the Linux kernel project.
* He started the `git` project.
* ...because he needed something for collaborating on the kernel.
* The software project `git` was kept in `git` from quite early on.
* _Remember the human_ on the internet.

<!-- prettier-ignore-end -->

---

# Demo: let's look at `git`'s history in `git`.

---

<center>

![h:600](assets/git-in-git.png)

</center>

---

# Parallel universes

---

# Saving cats from burning buildings

---

# Superhero teamup

---

<!--
_footer: Image: [Pro Git](https://git-scm.com/book/en/v2) / Ben Straub and Scott Chacon. CC BY-NC-SA 3.0.
-->

# "Changes" "Staged" "Committed"

<center>

![h:500](https://git-scm.com/book/en/v2/images/areas.png)

</center>

---

---

<!--
_footer: Image: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:DC_superhero_emojis.svg) / Di. CC BY-SA 4.0.
-->

![](assets/superheroes.png)

---

# Split bullet slide

- (Obviously)

<br/>
<div class="ccolumns">
<div>

- Bullet to the left

</div>
<div>

- Bullet to the right

</div>

---

# Code

```py

def i_prefer_python() -> None
    print("Obviously, I use type hints")
    return

```

```c++

int butWillWriteCppIfNeeded()
{
  return 1337;
}

```

---

# Emoji are cool

- ❤️🎉✅

---

# Maths

- An example of inline maths $e^{i\pi} = -1$
- An example of display format maths:

$$
\widehat{f}(\xi) = \int_{-\infty}^{\infty} f(x)\ e^{-i 2\pi \xi x}\,dx.
$$

---

# Conclusions

- One or two clear take-home points.
- Don't overload your audience.

---

# Appendix

---

# Further reading

|                                                      |             |
| ---------------------------------------------------- | ----------- |
| [Pro Git](https://git-scm.com/book/en/v2)            | Online book |
| GitHub's [Git Guides](https://github.com/git-guides) | Website     |
