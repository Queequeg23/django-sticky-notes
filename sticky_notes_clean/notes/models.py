from django.db import models


# Sticky_note models defined here
class Note(models.Model):
    '''
    Model representing a sticky note
    Attributes:
    title - CharField up to 255 characters, banks not allowed by default
    content - TextField for body of note, blanks not allowed by default
    created_at - time and date created
    (equivalent to TIMESTAMP in SQL) immutable
    updated_at - time and date modified, modified after each edit
    '''
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Configure subclass to define default query operations to oder by
    # date updated. Separately defined from attributes as not a DB column
    class Meta:
        '''
        Defines default ordering of queries
        '''
        ordering = ['-updated_at']

    def __str__(self):
        '''
        Defines default display for note object
        :param self: Description
        '''
        return self.title
