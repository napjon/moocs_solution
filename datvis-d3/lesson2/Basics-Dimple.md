Dimple JS has been popular for newcomers at D3 because it has gentler
learning curve. It's abstract the lower level of D3, such as append(),
enter(), and data(). Dimple also abstract the shape, scale and
positioning of D3. It's built on top of D3, and you can dig into more
customization with D3, within DimpleJS.

There is a method called Sketching. Sketching let you use couple of
visualization, to determine the best chart. While it's often not for our
best preference, we don't know how our data interact with aesthetics. 

There's simple explanation on the homepage of dimplejs. Basically after
we load the data file, there's a callback function. From there we can
vary its parameter, including label, chart, or anything else.

Here the code snippet of DimpleJS used by Data Visualization course at
Udacity. After we get the data and svg constructed of D3, here what we
code:

    var myChart = new dimple.chart(svg, data);
    var x = myChart.addTimeAxis("x", "year"); 
    myChart.addMeasureAxis("y", "attendance");
    myChart.addSeries(null, dimple.plot.bar);
    myChart.draw(); 

First, myChart is the chart constructed by dimple, that takes the data,
from draw callback function of our data. SVG objects is the D3 SVG that
we constructed earlier. Next we add time axis act in x-axis that takes
"year" column from our data, as so y-axis takes "attendance" column from
our data. Next we assign the bar plot for our chart. Notice the null
here is actually how we facet our data. Do we need some addition 3rd
variable or not.Finally draw() will draw our chart into SVG that has
been appended into our html file.

We find some missing information here. Time is not directly placed, so
we want to change that.Bar plot may not be the best option, we may
change that also. Or maybe we want to add some layers, like Grammar of
Graphics said, so it has two layers consist of line and scatter. Here's
the code snipper looks like.

    var myChart = new dimple.chart(svg, data);
    var x = myChart.addTimeAxis("x", "year");
    x.dateParseFormat = "%Y";
    x.tickFormat = "%Y";
    x.timeInterval = 4;
    myChart.addMeasureAxis("y", "attendance");
    myChart.addSeries(null, dimple.plot.line);
    myChart.addSeries(null, dimple.plot.scatter);
    myChart.draw();

For Exploratory Data Analysis, you want to have an insights about your
data. You try to find the errors or outliers. You may want to find the
structure. Asking the right question about the data, visualize, and keep
your curiousity. In this case, the EDA is about yourself, iterating
data for yourself to keep getting valuable information.

Contrary to EDA, Sketchings want to find the best visual layout, or
visual encodings. The idea is you want to iterate all visual elements
related to your variables, to find the best way to reach others, your
audience.





> **RESOURCES**:

> * http://dimplejs.org/
> * https://www.udacity.com/course/viewer#!/c-ud507/l-3168988586/m-3063989007
