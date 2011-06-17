Python Progressbar
==================

A progressbar utility for the command line.
Progressbar is a Python module with a ProgressBar class which can be used to represent a task's progress in the form of a progress bar and it can be formated in a basic way.

Here is some basic usage with the default options:

    >>> from progressbar import ProgressBar
    >>> p = ProgressBar()
    >>> print p
    [>............] 0%
    >>> p + 1
    >>> print p
    [=>...........] 10%
    >>> p + 9
    >>> print p
    [============>] 0%

And here another example with different options:

    >>> from progressbar import ProgressBar
    >>> custom_options = {
    ...     'end': 100, 
    ...     'width': 20, 
    ...     'fill': '#',
    ...     'format': '%(progress)s%% [%(fill)s%(blank)s]'
    ... }
    >>> p = ProgressBar(**custom_options)
    >>> print p
    0% [....................]
    >>> p + 5
    >>> print p
    5% [#...................]
    >>> p + 9
    >>> print p
    100% [####################]
