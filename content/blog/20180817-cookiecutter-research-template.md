Title: Facilitate reproducible research with cookiecutter-research-template
Slug: cookiecutter-research-template
Date: 2018-08-27
Tags: Research, Reproducibility, Waf, cookiecutter
Cover: images/fig-dag.png
Summary: This DAG is produced by a sample project for reproducible research
         from <a href="https://github.com/hmgaudecker/econ-project-templates">
         https://github.com/hmgaudecker/econ-project-templates</a>. I extended
         this template with the templating engine ``cookiecutter`` and various
         other software engineering tools.

In one of the university courses I was introduced to a [Waf framework for reproducible
research by Hans-Martin von
Gaudecker](https://github.com/hmgaudecker/econ-project-templates) which is amazingly
useful to manage your research project.

The basic idea is that a project is structured as a DAG, a directed-acyclic graph. A DAG
is a graph with a finite amount of node and edges where the edges have a specific
direction leading from input to output files. Furthermore, starting at node $\nu$ and
following the directed edges, it is not possible to find a way back to $\nu$. Here is
the DAG for the sample project:

<p align="center">
    <b>DAG of sample project</b><br>
    <img src="{static}/images/fig-dag.png">
</p>

As you can see everything starts off at ``get_simulation_draws.py`` which serves as the
source of ``initial_locations.csv`` which is the input of ... You get it.

You get the sample project by installing ``cookiecutter`` first with

```bash
$ pip install -U cookiecutter
```

Then, go to the directory which should contain the folder with the project and type

```bash
$ cookiecutter https://github.com/tobiasraabe/cookiecutter-research-template.git
```

Answer the following prompts so the project will be customized to your needs.

In the end, go into the project folder and set up the ``conda`` environment.

```bash
$ conda env create -n <project-name> -f environment.yml
```

At last, run the following command to make sure that the sample project works.

```bash
$ python waf.py distclean configure build
```

For more information on Waf read [Gaudecker's
documentation](http://hmgaudecker.github.io/econ-project-templates/) and my [Waf Tips &
Tricks](https://github.com/tobiasraabe/cookiecutter-research-template/
blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/WAF.rst).

To use all features of the template check out the
[documentation](https://cookiecutter-research-template.readthedocs.io/
en/latest/index.html).
