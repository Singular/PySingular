import SingularPython
from SingularPython import RunSingularCommand

RunSingularCommand( "ring r;" );
RunSingularCommand( "r;" );
RunSingularCommand( "ideal I = (x^2,xy,y^2,x^3);" );
RunSingularCommand( "std( I );" );