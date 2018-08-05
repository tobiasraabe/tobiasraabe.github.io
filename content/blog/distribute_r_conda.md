Date: 2018-03-21
Title: How to compile and distribute an R package with conda
Tags: Conda, Anaconda, R, conda-build, MRO

TL;DR: This article shows how to compile and distribute R packages on
anaconda.org to be used in your data science projects.

### Introduction to Anaconda and R

I like to manage my research projects with [conda][6] which is the package
manager for [Anaconda][7], a popular Python distribution for data science. For
one of my recent projects I also needed to install R and I was lucky to find
out that R is also available with ``conda``.

First, you create your normal Python environment for your new project

```bash
$ conda create --name project python=3.6 anaconda
```

This installs a complete Anaconda distribution with Python 3.6 under the name
``project``. If you only want the bare Python interpreter, call

```bash
$ conda create -n project python=3.6
```

Activate the environment with

```bash
$ activate project
```

> Hint: Since my os is running on Windows, I prefer to use Powershell.
  Unfortunately, activating and deactivating your environment usually fails.
  Try out [pscondaenvs][2] which installs corrected Powershell scripts.

If we also need an R distribution for our project, we have to make the decision
between to [R](https://www.r-project.org/) from R-Project and
[MRO](https://mran.microsoft.com/open) from Microsoft. The latter is the
default with Anaconda, but the former is still provided if you are running a
32-bit operating system or an older macOS version. The advantage of MRO is that
it is using the Intel Math Kernel Library (MKL) and enables multithreading by
default ([here](https://mran.microsoft.com/documents/rro/multithread) are some
benchmark reports and information on how to set the number of threads used).

Installing a basic R interpreter from MRO is as simle as typing

```bash
$ conda install --channel r mro-base
```

If you want to install R from R-Project, type ``conda install -c r r-base``.

It is important to note that it is impossible to have both R interpreters in
one environment and that packages for either one of them do not work with the
other. You can find more information [here][4].

There is also the option to install a whole R distribution which is called
``r-essentials``. It bundles many useful packages along with [``IRkernel``][8]
which enables you to use R in Jupyter notebooks. Again, there are two commands
depending on which R interpreter you are using.

```bash
$ conda install -c r r-essentials
$ conda install -c r r-essentials r-base
```

To update all of your R packages run

```bash
$ conda update r-essentials
```

If your desired package is not available in ``r-essentials``, you can use the
search on anaconda.org to find a channel which offers your package. But what if
your package is not available?

### Building and Distributing an R package

I had the same issue when I wanted to use [``mice``][3] which is a known
framework for multiple imputation by chained equations.

To build the package for your conda distribution, invoke the following command

```bash
$ conda skeleton cran r-mice
```

This will create a folder called ``r-mice`` which contains three files,
``bld.bat``, ``build.sh`` and ``meta.yml``. ``meta.yml`` is the important file
which controls the compilation. An example can be found [here][1]. Note the key
called ``requirements``. inside ``host`` and ``run`` the R interpreter is
defined. By default it is ``r-base``. If you are using MRO, you have to change
this to ``mro-base``.

```yaml
requirements:
  build:
    - {{ compiler('c') }}          # [not win]
    - {{ compiler('cxx') }}        # [not win]
    - {{native}}toolchain          # [win]
    - {{posix}}filesystem          # [win]
    - {{posix}}make

  host:
    - r-base
    - r-mass
    - r-rcpp
    - r-lattice
    - r-nnet
    - r-rpart
    - r-survival

  run:
    - r-base
    - {{native}}gcc-libs           # [win]
    - r-mass
    - r-rcpp
    - r-lattice
    - r-nnet
    - r-rpart
    - r-survival
```

In the next step, we want to compile the package. If you are on Windows, make
sure to install [RTools][9] in advance and add binaries to your system's path
during the installation. To compile the package, type

```bash
$ conda build r-mice
```

After the compilation ended successfully, you can install the package with

```bash
$ conda install --use-local r-mice
```

You can also [upload the package to Anaconda.org][10] to your private
repository and make it accessible to all people.

That's what I did. I have created a [repository][11] which builds the package
for Linux and macOS with [Travis-CI][12] and Windows with [Appveyor][13]. The
compiled packages are uploaded to my account and can be install via

```bash
$ conda install -c brimborium r-mice
```

### Compile your own package

If you want to use my solution for yourself, fork my repository. Then, replace
the recipe in conda-recipe with your recipe create with

```bash
$ conda skeleton cran <package name>
```

Push the repository to your Github account and create accounts on [Travis-
CI][12], [Appveyor][13] and [Anaconda.org](https://anaconda.org/).

Next, go to Anaconda.org, settings, access and create a token. Make sure to
check allow read and write API access. The rest is optional.

Set the resulting token as a secret environment variable to your projects on
Travis-CI and Appveyor. Make sure to name it ``CONDA_UPLOAD_TOKEN`` as the
scripts look for a variable called like this.

I know this was a fair amount of information and if you are not familiar with
automation tools like Travis-CI and Appveyor, this looks even more deterrent.
But that is why I created my repository which is reduced to the minimal amount
of code to do the task.

I will also extend this post and the repository description in the future.
Since I do only have rudimentary knowledge of the background of what I did,
there is a lot of room to grow :).

**References**

- [Anaconda: Download and more][7]
- [Using R language with Anaconda][5]
- [PSCondaEnvs: Fix activate/deactivate on Windows with Powershell][2]
- [mice by Stef van Buuren][3]
- [conda: documentation][6]
- [IRkernel: Use R with Jupyter notebooks][8]
- [RTools: Download][9]

[1]: https://github.com/tobiasraabe/r-mice/blob/master/conda-recipe/meta.yaml
[2]: https://github.com/BCSharp/PSCondaEnvs
[3]: https://github.com/stefvanbuuren/mice
[4]: https://github.com/conda-forge/r-base-feedstock/issues/34
[5]: https://docs.anaconda.com/anaconda/user-guide/tasks/use-r-language
[6]: https://conda.io/docs/
[7]: https://www.anaconda.com/distribution/
[8]: https://github.com/IRkernel/IRkernel
[9]: https://cran.r-project.org/bin/windows/Rtools/
[10]: https://www.anaconda.com/blog/developer-blog/conda-data-science/
[11]: https://github.com/tobiasraabe/r-mice
[12]: https://www.travis-ci.org/
[13]: https://www.appveyor.com/
