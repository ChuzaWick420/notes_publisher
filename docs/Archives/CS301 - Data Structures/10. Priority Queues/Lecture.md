---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Simulation
There are 2 types of `simulation` models.
1. Time-based simulation.
2. Event-based simulation.

In `time` based simulation, we maintain a clock for things (or events) to happen.  
In `event` based simulation, we maintain a list of events along with their computed times in increasing order. We do not wait for the clock to tick till the next event.

# Priority Queue
a #queue where the `de-queue` operation does not depends on the #FIFO but rather depends on the events with their time required for completion, is called #priority-queue.

Imagine a file with following data:

```
00 30 10
00 35 05
00 40 08
00 45 02
00 50 05
00 55 12
01 00 13
01 01 09
```

Where the first column represents _hours_, 2nd represents _minutes_ and 3rd represents _time required for transaction_. (Example of 4 queues in front of 4 tellers in a bank).

```cpp
#include <iostream>
#include <string>
#include <strstream.h>

#include "Customer.cpp"
#include "Queue.h"
#include "PriorityQueue.cpp"
#include "Event.cpp"

Queue q[4];       // teller queues
PriorityQueue pq; //eventList;
int totalTime;
int count = 0;
int customerNo = 0;

int main (int argc, char *argv[]) {
	Customer* c;
	Event* nextEvent;
	// open customer arrival file
	ifstream data("customer.dat", ios::in);
	// initialize with the first arriving customer.
	ReadNewCustomer(data);
	
	while( pq.length() > 0 ) {
		
		nextEvent = pq.remove();
		c = nextEvent->getCustomer();
		
		if( c->getStatus() == -1 ){  // arrival event
			int arrTime = nextEvent->getEventTime();
			int duration = c->getTransactionDuration();
			int customerNo = c->getCustomerNumber();
			processArrival(data, customerNo, arrTime, duration , nextEvent);
		}
		
		else{  // departure event
			int qindex = c->getStatus();
			int departTime = nextEvent->getEventTime();
			processDeparture(qindex, departTime, nextEvent);
		}
	}
}
```

Some of the functions used:

```cpp
void readNewCustomer(ifstream& data) {
	int hour,min,duration;
	
	if (data >> hour >> min >> duration) {
		customerNo++;
		Customer* c = new Customer(customerNo, hour*60+min, duration);
		c->setStatus( -1 ); // new arrival
		Event* e = new Event(c, hour*60+min );
		pq.insert( e ); // insert the arrival event
	}
	
	else {
		data.close(); // close customer file
	}
}
```

```cpp
int processArrival(ifstream &data, int customerNo, int arrTime, int duration, Event* event) {
	int i, small, j = 0;
	// find smallest teller queue
	small = q[0].length();
	for(i=1; i < 4; i++ )
		if( q[i].length() < small )
			small = q[i].length(); j = i;
	
	// put arriving customer in smallest queue
	Customer* c = new Customer(customerNo, arrTime, duration );
	c->setStatus(j);  // remember which queue the customer goes in
	q[j].enqueue(c);
	
	// check if this is the only customer in the.
	// queue. If so, the customer must be marked for
	// departure by placing him on the event queue.
	if( q[j].length() == 1 ) {
		c->setDepartureTime( arrTime+duration);
		Event* e = new Event(c, arrTime+duration );
		pq.insert(e);
	}
	
	// get another customer from the input
	readNewCustomer(data);
}
```

```cpp
int processDeparture(int qindex, int departTime, Event* event) {
	Customer* cinq = q[qindex].dequeue();
	int waitTime = departTime - cinq->getArrivalTime();
	totalTime = totalTime + waitTime;
	count = count + 1;
	
	// if there are any more customers on the queue, mark the
	// next customer at the head of the queue for departure
	// and place him on the eventList.
	if( q[qindex].length() > 0 ) {
		cinq = q[qindex].front();
		int etime = departTime + cinq->getTransactionDuration();
		Event* e = new Event(cinq, etime);
		pq.insert( e );
	}
}
```
