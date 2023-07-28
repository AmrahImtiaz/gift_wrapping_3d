# Gift Wrapping in 3D space
This work represents an implementation of gift wrapping algorithm in 3 dimentional space, coded with python, a project for computational geometry course.
The result of this project is a 3D convex wrapping all the points in the space.


## Run Locally

Clone the project

```bash
  git clone https://github.com/moharastegaran/gift_wrapping_3d.git
```

Go to the project directory

```bash
  cd gift_wrapping_3d
```

Install dependencies

```bash
  pip install -e
```

Run the main python script

```bash
  python3 main.py
```

or for ease of use, you can open the project folder in pyCharm, VSCode, etc.


## Models
The core concept of the code stands on three classes:

* __Point__ : Mapping of every dot point in space into Point Model
* __Edge__ : A line connecting two Point samples, each line is identified with start & end points
* __Face__ : 3d illustration of convex hull, contains of Triangular planes, identified with points and edges.

Array of samples of __Face__ model outputs the result of the project, which is the covex wrapping the points.

## Results
There are two ways to scatter points in the space, random generation of points or manual user inputs, errors are handled in both ways.
The result will gradually update the convex and each triangular plane is added gradually with an interval to see the wrapping process clearly. Two sample outputs are added in the following:

| ![](https://github.com/moharastegaran/gift_wrapping_3d/blob/main/output/output_test_1.gif) | ![](https://github.com/moharastegaran/gift_wrapping_3d/blob/main/output/output_test_2.gif) |
