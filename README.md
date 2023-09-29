## Todos
- [] Refactoring
- [] Commenting
- [] Testfälle erstellen
  - [] Algos beschreiben (best/worst case, aufwandsabschätzung anhand der Testbeispiele), Deckblatt, Struktur inhaltsverzeichnis (Vorlage eines Labs von der FH), Seiten 3-5 (hat er aber offen gelassen), Testmessungen

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
  </ol>
</details>

# Convex Hull Algorithms

<!-- ABOUT THE PROJECT -->
## About The Project

The project aims to implement and visualize two different convex hull algorithms for 2D data: Quickhull and Giftwrapping. The primary objective is to compare the performance of these algorithms in terms of execution time and to provide interactive visualizations of the step-by-step convex hull construction.

## Convex Hull Algorithms:
The project focuses on two well-known convex hull algorithms:

* Quickhull: A divide-and-conquer algorithm known for its efficiency in finding the convex hull of a set of points in 2D. Example of the Algorithm:

https://github.com/eliasmarcon/Convex_Hull/assets/98773135/10d2c18a-7fb4-4aa3-b1f3-f0160ea19e97


* Giftwrapping (also known as Jarvis March): An iterative algorithm that constructs the convex hull by choosing points in a counter-clockwise manner. Example of the Algorithm:

https://github.com/eliasmarcon/Convex_Hull/assets/98773135/9f0eecef-16b2-436e-80de-b003796e2c5a


## Data Generation:
Two methods of generating input data for the algorithms are considered:

1. Randomly Generated Test Data: A set of 2D points with float values is generated randomly to create a dataset for convex hull computation. Example how do do this:

    * In order to generate/add test data you have to switch into the **additional_files** folder with the following command:
    
    ```sh
    cd additional_files      
    ```

    * If you are in the folder you can execute the following command:

    ```sh
    python performance_generation.py ["Giftwrapping", "Quickhull"] 300      
    ```

      the first argument has to be either ["Giftwrapping", "Quickhull"] in order to determine which CSV File should be updated. The second argument can be an integer in order to determine with how many points the test data should be generated. If you dont input an integer the programm will randomly choose a number of points which should be generated for the test case.



2. File Import with Simple File Format: Alternatively, users can import data from a file with a specific format:
      * The first line indicates the number of points, 'n'.
      * The subsequent 'n' lines contain 'x, y' comma-separated float values for each point.
      * Larger datasets are recommended for meaningful performance measurements.

    * In order to generate/add test data you have to switch into the **additional_files** folder with the following command:
    
    ```sh
    cd additional_files      
    ```

    * If you are in the folder you can execute the following command, you can also add an integer in order to determine how many random points should be generated (optional). If you dont input an integer it will randomly choose a number of points which should be generated:

    ```sh
    python generating_file_input.py 300 (Text file with 300 points would be generated)     
    ```

## Modes of Operation:
The project offers two modes of operation to cater to different user needs:

### Performance-Optimized Mode:

* This mode focuses on measuring and displaying the performance of both Quickhull and Giftwrapping algorithms.
* It provides printed results and precise time measurements for each algorithm's execution.

### Visual Mode:

* In this mode, users can interactively visualize the step-by-step construction of the convex hull using both algorithms.
* The visualization illustrates how the algorithms select points and build the convex hull incrementally, providing a deeper understanding of their inner workings.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Built With

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

3. Or open the Convex_Hull_App.bat file this will automatically install all requirements and open the main.py file

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

* For local usage, run the python script or the executable file. If you want to run the python script make sure you have installed the requirements txt as described above!
    ```sh
    python main.py
    ``` 

    or 

    ```sh
    open the executable file (here the requirements were installed automatically)
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




