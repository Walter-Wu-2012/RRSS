from scipy import interpolate

def interpolation(x, y, xnew):
    f = interpolate.interp1d(x, y, kind='quadratic')
    ynew = f(xnew)