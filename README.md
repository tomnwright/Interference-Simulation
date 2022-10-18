# Interference-Simulation
Simulation of the interference pattern between *n* coherent[<sup>1</sup>](https://github.com/tomnwright/Interference-Simulation/issues/2) sources. Each source is assigned a pixel location. Then, for each pixel, the distance from that pixel to each source is calculated and used to calculate the amplitude of the wave from each source. These amplitudes are added to find the superposition of all waves at that point. A separate function interpolates between blue (-1), white (0), and red (+1), and is used to assign each pixel a colour based on its wave superposition. Wave functions return between -1 (trough) and +1 (peak), but the superposition of these waves may exceed this range.

The amplitude, *I*, of the wave from each source at a given pixel is calculated as a function of the distance of that pixel to the source. For source A:

<a href="https://www.codecogs.com/eqnedit.php?latex=I&space;=&space;\sin{d}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?I&space;=&space;\sin{d}" title="I = \sin{d}" /></a>

This produces a wave with a wavelength of <a href="https://www.codecogs.com/eqnedit.php?latex=2\pi" target="_blank"><img src="https://latex.codecogs.com/svg.latex?2\pi" title="2\pi" /></a>. Therefore scaling the function along the *d* axis by a factor of

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\lambda&space;s}{2\pi}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\frac{\lambda&space;s}{2\pi}" title="\frac{\lambda s}{2\pi}" /></a>

, where *s* is the number of pixels per unit distance (pixel **s**cale), produces a wave with a wavelength of *s* px:

<a href="https://www.codecogs.com/eqnedit.php?latex=I&space;=&space;\sin{\frac{2\pi&space;d}{\lambda&space;s}}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?I&space;=&space;\sin{\frac{2\pi&space;d}{\lambda&space;s}}" title="I = \sin{\frac{2\pi d}{\lambda s}}" /></a>

Next the wave is translated along the x axis as a function of the amount of time which has passed, allowing animation. If the wave moves along the *d* axis at a rate of one wavelength per second, then its dispacement, *k* is given as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;k&space;&=&space;t_{seconds}&space;\cdot&space;\lambda&space;s&space;&plus;&space;p&space;\lambda&space;s\\&space;&=&space;\frac{t&space;\lambda&space;s}{f}&plus;&space;p&space;\lambda&space;s&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;k&space;&=&space;t_{seconds}&space;\cdot&space;\lambda&space;s&space;&plus;&space;p&space;\lambda&space;s\\&space;&=&space;\frac{t&space;\lambda&space;s}{f}&plus;&space;p&space;\lambda&space;s&space;\end{align*}" title="\begin{align*} k &= t_{seconds} \cdot \lambda s + p \lambda s\\ &= \frac{t \lambda s}{f}+ p \lambda s \end{align*}" /></a>, where:
* *t* is time in frames, and *f* is video frame rate.
* *p* is phase, as a fraction of wavelength

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{align*}&space;\therefore&space;I&space;&=&space;\sin{\frac{2\pi&space;(d-k)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(d-\frac{t&space;\lambda&space;s}{f}&space;-&space;p&space;\lambda&space;s)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(\frac{fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{align*}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\therefore&space;I&space;&=&space;\sin{\frac{2\pi&space;(d-k)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(d-\frac{t&space;\lambda&space;s}{f}&space;-&space;p&space;\lambda&space;s)}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(\frac{fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s}{f})}{\lambda&space;s}}\\&space;&=&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{align*}" title="\begin{align*} \therefore I &= \sin{\frac{2\pi (d-k)}{\lambda s}}\\ &= \sin{\frac{2\pi (d-\frac{t \lambda s}{f} - p \lambda s)}{\lambda s}}\\ &= \sin{\frac{2\pi (\frac{fd - t \lambda s- fp \lambda s}{f})}{\lambda s}}\\ &= \sin{\frac{2\pi (fd - t \lambda s- fp \lambda s)}{f \lambda s}} \end{align*}" /></a>

Also, *k* gives the leading edge of the wave, allowing restriction of the wave domains:

<a href="https://www.codecogs.com/eqnedit.php?latex=I&space;=&space;f(d)&space;\left\{&space;\begin{array}{lr}&space;d>k&space;:&space;0\\&space;d\leq&space;k:&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{array}&space;\right." target="_blank"><img src="https://latex.codecogs.com/svg.latex?I&space;=&space;f(d)&space;\left\{&space;\begin{array}{lr}&space;d>k&space;:&space;0\\&space;d\leq&space;k:&space;\sin{\frac{2\pi&space;(fd&space;-&space;t&space;\lambda&space;s-&space;fp&space;\lambda&space;s)}{f&space;\lambda&space;s}}&space;\end{array}&space;\right." title="I = f(d) \left\{ \begin{array}{lr} d>k : 0\\ d\leq k: \sin{\frac{2\pi (fd - t \lambda s- fp \lambda s)}{f \lambda s}} \end{array} \right." /></a>
## Time Scale
The <a href="https://www.codecogs.com/eqnedit.php?latex=t_{\text{seconds}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?t_{\text{seconds}}" title="t_{\text{seconds}}" /></a> value above, is in terms of video seconds. However, if the waves are assumed to be sound in air, an absolute time value can be calculated. In one video second, the wave travels 1 wavelength. The speed of sound in air is 343 ms<sup>-1</sup>. Therefore, the sound wave takes <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{343}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{343}" title="\frac{1}{343}" /></a> virtual seconds to travel that one wavelength, 1m (only if <a href="https://www.codecogs.com/eqnedit.php?latex=\lambda&space;=&space;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\lambda&space;=&space;1" title="\lambda = 1" /></a>). Therefore, 1 video second (25 frames) = <a href="https://www.codecogs.com/eqnedit.php?latex=\frac{1}{343}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{343}" title="\frac{1}{343}" /></a> virtual seconds.


## Demo
Watch on YouTube:
https://www.youtube.com/watch?v=CgBImdjw3hc

[![Interference Demo Video](https://img.youtube.com/vi/CgBImdjw3hc/0.jpg)](https://www.youtube.com/watch?v=CgBImdjw3hc)
