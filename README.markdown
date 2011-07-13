Python Progressbar
==================

A progressbar utility for command line programs.
Progressbar is a Python module which contains two class so far:

    ProgressBar
    AnimatedProgressBar

ProgressBar class implements all the base stuffs that makes progress bars work as they does and admit some basic customization.
AnimatedProgressBar class extends ProgressBar to allow you to use it straightforward in your scripts. By default the AnimatedProgressBar
sends the output to sys.stdout but you can change this passing a the `stdout` keyword parameter which must be a file-like object.

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

Finally, a real example where I had to use it:

	>>> import ftplib
	>>> import progressbar
	>>>
	>>> ftp = ftplib.FTP('ftp.myserver.com', 'user', 'passwd')
	>>> filesize = ftp.size('path/to/remotefile.zip')
	>>> progress = progressbar.AnimatedProgressBar(end=filesize, width=50)
	>>>
	>>> with open('localfile.zip', 'w') as f:
	>>>		def callback(chunk):
	>>>			f.write(chunk)
	>>>			progress + len(chunk)
	>>>
	>>>			# Visual feedback of the progress!
	>>>			progress.show_progress()
	>>>		
	>>>		ftp.retrbinary('RETR path/to/remotefile.zip', callback)

