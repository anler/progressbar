
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
        if 100 >= self.progress + increment:
            self.progress += self._get_progress(increment)
        return self
    
    def __str__(self):
        """docstring for __str__"""
        progressed = self.progress / self.step
        fill = progressed * self.fill
        blank = (self.width - progressed) * self.blank
        return self.format % {'fill': fill, 'blank': blank, 
                    'progress': self.progress}
    
    __repr__ = __str__
    
    def _get_progress(self, increment):
        return (increment * 100) / self.end
    
    def reset(self):
        """docstring for reset"""
        self.progress = self._get_progress(self.start)
        return self