Title: What I have been doing
Date: 2020-09-30
Tags: Software Engineering
Author: Tobias Raabe

Hi everybody,

I have not written a post in a long time and so I resuming this blog by keeping you
posted on some of the projects I have been working on.

In general, I have been developing or contributing to several research applications in
the last year. I learned a lot about software engineering and designing applications.
Maybe I find the time to make a post on some of the things I learned along the way.

<!-- PELICAN_END_SUMMARY -->

### pytask

The project I am most excited about right now is
[pytask](https://github.com/pytask-dev/pytask), a build system designed for researchers
to run their project pipeline from data preparation over analyses to
compiling the reports.

I was extremely frustrated with existing solutions and programmed my own build system.
One of the highlights is the interface which is pretty similar to pytest to lower the
entry-barrier. It also burrows the plugin system from pytest which is based on
[pluggy](https://github.com/pytest-dev/pluggy).

If you already know my [cookiecutter for reproducible
research](https://github.com/tobiasraabe/cookiecutter-research-template), you know Waf.
pytask replaces Waf. I will probably not update the cookiecutter for the foreseeable
future and, instead, I recommend [Hans-Martin's cookiecutter](
https://github.com/hmgaudecker/econ-project-templates) which will support pytask.

Please take a look at pytask and try it out in your next project. I appreciate any
feedback, comments, feature requests and also harsh criticism :). Write me an email or
file an issue to get in touch.

I already held a presentation about pytask's design which I will probably post here in
some weeks. Half the time is about plugin architectures in general and pluggy and the
other half is about pytask.


### respy

Together with [Janos](https://github.com/janosg) I created a framework for a certain
class of econometric models, called
[respy](https://github.com/OpenSourceEconomics/respy).

For the insiders, it is a framework for finite-horizon discrete choice dynamic
programming models also called Eckstein-Keane-Wolpin models which are used to study the
human capital accumulation process of individuals in the labor market.

The documentation is quite extensive for such a young project and is currently extended
by other contributors which take over the project.

If you are an economist and interested in structural modeling, it might be a good place
to start. Even if you do not want to use this model, you might be able to get some
inspiration for your own model.

I learned a lot about how to build interfaces people actually are able to use and how to
write performant code by choosing the right design and Numba where necessary.


### gettsim

I redesigned the computational backend of
[gettsim](https://github.com/iza-institute-of-labor-economics/gettsim) with
[Janos](https://github.com/janosg) and [Hans-Martin](https://github.com/hmgaudecker).
gettsim offers a representation of the German tax and transfer system and allows
researchers to study the impact of reforms on the amount of taxes and benefits people
face.

The task was to design an interface which allows users to modify or extend the
pre-implemented tax and transfer system.

Our solution is a mixture inspired by pytest's fixtures and a DAG (directed acyclic
graph).

The general idea is that the whole tax and transfer system is a function which receives
data on individuals and returns relevant quantities like child benefits or the amount of
taxes on capital gains.

We can divide the function into smaller functions which compute quantities in the tax
and transfer system we are not ultimately interested in, but whose result can be shared
to compute following, relevant quantities.

Now, we divided the tax and transfer system into a collection of smaller functions which
need to tell us how they related to each other, meaning that the result of one function
needs to be passed to another function as an argument.

Here, we use the idea of pytest's fixtures where using a fixture's name as an argument
in a test function gives you access to the return of the fixture inside the test
function. Similarly, a function in gettsim looks like this

```python
def child_benefits(n_children, parameters):
    return n_children * parameters["child_benefits"]
```

where ``n_children`` is either a variable in the input data or a function with the same
name which computes the quantity.

From a function's name and the its argument names, we can build a DAG which allows us to
determine the correct order in which functions should be evaluated.

Now, a user can modify the collection of function by overwriting existing functions or
adding her own which will create a new DAG.

If this sketch of the core idea was too rough, take a look at the documentation and
maybe the [visualiuzation of such a
DAG](https://gettsim.readthedocs.io/en/latest/tutorials/visualizing_the_system.html).


### sid

Last but not least, I have been working on an epidemiological model to predict the
spread of infectious diseases. This is my COVID-19 project with
[Klara](https://github.com/roecla) and [Janos](https://github.com/janosg). It is called
[sid](https://github.com/covid-19-impact-lab/sid) and we hope to get something out soon.
