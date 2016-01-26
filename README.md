# Stimela

Tools for flexible and system independent (as much docker allows) radio interferometric simulations and reductions.
The main goal of this project is to test the feasibilty of using the AWS system to do SKA1-MID scale simulations and reductions. The simulations and reduction framework is largely based on [Pyxis](https://github.com/ska-sa/pyxis) and [Docker](https://www.docker.com/).

This project is funded by the [SKA/AWS Astrocompute in the cloud ](https://www.skatelescope.org/ska-aws-astrocompute-call-for-proposals) initiative. 

## Overview
This project is centred around two sets of docker images, i) *base images* have the required software tools installed in them, then ii) very light weight *executor images* are based on the *base* images and perform radio inteferometry related tasks like imaging, telescope simulations, and calibration. The base images can either be built locally or pulled from [docker hub](https://hub.docker.com/u/stimela), and the executor images must be built locally. Note that the (fairly heavy) base images have to be pulled/built very rarely.


**Base Images**
* base - This image has the [radio-satro ppa](https://launchpad.net/~radio-astro/+archive/ubuntu/main) installed, as well as standard packages such as git, python-pip etc.  
* casapy - This is a CASA image. [its huge](http://thepracticingcatholic.com/wp-content/uploads/2013/08/donald-trump-and-hedge-fund-manager-marc-lasry-will-launch-an-online-gambling-venture-once-its-legalized.jpg)
* lwimager - light weight imager based on casarest 
* wsclean - Imager
* casa - CASA package
* simms - tool to create empty visibility datasets
* meqtrees - MeqTrees
* autoflagger - Has automatic flagging tools instaleld (only has aoflagger for now)
* sourcery - Source finding image (based on lofar PyBDSM)



**Executor Images** (a.k.a **cab** images)
* simms - Creates visibility datasets
* simulator - Simulates a component sky mode into an MS
* predict - Simulates a FITS image sky model into an MS
* subtract - Subtracts a component sky model from an MS
* calibrator - Self-Calibrates an MS
* lwimager - Image an MS
* wsclean - Image an MS
* casa (clean task; imaging) - Image an MS
* sourcery - Runs a source-finder on a FITS image
* autoflagger - Automatically flags an MS
* flagms - Manually flags an MS

Each of these executor images has an execution script (generally a pyxis script) which performs the given task.




## Requires 
* [Docker](http://docs.docker.com/)
* Python

## Install
For a system wide install run (requires sudo powers) :
```
pip install stimela
```
Alternatively, you can do a local install by enbabling the `--user` flag
```
pip install stimela --user
```
This will install the binaries in `$HOME/.local/bin` and the python packages at `$HOME/.local/lib//python2.7/site-packages`. Finally, add these paths to your *PATH* and *PYTHONPATH* respectively. 
On my bash shell I add the following to `$HOME/.bashrc` (you do you):

```
export PATH=$PATH:$HOME/.local/bin
export PYTHONPATH=$PYTHONPATH:$HOME/.local/lib//python2.7/site-package
```

**Or**

Download the repo.
```
git clone https://github.com/SpheMakh/Stimela
```
Then install
```
cd Stimela
python setup.py install
```
Similarly, you can add the `--user` to `setup.py` flag to do a local install.

## Uninstall
```
pip uninstall stimela
```

## For Mac Users

**Prerequisites**
- install docker for Mac OS X (https://docs.docker.com/v1.8/installation/mac/)

- open a terminal and do the following commands:

```
docker-machine env default
eval "$(docker-machine env default)"
```

This will set up the default docker environment (report to the documentation for user specific environment settings)


Using docker on a Mac requires a particular setup and has some limitations
- Mac OS does not allow folders not owned by the host user to be mounted onto containers. So, on a Mac you have to do the local install. 

- Also, Casacore is known to have I/O issues when trying to read/write a file in a mounted volume on a Mac OS host (see Issue
[#5](https://github.com/SpheMakh/Recipepent/issues/5)).

So every I/O operation require additional data management to transfer the files in and out. If you are using a Mac you will have tell *stimela* that. Do this by enabling the `mac_os` flag in the *Recipe* instance when writing your *stimela* script. 

```
from otrera import Recipe
Recipe("The one pipeline to rule them all", ..., mac_os=True)
```

## Building *stimela* infrastructure
As mentioned earlier, *stimela* is based on Docker. And before you start scripting, you first need to either build or pull the neccessary Docker images (base images). To pull the images from the Docker hub:
```
stimela pull 
```
or build them locally
```
stimela -build-base
```

Then finally, build the executor images
```
stimela -build
```


See the [wiki](../../wiki/) for tutorials.
