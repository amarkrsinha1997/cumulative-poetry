# seperate what varies from what stays the same.

class EchoFormatter:
    def echo(self, array):
        return ["{0}\n\t{1}".format(elem, elem) for elem in array]


class NoEchoFormatter:
    def echo(self, array):
        return array

## OCP - open - closed principle - open for extension, closed for modification...

class AlternatingEchoFormatter:
    def _echo(self,i,line):
        if i % 2 == 0:
            return EchoFormatter().echo([line])[0]
        else:
            return line
    
    def echo(self,lines):
        return [self._echo(i,line) for (i,line) in enumerate(lines)] 
