# CPP Husky A200 Mapping

Review Status: Not Reviewed

## Introduction

This is document covers the mapping component that was outlined within [Cal Poly Pomona's Self Driving Husky A200](https://github.com/cpp-self-driving-husky/cpp-husky-a200-design-doc). Mapping serves the purpose of providing a representation or map of Cal Poly Pomona's campus that could be used for routing the best path for traversal. In addition, it provides an environment in which the Husky can localize and find out exactly where it is in map.

## User Stories

* As a user, I want to be able to easily address any physical environmental changes in Cal Poly Pomona's Campus.

## Requirements

* The mapping solution must accurately reflect the Cal Poly Pomona's campus in real time.
* The mapping solution must only depict Cal Poly Pomona's campus. Nothing more and nothing less.
* The mapping solution must depict traversable and non-traversable paths the Husky A200 can take.

## Solution

The solution that is being proposed is to use a static map that can be provided as a KML, Keyhole Markup Language, file from Google Maps and Google Earth. Cal Poly Pomona's campus doesn't change frequently, thus it is appropriate to use a static map instead of implementing a dynamic mapping service.

The KML file will then be translated into a graph that can used for finding the shortest path.

If the map of Cal Poly Pomona ever changes then the KML map can be updated to reflect that information.

Another bonus for using a KML file is that the same KML file can be used on the UI and can also be loaded by the Google Maps API.

## Reference

1. [Graph building based on Google Maps and Google Earth. Might need CPP internet access.](http://ieeexplore.ieee.org/document/7028728/)
2. [KML](https://developers.google.com/kml/)
3. [Google Map of Cal Poly Pomona](https://www.google.com/maps/d/u/0/viewer?mid=1RdxeCoUTop2E_mOp6rXrVYvnFDM&hl=en_US&ll=34.05797943205995%2C-117.82245283392047&z=17)
4. [Robotic Mapping](https://en.wikipedia.org/wiki/Robotic_mapping)
5. [How to export data from google earth](https://www.uvm.edu/~swac/docs/mod7/Exporting.pdf)