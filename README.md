## Todos
- [x] Refactoring
- [x] Commenting
- [x] Variable Names
- [] Read ME
- [] Testprotokoll
- [] Testfälle erstellen
- [x] Design 


<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<h2 align="center">Advanced Programm Project: Convex Hull with Quickhull and Giftwrapping</h3>

  <p align="center">
    A Convex Hull Project where the algorithms Quickhull and Giftwrapping were implemented.
    <br />
    <a href="https://github.com/eliasmarcon/Convex_Hull/issues">Report Bug</a>
    ·
    <a href="https://github.com/eliasmarcon/Convex_Hull/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#convex-hull-algorithms">Convex Hull Algorithms</a></li>
    <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
  <li><a href="#computer-vision-tensor-serve-and-dash">Computer Vision Tensor Serve and Dash</a></li>
  </ol>
</details>

# Convex Hull Algorithms

<!-- ABOUT THE PROJECT -->
## About The Project

The project aims to implement and visualize two different convex hull algorithms for 2D data: Quickhull and Giftwrapping. The primary objective is to compare the performance of these algorithms in terms of execution time and to provide interactive visualizations of the step-by-step convex hull construction.

### Convex Hull Algorithms:
The project focuses on two well-known convex hull algorithms:

* Quickhull: A divide-and-conquer algorithm known for its efficiency in finding the convex hull of a set of points in 2D. Example of the Algorithm:

<video width="320" height="240" controls>
    <source src="videos/Quickhull.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>


* Giftwrapping (also known as Jarvis March): An iterative algorithm that constructs the convex hull by choosing points in a counter-clockwise manner. Example of the Algorithm:

<video width="320" height="240" controls>
    <source src="videos/Giftwrapping.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

### Data Generation:
Two methods of generating input data for the algorithms are considered:

1. Randomly Generated Test Data: A set of 2D points with float values is generated randomly to create a dataset for convex hull computation.
2. File Import with Simple File Format: Alternatively, users can import data from a file with a specific format:
    * The first line indicates the number of points, 'n'.
    * The subsequent 'n' lines contain 'x, y' comma-separated float values for each point.
    * Larger datasets are recommended for meaningful performance measurements.

### Modes of Operation:
The project offers two modes of operation to cater to different user needs:

### Performance-Optimized Mode:

* This mode focuses on measuring and displaying the performance of both Quickhull and Giftwrapping algorithms.
* It provides printed results and precise time measurements for each algorithm's execution.

### Visual Mode:

* In this mode, users can interactively visualize the step-by-step construction of the convex hull using both algorithms.
* The visualization illustrates how the algorithms select points and build the convex hull incrementally, providing a deeper understanding of their inner workings.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* Python
* Tkinter

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Installation

If you want to run the code locally, proceed with the following steps:

1. Clone the repo
   ```sh
   git clone https://github.com/eliasmarcon/Convex_Hull.git
   ```
2. Install Python packages
    ```sh
    pip install -r requirements.txt
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

* For local usage, run python script or the executable file, BUT first install the requirements!
    ```sh
    python main.py
    ``` 

    or 

    ```sh
    open the executable file
    ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

* https://github.com/eliasmarcon
* https://github.com/fasteiner
* https://github.com/hannah039


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [https://github.com/othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>




