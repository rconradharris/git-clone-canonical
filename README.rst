===================
git-clone-canonical
===================

`clone-canonical` is a git extension that lets you clone popular open source
projects by *name* instead of *location*.


Installation
============

::

    pip install git-clone-canonical


Clone
=====

Clone a repo by name::

    git clone-canonical sqlalchemy


Update
======

You can grab the latest repos by running::

    git clone-canonical --update


Search
======

To find all repos that have `openstack` as a keyword::

    git clone-canonical --search openstack



Extras
======

A repo can specify RCS=hg to signify that Mercurial should be used.
