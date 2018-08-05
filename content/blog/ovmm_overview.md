Date: 2017-10-22
Slug: ovmm_overview
Title: Beginners Guide to ovmm Part I - Overview
Tags: ovmm, oTree
series: Introduction to oTree Virtual Machine Manager
series_index: 1
status: draft

### Outline

The goal of this article is threefold: first, we will build our own oTree
server in a couple of minutes. Second, we will take a look at the capabilities
of ``ovmm`` as a tool to administrate your online experiment server and, third,
look at the user friendly environment for experimenters provided by ``ovmm``.

The first part is interesting to both, server administrators and researchers
who want to run the server on their own computer. The second part is more
directed at administrators and the third at users.

### Motivation

The need for ``ovmm`` arised when the online experiment server of the
[IAME](https://www.iame.uni-bonn.de/) was used by more researchers and purely
administrative tasks like creating user accounts and backups, deleting
accounts, etc. consumed more time than before. The idea was to create a tool
based on an existing server configuration which performs the repetitive tasks
faster and more reliable. ``ovmm`` was born alongside a pre-configured Ubuntu
image which serves as a template. Later, ``ovmm`` was extended to provide more
user-friendly solutions for beginners with oTree to make the transition from
point-and-click to command line easier.

### Advantages

To explain why ``ovmm`` might be useful for you, we consider two personas, a
researcher who wants to run his onetime experiment and an administrator who
oversees multiple online experiments. These are the advantages:

**User**

- pre-configured virtual machine image (no need to consult documentation on
  server set up)
- ``ovmm`` provides useful and user-friendly commands to manage your experiment

**Administrator**

- pre-configured virtual machine image (no need to consult documentation on
  server set up)
- administrative tasks are reliably done by ``ovmm`` in a split of second

### Comparison to other solutions

**Heroku**

- safe harbor certified? Looks like it is. But expensive.

**Docker**

- even more complicated than everything else

