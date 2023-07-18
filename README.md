# surfaceViz
A repo to showcase _3d surface plot_ experiments inside Rhino/IronPython. 

- Note: we don't employ any standard Python libraries like Numpy, Matplotlib, etc; as they are not compatible with the IronPython which is as .NET port of Python. 
- We mimiced the standard generation functions to build a set of visualization methods in RhinoCommon instead.
- The system can produce Point Clouds, Meshes, and Surface representations.
- Additional colorization routines are also encoded, which include a height-based colorizer, and an internal generation sequence visualizer, and various color gradients.

The repository currently hosts 10 general parametric surface equations, and the Super Formula equation.

1. Enepper Surface
1. Monkey Saddle 
1. Mobeus Strip
1. Klein Bottle
1. Egg Crate Surface
1. Pringle Surface
1. Dini's Surface
1. Bump Surface
1. Flower Surface
1. Vault-like Surface
1. Super Formula Surfaces


<!--
```math
\displaylines{
}
```
-->

## ENEPPER SURFACE

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
![210624 87](https://user-images.githubusercontent.com/6398561/227831712-1ffe47ac-53fa-4da0-a879-56795792ab2e.jpg)
![210624 82](https://user-images.githubusercontent.com/6398561/227831882-c03b7735-d6bb-4fe4-951a-2704b2d68829.jpg)
![210624 03](https://user-images.githubusercontent.com/6398561/227832067-b080a29a-e26c-4224-926a-0ea946872bd0.jpg)



<p align="center" width="100%">
  View in 3D! <br>
  <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/Enepper%20Surface_v2B.19_higherOrderVersion10-D_fixed2_variations!!_iterationGen_02_hiResPrinter.py_03_(orig).3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
</p>

<!-- [<img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width = "35">](https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/Enepper%20Surface_v2B.19_higherOrderVersion10-D_fixed2_variations!!_iterationGen_02_hiResPrinter.py_03_(orig).3dm) -->

<!-- [**VIEW 3D**](https://3dviewer.net/#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/Enepper%20Surface_v2B.19_higherOrderVersion10-D_fixed2_variations!!_iterationGen_02_hiResPrinter.py_03.stl) -->

## MONKEY SADDLE

```math
\displaylines{
\begin{equation*}
z = x^3 - 3xy^2
\end{equation*}
}
```

This equation defines a surface in three dimensions where $z$ is a function of $x$ and $y$, with the height of the surface at any point $(x,y)$ determined by the expression $x^3 - 3xy^2$. The Monkey Saddle is a saddle-shaped surface, with two saddle points at $(0,0)$ and $(\pm\sqrt{3/2},0)$.

![210614 01 img9 1](https://user-images.githubusercontent.com/6398561/145766916-029f94cc-10ad-4060-afe2-472116c45d47.jpg)

## MOBEUS STRIP
```math
\displaylines{
\begin{align*}
x &= (1 + \frac{v}{2}\cos(\frac{1}{2}u))\cos(u) \
y &= (1 + \frac{v}{2}\cos(\frac{1}{2}u))\sin(u) \
z &= \frac{v}{2}\sin(\frac{1}{2}u)
\end{align*}
}
```

This defines the three-dimensional function $(x, y, z)$, which is a parametric surface defined over the ranges $u \in (0, 2\pi)$ and $v \in (-1, 1)$.

![210622_01](https://user-images.githubusercontent.com/6398561/145766822-242bbfb8-ae64-4a5f-8f6f-ee79073a6e63.jpg)

## KLEIN BOTTLE

```math
\displaylines{
\begin{align*}
x &= aa + \cos\left(\frac{v}{2}\right)\sin u - \sin\left(\frac{v}{2}\right)\sin(2u)\cos v \
y &= aa + \cos\left(\frac{v}{2}\right)\sin u - \sin\left(\frac{v}{2}\right)\sin(2u)\sin v \
z &= \sin\left(\frac{v}{2}\right)\sin u + \cos\left(\frac{v}{2}\right)\sin(2u)
\end{align*}
}
```

This defines the three-dimensional function $(x, y, z)$, which is a parametric surface defined over the ranges $u \in (0, 2\pi)$ and $v \in (0, 6)$.

![210623 07_triColorizationRoutines 3](https://user-images.githubusercontent.com/6398561/145766988-f96e01f6-fa52-47dd-a5f3-f439497786a4.jpg)

## EGG CRATE SURFACE
```math
\displaylines{
\begin{equation*}
z = \sin(xh_2) \cdot \cos(yh_2) \cdot h_1
\end{equation*}
}
```
where $x$ and $y$ are defined as follows:
```math
\displaylines{
\begin{equation*}
x = \begin{cases}
-v, & -v < x < v \
v, & \text{otherwise}
\end{cases} \quad \text{and} \quad
y = \begin{cases}
-v, & -v < y < v \
v, & \text{otherwise}
\end{cases}
\end{equation*}
}
```
This defines a surface in three dimensions where $z$ is a function of $x$ and $y$, with $x$ and $y$ constrained to the square region $-v < x, y < v$. The height of the surface at any point $(x,y)$ is proportional to $\sin(xh_2)\cos(yh_2)$ and scaled by the constant $h_1$.

![210614 01_210618 01_K](https://user-images.githubusercontent.com/6398561/145766874-24fcfc4b-d140-4782-896f-a427c20d53e6.jpg)

## PRINGLE SURFACE
```math
\displaylines{
\begin{equation*}
z = \begin{cases}
\sin(x^4) + \cos(y^4), & 0 < x < u \sin(v) \text{ and } 0 < y < u \sin(v) \
0, & \text{otherwise}
\end{cases}
\end{equation*}
}
```
![210623 03](https://user-images.githubusercontent.com/6398561/145766772-27834841-5d17-4e2f-9b3e-d34d53b025e2.jpg)

## DINI'S SURFACE

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

## BUMP SURFACE

```math
\displaylines{
\begin{equation*}
z = e^{-(x^2+y^2)}h
\end{equation*}
}
```
where $x$ and $y$ are defined as follows:

```math
\displaylines{
\begin{equation*}
x = \begin{cases}
-v, & -v < x < v \
v, & \text{otherwise}
\end{cases} \quad \text{and} \quad
y = \begin{cases}
-v, & -v < y < v \
v, & \text{otherwise}
\end{cases}
\end{equation*}
}
```

This defines a surface in three dimensions where $z$ is a function of $x$ and $y$, with $x$ and $y$ constrained to the square region $-v < x, y < v$. The height of the surface at any point $(x,y)$ is proportional to $e^{-(x^2+y^2)}$ and scaled by the constant $h$.

![210616 09](https://user-images.githubusercontent.com/6398561/227825742-e9355a48-66bf-42b4-8854-0f148092fe34.jpg)

<!--
![210616 10](https://user-images.githubusercontent.com/6398561/227824747-fea30178-8ab1-470d-a561-fa479e2c0027.jpg)
-->


## FLOWER SURFACE

```math
\displaylines{
\begin{equation*}
z = \sin(\sqrt{x^2+y^2}) \cdot h
\end{equation*}
}
```
where $x$ and $y$ are defined as follows:
```math
\displaylines{
\begin{equation*}
x = \begin{cases}
-v, & -v < x < v \
v, & \text{otherwise}
\end{cases} \quad \text{and} \quad
y = \begin{cases}
-v, & -v < y < v \
v, & \text{otherwise}
\end{cases}
\end{equation*}
}
```

This defines a surface in three dimensions where $z$ is a function of $x$ and $y$, with $x$ and $y$ constrained to the square region $-v < x, y < v$. The height of the surface at any point $(x,y)$ is proportional to $\sin(\sqrt{x^2+y^2})$ and scaled by the constant $h$.


![210614 01 img10 1](https://user-images.githubusercontent.com/6398561/227827108-ca27b0da-f943-411e-9f5e-8e46d5e05140.jpg)

## VAULT-LIKE SURFACE
```math
\displaylines{
\begin{equation*}
z = h_1 - (x^2 + y^2)
\end{equation*}
}
```
where $x$ and $y$ are defined as follows:
```math
\displaylines{
\begin{equation*}
x = \begin{cases}
-v, & -v < x < v \
v, & \text{otherwise}
\end{cases} \quad \text{and} \quad
y = \begin{cases}
-v, & -v < y < v \
v, & \text{otherwise}
\end{cases}
\end{equation*}
}
```
This defines a surface in three dimensions where $z$ is a function of $x$ and $y$, with $x$ and $y$ constrained to the square region $-v < x, y < v$. The height of the surface at any point $(x,y)$ is proportional to the difference between a constant value $h_1$ and the sum of the squares of $x$ and $y$.

<!--
![numpyInspired3DPlots_v1_img7](https://user-images.githubusercontent.com/6398561/227830589-e0fb9652-b7e8-4072-8ac4-1632e896ff69.jpg)
-->
![210616 31](https://user-images.githubusercontent.com/6398561/227831326-00ffb1c6-354e-4b7d-8ef1-4158c4c0ca6b.jpg)


## SUPER FORMULA SURFACES

```math
\displaylines{
r(\varphi) = (|\frac{cos(\frac{m\varphi}{4})}{a}|^{n_2} + |\frac{sin(\frac{m\varphi}{4})}{b}|^{n_3})^{-\frac{1}{n_1}}
}
```

by choosing different values for the parameters `a,b,m,n_1,n_2,n_3`, different shapes can be generated.
It is possible to extend the formula to 3,4, `n` dimensions, by means of the spherical product of superformulas.
The parametric equations are as follows:

```math
\displaylines{
x = r_1(\theta)cos\theta \cdot r_2(\phi)cos\phi \\
y = r_1(\theta)sin\theta \cdot r_2(\phi)cos\phi \\
z = r_2(\phi)sin\phi \\
}
```

where 

```math
\displaylines{
-\frac{\pi}{2} > {\phi} > \frac{\pi}{2} \\
-{\pi} > {\theta} > {\pi} \\
}
```

![__210714 04_typeD](https://user-images.githubusercontent.com/6398561/145766254-513d5073-6f0e-4eed-b591-b5236f389e0b.jpg)
![__210714 04_typeB](https://user-images.githubusercontent.com/6398561/227833532-6cd35617-dac3-412c-9a47-87940fb3b194.jpg)
<!-- ![__210714 07_typeA](https://user-images.githubusercontent.com/6398561/227833887-6d3f4c47-bd4d-44c4-981b-03f0caac5eb0.jpg) -->


![210714 28_msh-colored_1](https://user-images.githubusercontent.com/6398561/227833441-a0bc87e7-c392-448c-b223-fc893aad6c6f.jpg)

![210714 11_msh-colored](https://user-images.githubusercontent.com/6398561/227834057-c0cc9f4b-2ffc-488d-bd9c-07f19e94e40c.jpg)

<p align="center" width="100%">
  View the 3D shape variations: <br>
  <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.4-B.gh_(3rd-reduce).3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
    <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.4-C.gh_(2nd-reduce).3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
</p>

<!-- 
![210715 03](https://user-images.githubusercontent.com/6398561/227833317-11e75f48-3207-4724-8184-a5f3936929a2.jpg) -->
![210715 01_transparentPlasticSurface](https://user-images.githubusercontent.com/6398561/227833814-1061c184-b411-4d41-99b4-ae79f1e56186.jpg)

![210714 04](https://user-images.githubusercontent.com/6398561/227833388-907813a1-2f13-40f7-9085-c10ae331fdfd.jpg)
<!-- ![210714 01](https://user-images.githubusercontent.com/6398561/227833406-94c06eea-61df-4799-b7de-81257eb6ddcd.jpg) -->



<p align="center" width="100%">
  View in 3D! <br>
  <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.3.gh_1.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
    <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.3.gh_2_meshStriated.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
</p>

![210715 04_colorRange](https://user-images.githubusercontent.com/6398561/227835167-bc70e910-4394-4f28-a20c-5244f20b6edd.jpg)

<!-- 
![210714 03](https://user-images.githubusercontent.com/6398561/227834004-b1618d4c-4281-4b9e-9544-2a77e7a337d4.jpg) -->

![210714 01](https://user-images.githubusercontent.com/6398561/227835268-e438a6e2-3370-4bea-96ce-d182bba63d65.jpg)

<p align="center" width="100%">
  View in 3D! <br>
  <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-2.py.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
    <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4.gh_01_mesh.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
    <a href="https://3dviewer.net/#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4.gh.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
    <a href="https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.2.gh.3dm"> <img src="https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp" width="35" height="35"> </a>
</p>

![Capture_GH1](https://user-images.githubusercontent.com/6398561/227835450-c061d9db-386e-4d08-85c7-316c6d249068.JPG)

<!-- [<img src="img/myImage.png">](http://example.com/) -->
<!-- [![](https://github.com/gasingh/surfaceViz/blob/main/shape_files/icon_online-3d-viewer_190499.webp)](https://3dviewer.net/index.html#model=https://github.com/gasingh/surfaceViz/blob/main/shape_files/superSurface_01F-4_surfacer.4-B.gh_(3rd-reduce).3dm) -->

[Source: Math Equations on my GitLab Repo](https://gitlab.com/gasingh/mathSurfaces/-/blob/c07bfc86433f5cd4a9437638ec126a38e5edd09b/README.md)
