[![Updates](https://pyup.io/repos/github/tobiasraabe/tobiasraabe.github.io/shield.svg)](https://pyup.io/repos/github/tobiasraabe/tobiasraabe.github.io/)

---

# Develope the website

There are two possibilities to run a development server.

1. The easiest way is to open a bash terminal and hit

        $ make devserver

2. Another way to debug your script is to run

        $ python -m pelican.server

   to view the published website on http://localhost:8000. Make sure to use
   your browser in private mode.

   The second terminal runs

        $ pelican -r

   or

        $ make DEBUG=1 html

   if you want to see the full traceback of your error.


# Publish the website

To publish the site, run

    $ make github

and the content of the output folder will be moved to the master branch.
