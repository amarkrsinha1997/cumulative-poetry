Polymorphism
```python
# def __init__(self, poem, shouldEcho=False, shouldEchoAlternate=False, startWith1stOr2nd = 1): 
    # TODO - growth of this feature will lead to too many parameter problem
        
        # Poet(poem) -- no echo
        # Poet(poem, shouldEcho = True) -- just echo
        # Poet(poem, shouldEchoAlternate = True, shouldEcho = ???) -- Now as a consumer I am confused.
        
        # if shouldEchoAlternate:
        #     # consumer's code will work
        #     pass
        # if shouldEcho: # consumer's code will not work
        #     if shouldEchoAlternate: 
        #     pass
        # {
        #   "shouldEcho" 
        # }

        # {
        #     "shouldEcho" : True,
        #     "shouldEchoAlternating" : True,
        #     "numberOfTimes" : 3,
        #     "startWith1stOr2nd" : 2 
        # }
        # {
        #     "shouldEcho" : {
        #         "shouldEchoAlternating" : True,
        #     },
        #     "numberOfTimes" : 3,
        #     "startWith1stOr2nd" : 2
        # }

        # {
        #     "shouldEchoAlternating" : True,
        # }

```