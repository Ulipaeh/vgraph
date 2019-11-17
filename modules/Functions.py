def is_visible (y ,a ,b ):
    isit = True
    c = a +1
    while isit and c < b:
        isit = y[c]<y[b]+(y[a]-y[b])*((b-c)/float(b -a ))
        c = c +1
    return isit

def grado_max (G):
    return max(dict(G.degree(G.nodes())). values ())

