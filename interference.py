import math,time
from PIL import Image, ImageDraw
def get_dist(a,b):
    x = a[0]-b[0]
    y = a[1]-b[1]
    return math.sqrt((x**2)+(y**2))

class colour:
    @staticmethod
    def get_rgb(n):
        return (
            int(colour.get_r(n)*255),
            int(colour.get_g(n)*255),
            int(colour.get_b(n)*255)
        )
    @staticmethod
    def get_r(n):
        if n>0:
            return 1.0
        else:
            return n+1
    @staticmethod
    def get_b(n):
        if n<0:
            return 1.0
        else:
            return 1-n
    @staticmethod
    def get_g(n):
        if n>=0:
            return 1-n
        else:
            return n+1
    @staticmethod
    def quad(n):
        '''colour ramp for -1<=n<=+1'''
        out  = 1 - (n**2)
        return out
def get_i(d, f, t, s, w):
    '''
    :param d: distance
    :param f: frame rate
    :param t: time (frames)
    :param s: scale (pixels per meter)
    :param w: wavelength'''
    leading_edge = (t*s*w)/f
    if d>leading_edge:
        return 0
    else:
        return math.sin(
            (2*math.pi* ((f*d)-(t*s*w)))/(f*w*s)
        )
def get_Peak(n,t,l,s,f):
    '''
        :param n: nth peak
        :param t: time(frames)
        :param l: lambda (wavelength)
        :param s: Scale (pixels per meter)
        :param f: frame rate '''
    return ((t-((n+0.75)*f))*l*s)/f
def get_Trough(n,t,l,s,f):
    '''
        :param n: nth trough
        :param t: time(frames)
        :param l: lambda (wavelength)
        :param s: Scale (pixels per meter)
        :param f: frame rate '''
    return ((t-((n+0.25)*f))*l*s)/f

def render_imgV(res,frame_rate,time, pixel_scale, wavelength,separation=0.3):
    img = Image.new('RGB', res)
    #sources
    A = (
        int(res[0]/2),
        int((res[1]+ (res[1]*separation))/2)
        )
    B = (
        int(res[0]/2),
        int((res[1]- (res[1]*separation))/2)
        )
    print(A,B)

    settings = (frame_rate, time, pixel_scale, wavelength)
    for x in range(res[0]):
        for y in range(res[1]):
            loc = (x,y,)
            i_a = get_i(get_dist(A,loc),*settings)
            i_b = get_i(get_dist(B,loc),*settings)
            i_total = (i_a+i_b)/2
            img.putpixel((x,y,),colour.get_rgb(i_total))
    return img
def render_imgH(res,frame_rate,time, pixel_scale, wavelength,separation=0.3):
    img = Image.new('RGB', res)
    #sources
    A = (
        int((res[0]+ (res[0]*separation))/2),
        int(res[1]/2),
        )
    B = (
        int((res[0]- (res[0]*separation))/2),
        int(res[1]/2),
        )
    #print(A,B)

    settings = (frame_rate, time, pixel_scale, wavelength)
    for x in range(res[0]):
        for y in range(res[1]):
            loc = (x,y,)

            i_a = get_i(get_dist(A,loc),*settings)
            i_b = get_i(get_dist(B,loc),*settings)
            
            i_total = (i_a+i_b)/2
            img.putpixel((x,y,),colour.get_rgb(i_total))
    return img

def render_contours(peak_or_trough,res,frame_rate,time, pixel_scale, wavelength,separation=0.3):
    img_L = Image.new('RGBA', res); img_R = Image.new('RGBA', res)
    img_Ldraw = ImageDraw.Draw(img_L,'RGBA'); img_Rdraw = ImageDraw.Draw(img_R,'RGBA')
    #sources
    A = (
        int((res[0]+ (res[0]*separation))/2),
        int(res[1]/2),
        )
    B = (
        int((res[0]- (res[0]*separation))/2),
        int(res[1]/2),
        )
    #print(A,B)
    i = 0
    while True:
        r = [get_Trough(i,time,wavelength,pixel_scale,frame_rate),get_Peak(i,time,wavelength,pixel_scale,frame_rate)][peak_or_trough]
        if r<0:
            break
        else:
            img_Rdraw.ellipse((A[0]-r, A[1]-r, A[0]+r, A[1]+r),(0, 0, 0, 0),outline = 'white')#,width=3)
            img_Ldraw.ellipse((B[0]-r, B[1]-r, B[0]+r, B[1]+r),(0, 0, 0, 0),outline = 'white')
        i+=1
    del img_Ldraw; del img_Rdraw
    return Image.alpha_composite(img_L, img_R)

    

def render_animation(folder, start, end, **kwargs):
    for frame in range(start,end):

        x = render_imgH(
            time=frame,
            **kwargs
            )
        x.save('{}/frame_{}.png'.format(folder,frame),format = 'PNG')
        print(frame)

def animate_contours(start, end, **kwargs):
    for frame in range(start, end):
        print(frame, end='')
        x = render_contours(0, #denotes peak/trough
            time = frame,
            **kwargs)
        x.save('troughs/{}.png'.format(frame), format = 'PNG')

        y = render_contours(1, #denotes peak/trough
            time = frame,
            **kwargs)
        y.save('peaks/{}.png'.format(frame), format = 'PNG')
        print(': COMPLETE')
'''x = render_imgH(
    res = (1280,720,),
    frame_rate = 25,
    time = 1500,
    pixel_scale = 50,
    wavelength =  1,
    separation = 0.1
    )
x.show()'''


if __name__ == '__main__':
    animate_contours(0,1000,
        res = (1280,720,),
        frame_rate = 25,
        pixel_scale = 50,
        wavelength =  1,
        separation = 0.1)
#started at 2021 ish
