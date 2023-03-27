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


<!--
```math
\displaylines{
}
```
-->

## Enepper Surface

```math
\displaylines{
\begin{aligned}
x &= u\cos(v) - \frac{u^b \cos(bv)}{b}  \
y &= u\sin(v) + \frac{u^b \sin(bv)}{b}  \
z &= 2u^a \frac{\cos(av)}{a}
\end{aligned}
}
```
with 
```math
\displaylines{
\begin{aligned}
0 < u < 1.2 \
-\pi < v < \pi
\end{aligned}
}
```

![210625 18 6_ 2 0 scale](https://user-images.githubusercontent.com/6398561/145767247-bce844ce-658b-47ab-8060-0384c6439a91.jpg)

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

```math
\displaylines{
\begin{aligned}
\begin{equation*}
f(u,v) = \left(\cos(u)\sin(v), \sin(u)\sin(v), \cos(v) + \log\left(\tan\left(\frac{v}{2}\right)\right) + a u\right),
\end{equation*}
\end{aligned}
}
```
with 
```math
\displaylines{
\begin{aligned}
0 \leq u \leq 2\pi \
0 < v < \pi
\end{aligned}
}
```

![210623 06](https://user-images.githubusercontent.com/6398561/145766700-92816276-f3cf-4f51-9780-9a45b8fcf425.jpg)

## Super Formula Surfaces

![__210714 04_typeD](https://user-images.githubusercontent.com/6398561/145766254-513d5073-6f0e-4eed-b591-b5236f389e0b.jpg)

[Math Equations on my GitLab Repo](https://gitlab.com/gasingh/mathSurfaces/-/blob/c07bfc86433f5cd4a9437638ec126a38e5edd09b/README.md)
