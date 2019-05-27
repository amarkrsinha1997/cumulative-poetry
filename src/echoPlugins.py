# seperate what varies from what stays the same.

class Echo:
    def echo(self, array):
        return ["{0}\n\t{1}".format(elem, elem) for elem in array]


class NoEcho:
    def echo(self, array):
        return array

## OCP - open - closed principle - open for extension, closed for modification...

class AlternatingEcho:
    def _echo(self,i,line):
        if i % 2 == 0:
            return Echo().echo([line])[0]
        else:
            return line
    
    def echo(self,lines):
        return [self._echo(i,line) for (i,line) in enumerate(lines)] 
