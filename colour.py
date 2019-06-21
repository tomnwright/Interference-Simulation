#colour ramp

def get_rgb(n):
    return (
        int(get_r(n)*255),
        int(get_g(n)*255),
        int(get_b(n)*255)
    )

def get_r(n):
    if n>0:
        return 1.0
    else:
        return n+1

def get_b(n):
    if n<0:
        return 1.0
    else:
        return 1-n

def get_g(n):
    if n>=0:
        return 1-n
    else:
        return n+1