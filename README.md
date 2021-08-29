## Hough Transform
Line detection can be done using Hough Transform. However we first need to see an alternate way to represent straight lines. Straight lines can be represented using the following parameters instead of the traditional slope and y-intersepct:

$/theta$: Angle between the normal and the x-axis.
$/rho$: Perpendicular distance to the line from Origin.

The lines can be represented as : rho = x * sin(theta) + y * cos(theta) where x and y are point coordinates.

We also need to define a Hough space. Hough space can be interpreted as an inverse of the space where the lines are situated. In the Hough space the x-axis is theta and the y-axis is rho. Therefore, each point on the Hough space corresponds to a line on the 2D space $R^2$. Similarly each point on $R^2$ can be mapped as a line or curve onto the Hough space.

In order to detect lines in an image we need to first detect the edges. Then for each edge point on the edge image, for combination of all possible theta and rho values their occurances are mapped to the Hough space. After that, from the hough space we take the points which have the highest occurances.
