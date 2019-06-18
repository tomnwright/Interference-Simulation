# Interference-Simulation
Simulation of the interference pattern between two coherent sources. Each source is assigned a pixel location. Then, for each pixel, the distance from that pixel to each source is calculated and used to calculate the amplitude of the wave from each source. These amplitudes are added to find the superposition of the two waves, producing a value between -1 (trough) and +1 (peak). A separate function interpolates between blue (-1), white (0), and red (+1), and is used to assign each pixel a colour based on its wave superposition.

The amplitude of each wave at a gien pixel is calculated as a function of the distance of that pixel from each source. For source A:

<a href="https://www.codecogs.com/eqnedit.php?latex=I_a&space;=&space;\sin{d}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?I_a&space;=&space;\sin{d}" title="I_a = \sin{d}" /></a>

This produces a wave with a wavelength of <a href="https://www.codecogs.com/eqnedit.php?latex=2\pi" target="_blank"><img src="https://latex.codecogs.com/svg.latex?2\pi" title="2\pi" /></a>. Therefore scaling the function along the *d* axis by a factor of

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\lambda&space;s}{2\pi}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\frac{\lambda&space;s}{2\pi}" title="\frac{\lambda s}{2\pi}" /></a>

, where *s* is the number of pixels per unit distance (pixel **s**cale), produces a wave with a wavelength of *s* px:

<a href="https://www.codecogs.com/eqnedit.php?latex=I_a&space;=&space;\sin{\frac{2\pi&space;d}{\lambda&space;s}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I_a&space;=&space;\sin{\frac{2\pi&space;d}{\lambda&space;s}}" title="I_a = \sin{\frac{2\pi d}{\lambda s}}" /></a>

Next the wave is translated along the x axis as a function of the amount of time which has passed, allowing animation. If the wave moves along the *d* axis at a rate of one wavelength per second, then its dispacement, *k* is given as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;k&space;&=&space;t_{seconds}&space;\cdot&space;\lambda&space;s\\&space;&=&space;\frac{t&space;\lambda&space;s}{f}&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;k&space;&=&space;t_{seconds}&space;\cdot&space;\lambda&space;s\\&space;&=&space;\frac{t&space;\lambda&space;s}{f}&space;\end{align*}" title="\begin{align*} k &= t_{seconds} \cdot \lambda s\\ &= \frac{t \lambda s}{f} \end{align*}" /></a>, where *t* is time in frames, and *f* is video frame rate.

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\therefore&space;I_a&space;&=&space;\sin{\frac{2\pi&space;(d-k)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(d-\frac{t&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(\frac{fd&space;-&space;t&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;\therefore&space;I_a&space;&=&space;\sin{\frac{2\pi&space;(d-k)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(d-\frac{t&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(\frac{fd&space;-&space;t&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{align*}" title="\begin{align*} \therefore I_a &= \sin{\frac{2\pi (d-k)}{\lambda s}}\\ &= \sin{\frac{2\pi (d-\frac{t \lambda s}{f})}{\lambda s}}\\ &= \sin{\frac{2\pi (\frac{fd - t \lambda s}{f})}{\lambda s}}\\ &= \sin{\frac{2\pi (fd - t \lambda s)}{f \lambda s}} \end{align*}" /></a>

Also, *k* gives the leading edge of the wave, allowing restriction of the wave domains:

<a href="https://www.codecogs.com/eqnedit.php?latex=I_a,&space;I_b&space;=&space;f(d)&space;\left\{&space;\begin{array}{lr}&space;d>k&space;:&space;0\\&space;d\leq&space;k:&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?I_a,&space;I_b&space;=&space;f(d)&space;\left\{&space;\begin{array}{lr}&space;d>k&space;:&space;0\\&space;d\leq&space;k:&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{array}&space;\right." title="I_a, I_b = f(d) \left\{ \begin{array}{lr} d>k : 0\\ d\leq k: \sin{\frac{2\pi (fd - t \lambda s)}{f \lambda s}} \end{array} \right." /></a>

In fact, the <a href="https://www.codecogs.com/eqnedit.php?latex=t_{\text{seconds}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t_{\text{seconds}}" title="t_{\text{seconds}}" /></a> value above, is in terms of video seconds. However, if the waves are assumed to be sound in air, an absolute time value can be calculated. In one video second, the wave travels 1 wavelength. The speed of sound in air is 343 ms<sup>-1</sup>. Therefore, the sound wave takes <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{343}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{343}" title="\frac{1}{343}" /></a> virtual seconds to travel that one wavelength, 1m (only if <a href="https://www.codecogs.com/eqnedit.php?latex=\lambda&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\lambda&space;=&space;1" title="\lambda = 1" /></a>). Therefore, 1 video second (25 frames) = <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{343}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{343}" title="\frac{1}{343}" /></a> virtual seconds.

# Output

See [youtube video](https://youtu.be/TV-m9Ic4xkg)
