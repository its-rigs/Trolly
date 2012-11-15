Trolly
======

A wrapper around the Trello API. Provides a group of classes to represent Trello Objects. None of the classes cache values as they are designed to be inherited and extended to suit the needs of each user. Each class includes a basic set of methods based on general use cases.

    class MyList( List ):
        
        def __init__( self, board, list_id, name = '' ):
            
            super( MyList, self ).__init__( board, cli )