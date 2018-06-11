
# Develope the website

If you want to write content with Jupyter notebooks, run

    start fab serve

to start a Jupyter server and the Hugo server in the background.


# Publish the website

If you made changes to the website, commit everything. Then, run

    fab render_notebooks

so the Markdown representation of the notebooks is refreshed. Then, commit
all changes to the repo. After that, run

    fab publish

to make the latest changes available online.
