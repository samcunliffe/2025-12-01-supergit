---
marp: true
theme: default
---

![bg fit](assets/ucl-banner.png)

<br/><br/><br/><!-- aesthetic vspace so the title isn't too close to the UCL banner -->

# `git` gives you superpowers

Sam Cunliffe and Matthew Scroggs

Centre for Advanced Research Computing, UCL.

CDT CCMI Software Engineering Fundamentals, 90 High Holborn. 2025-11-24.

---

<!--
paginate: true
footer: `git` superpowers, 2025-11-24.
-->

# Our plan

- A tour of the most useful features.
  - Branching, rebasing.
  - Log, checkout.
  - Revert, soft reset.
  - Collaboration, pull requests, bug reports, ettiquette.
- This is not really an introduction to `git` (sorry!)

---

# Our plan

- A tour of the most useful features.
  - Parallel universe management.
  - Time travelling.
  - Saving cats from a burning building.
  - Superhero teamup.
- This is not really an introduction to `git` (sorry!)

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

- First interesting thing: `git` allows you to time travel.
- You can go back, forwards, to the beginning of a project.
- It's one of those things you learn but you don't appreaciate until you need it.

---

<!--
_footer: Image: [Pro Git](https://git-scm.com/book/en/v2) / Ben Straub and Scott Chacon. CC BY-NC-SA 3.0.
-->

# "Changes" "Staged" "Committed"

<center>

![h:500](https://git-scm.com/book/en/v2/images/areas.png)

</center>

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
