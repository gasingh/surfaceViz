# surfaceViz
A repo to showcase _3d surface plot_ experiments inside Rhino/IronPython. Note: we don't employ any standard Python libraries like Numpy, Matplotlib, etc; as they are not compatible with the IronPython which is as .NET port of Python. We mimiced the standard generation functions to build a set of visualization methods in RhinoCommon instead.

- Enepper Surface
- Monkey Saddle 
- Mobeus Strip
- Klein Bottle
- Egg Crate
- Pringle Surface
- Dini's Surface
- Super Formula Surfaces


## Enepper Surface
![210625 18 6_ 2 0 scale](https://user-images.githubusercontent.com/6398561/145767247-bce844ce-658b-47ab-8060-0384c6439a91.jpg)

'''
%Equation of a straight line is $y= mx + c$\\
$$
r(\varphi) = (|\frac{cos(\frac{m\varphi}{4})}{a}|^{n_2} + |\frac{sin(\frac{m\varphi}{4})}{b}|^{n_3})^{-\frac{1}{n_1}}
$$

by choosing different values for the parameters $a,b,m,n_1,n_2,n_3$, different shapes can be generated.

It is possible to extend the formula to 3,4, $n$ dimensions, by means of the spherical product of superformulas.
The parametric equations are as follows:

\begin{align}
x &= r_1(\theta)cos\theta \cdot r_2(\phi)cos\phi \\
y &= r_1(\theta)sin\theta \cdot r_2(\phi)cos\phi \\
z &= r_2(\phi)sin\phi
\end{align}
where $-\frac{\pi}{2} > \phi > \frac{\pi}{2},$ and $\-\pi > \theta > \pi$ \\
'''


## Monkey Saddle 

![210614 01 img9 1](https://user-images.githubusercontent.com/6398561/145766916-029f94cc-10ad-4060-afe2-472116c45d47.jpg)

## Mobeus Strip
![210622_01](https://user-images.githubusercontent.com/6398561/145766822-242bbfb8-ae64-4a5f-8f6f-ee79073a6e63.jpg)

## Klein Bottle
![210623 07_triColorizationRoutines 3](https://user-images.githubusercontent.com/6398561/145766988-f96e01f6-fa52-47dd-a5f3-f439497786a4.jpg)

## Egg Crate

![210614 01_210618 01_K](https://user-images.githubusercontent.com/6398561/145766874-24fcfc4b-d140-4782-896f-a427c20d53e6.jpg)

## Pringle Surface

![210623 03](https://user-images.githubusercontent.com/6398561/145766772-27834841-5d17-4e2f-9b3e-d34d53b025e2.jpg)

## Dini's Surface
![210623 06](https://user-images.githubusercontent.com/6398561/145766700-92816276-f3cf-4f51-9780-9a45b8fcf425.jpg)

## Super Formula Surfaces

![__210714 04_typeD](https://user-images.githubusercontent.com/6398561/145766254-513d5073-6f0e-4eed-b591-b5236f389e0b.jpg)

