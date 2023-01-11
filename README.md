# Unitem-Mower

Implementation Producer-Consumer Pattern using `threading.Thread` and a `queue.Queue` for Unitem test task

## General Information

### Producer Tasks
Producer (implemented as a thread) has a data source with size: width=1024px, height=768px, channels=3. In every 50ms a Producer takes new data from Source and puts them into a queue A

### Consumer Tasks
Consumer (implemented as a thread) takes available data from queue A and makes operations on the data:
- reduce the size of the image twice (final size is 2 times smaller)
- apply median filter with kernel 5x5 
After doing that, a new image is placed in queue B.

### Main function
Need to process 100 frames of data and stop the program after that. Also, data from queue B should be saved in a folder named "processed" in png format

### Implementation the Producer-Consumer Pattern
We have 4 approaches to solving this problem:
- One Producer and One Consumer
- One Producer and Multiple Consumers
- Multiple Producers and One Consumer
- Multiple Producers and Multiple Consumers

The last two probably violate the condition of the test task. So in this code implement "One Producer and One Consumer" approach. Also on branch `multi_consumer` implemented "One Producer and Multiple Consumers" approach but it did not give a big advantage in the time of the script execution. Tests was conducted for different numbers of Consumer threads from 2 to 10. 

## Setup
Clone the repo and install dependencies
```
$ git clone https://github.com/SystemDiagnosticss/Unitem-Mower
$ pip3 install -r requirements.txt
```

## Run 

1. Run application 
```
$ python3 main.py
```
Program will create 100 files in `processed` folder.

2. Run tests
```
$ pytest -s -v tests
```
