"""
    progressbar.py
    
    A Python module with a ProgressBar class which can be used to represent a
    task's progress in the form of a progress bar and it can be formated in a
    basic way.
    
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
"""
import sys
import time

class TaskCompleted(Exception):
    """docstring for TaskCompleted"""
    pass
        

class ProgressBar(object):
    """docstring for ProgressBar
    """
    def __init__(self, start=0, end=10, width=12, fill='=', blank='.',
                format='[%(fill)s>%(blank)s] %(progress)s%%', 
                incremental=True):
        super(ProgressBar, self).__init__()
        self.start = start
        self.end = end
        self.width = width
        self.fill = fill
        self.blank = blank
        self.format = format
        self.incremental = incremental
        
        self.step = 100 / width
        
        self.reset()
    
    def __add__(self, increment):
        """docstring for __add__"""
        increment = self._get_progress(increment)
        if 100 > self.progress:
            if 100 > self.progress + increment:
                self.progress += increment
            else:
                self.progress = 100
        else:
            raise TaskCompleted
        return self
    
    def __str__(self):
        """docstring for __str__"""
        progressed = int(self.progress) / self.step
        fill = progressed * self.fill
        blank = (self.width - progressed) * self.blank
        return self.format % {'fill': fill, 'blank': blank, 
                    'progress': int(self.progress)}
    
    __repr__ = __str__
    
    def _get_progress(self, increment):
        return float(increment * 100) / self.end
    
    def reset(self):
        """docstring for reset"""
        self.progress = self._get_progress(self.start)
        return self


class AnimatedProgressBar(ProgressBar):
    """The animated version. To use straighforward on a script"""
    def __init__(self, *args, **kwargs):
        super(AnimatedProgressBar, self).__init__(*args, **kwargs)
        self.stdout = sys.stdout
    
    def show_progress(self):
        self.stdout.write('\r')
        self.stdout.write(str(self))
        self.stdout.flush()
        time.sleep(0.01)

if __name__ == '__main__':
    p = AnimatedProgressBar(end=1000000, width=20)
    
    try:
        while True:
            p + 1000
            p.show_progress()
    except TaskCompleted, e:
        print "Completed!"
        