# Develope the website

You need to powershell terminals. The first terminal runs

    $ python -m pelican.server

and you can view the published website on http://localhost:8000. Make sure to
use your browser in private mode.

The second terminal runs

    $ pelican -r

or

    $ make DEBUG=1 html

if you want to see the full traceback of your error.


# Publish the website

To publish the site, run

    $ make github

and the content of the output folder will be moved to the master branch.
