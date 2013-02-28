===================
git-clone-canonical
===================

git extension that lets you easily fetch the source code for popular
open-source projects.

Installation
============

::

    pip install git-clone-canonical
      - install binary
      - clone repo to /usr/local/git-clone-canonical
      - add any tab-completion hook


Usage
=====

::

    clone: git clone-canonical sqlalchemy
    update: git clone-canonical --update
    search: git clone-canonical --search sql


Search
======

You can search based on name or keyword.

For example, to find a repo with sqlalchemy in the name you would type::

    git clone-canonical --search sqlalchemy

Or to find all repos related to openstack::

    git clone-canonical --search openstack
