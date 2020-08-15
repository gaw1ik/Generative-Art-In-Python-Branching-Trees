# Generative Art In Python: Branching Trees

This repo details an algorithm for creating a branching structure for generative art creations. This algorithm can be used to create anything with a branching geometry, most notably - trees. 

If you would like to follow my art (and also gawk at some old food pics) you can check me out on instagram  [@brian_gawlik](https://www.instagram.com/brian_gawlik/?hl=en).

<p align="center">
   <img src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/example2.png" width="48.5%"/>
   <img src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/test2.gif" width="48.5%"/>
</p>

<p align="center">
   <img align="center" src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/example6.png" width="24%" />
   <img align="center" src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/example7.png" width="24%"/>
   <img align="center" src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/example8.png" width="24%"/>
   <img align="center" src="https://github.com/gaw1ik/Generative-Art-In-Python-Tree-Branching/blob/master/example9.png" width="24%"/>
</p>

## Description of the Algorithm
The algorithm utilizes the pycairo library to draw line segments which define the branches in a hierarchical manner as is shown in the GIF above. The algorithm begins by starting a line at the starting point (x1,y1 - as defined in the Inputs section) and then draws a line between that point and the point (x2,y2), which is defined by a length (selected randomly) and an angle (also selected randomly). The ranges for the available lengths and angles are constrained so that the line segments won't be too large or get tangled up with each other. The angles are chosen as a deviation from the current angle of trajectory. If the angle range is set relatively small (e.g. -10 to 10 degrees) the branches will meander in a relatively straight line, but will twist and turn just enough to appear like an organically grown tree branch. This "growing" process is repeated until the total length of the branch exceeds a maximum value (I used something like 0.6 for example, which means 60% the width of the frame). As this process is ensuing, branch points will randomly be triggered by choosing from a list containing 0's and 1's, e.g. choice([0,0,0,0,1]). So, occasionally a branch point will be triggered and the coordinate of all the branch points are recorded. The algorithm finishes drawing the current branch, but after, draws another branch starting from *each* branch point, and the branch triggering process is repeated for each new branch resulting in recursive growth. This process is done *nBranches* number of times.  

## Going Beyond the Basic Algorithm
The code included above "makeBranches.py" is a relatively simple incarnation of the algorithm. Well actually, if you mess around with the inputs, it still has quite a lot of of power, but in my own adventures, I have added more advanced bits of functionality. Many of these additional functionalities can be seen in the images above including more detailed coloring and the ability to place objects on the branches like berries, leaves, ornaments, etc. I've also added the ability to control the branch thicknesses so that the lower level branches can become progressively thinner. Similarly, I've added the ability to control the initial spliting angle for each branch level. If you look at trees in real life, you will notice there is a hierarchical instruction for how they grow. The first split might happen at around +/- 20 degrees and subseqeuent splits near the leaves may approach +/- 90 degrees. Every plant and tree has it's own unique set of instructions and defining these traits for each branch offers a wide variety of results. 
