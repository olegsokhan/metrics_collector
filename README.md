# OS metrics collector

This script prints basic info about CPU and memory

## Installation

metrics.py uses python 3.6.5

To use metrics.py script you should install psutil

https://github.com/giampaolo/psutil/blob/master/INSTALL.rst

mitrics.py script support cpu and mem parameters

```
python metrics.py mem
```

```
python metrics.py cpu
```

### Running in Docker container

To build docker image use next command
Current directory should be with metrics.py script and Dockerfile

```
docker build -t metrics ./
```

Then run script

```
docker run metrics mem
```

```
docker run metrics cpu
```

#### Authors

Oleg Sokhan