from matplotlib.backends.backend_qt5 import NavigationToolbar2QT


class MyNavigationToolbar(NavigationToolbar2QT):

    toolitems = [t for t in NavigationToolbar2QT.toolitems if
                 t[0] in ('Home','Pan', 'Zoom', 'Save','Subplots')]