[![Updates](https://pyup.io/repos/github/tobiasraabe/tobiasraabe.github.io/shield.svg)](https://pyup.io/repos/github/tobiasraabe/tobiasraabe.github.io/)

---

# Develop the website

The easiest way is to open a bash terminal and hit

        $ pelican -lrD

Currently, this option is not working under Windows
([#2400](https://github.com/getpelican/pelican/issues/2400)), but you can use WLS
instead.

# Publish the website

To publish the site, run

    $ make github

and the content of the output folder will be moved to the master branch.
