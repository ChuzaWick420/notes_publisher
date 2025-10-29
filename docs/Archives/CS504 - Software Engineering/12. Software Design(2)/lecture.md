---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Coupling and Cohesion

Less `coupling` means the different components have less reliance over each other, meaning they are more independent.  
More `coupling` means the opposite.

`Cohesion` means that the components have strong logical relation with each other.  
Meaning, a component should do exactly one thing.  
If the component contains parts which are not necessary to implement its functionality, then it is said to be less `cohesive`.

By making a strong `cohesive` component, it becomes more and more independent of other components, hence leading to less `coupling` on its own.  
So, there is a direct correlation between more `cohesion` and less `coupling`.

## Example of Coupling

**Example:** Take electric appliances of a house.  
All of them are encapsulated within their own bodies and do not rely on other appliances to function.  
Like a fan doesn’t rely on a fridge to function.

The components which communicate through `messages` tend to have less `coupling` as compared to the ones which use shared data (variables to maintain the state of program) have higher `coupling`.  
![[Pasted image 20240523182340.png]]

```cpp
class vector {
	public:
		float x;
		float y;
		vector (float x, float y);
		float getX();
		float getY();
		float getMagnitude();
		float getAngle();
};
```

Now imagine 2 functions which use this `class`.

```cpp
float myDotProduct1(vector a, vector b) {
	float temp1 = a.getX() * b.getX();
	float temp2 = a.getY() * b.getY();
	return temp1 + temp2;
}
```

```cpp
float myDotProduct2(vector a, vector b) {
	float temp1 = a.x * b.x;
	float temp2 = a.y * b.y;
	return temp1 + temp2;
}
```

The first one depends on the public `interface` the `class` provides. (less `coupling`)  
Meanwhile, the other one depends more on internal structure of the `class` itself. (more `coupling`)  
As soon as the internal structure of the `class` changes, the 2nd function will break.

## Example of Cohesion

A `class` is `cohesive` if most of its members access most of its data, most of the times.  
If there are certain groups of methods which manipulate a certain subset of data, then the `class` is less `cohesive` and should be broken down into multiple `classes`.  
![[Pasted image 20240523184620.png]]

```cpp
class order {

public:
	int getOrderID();
	date getOrderDate();
	float getTotalPrice();
	int getCustometId();
	string getCustomerName();
	string getCustometAddress();
	int getCustometPhone();
	void setOrderID(int oId);
	void setOrderDate(date oDate);
	void setTotalPrice(float tPrice);
	void setCustometId(int cId);
	void setCustomerName(string cName);
	void setCustometAddress(string cAddress);
	void setCustometPhone(int cPhone);
	void setCustomerFax(int cFax)

private:
	int oredrId;
	date orderDate;
	float totalPrice;
	item lineItems[20];
	int customerId;
	string customerName;
	int customerPhone;
	int customerFax;
};
```

Look at this `class`, it contains data regarding `order` and `customer`.  
It is less `cohesive` for this very reason.  
Hence it should be broken down into 2 `classes` as follows.

```cpp
class order {

public:
	int getOrderID();
	date getOrderDate();
	float getTotalPrice();
	int getCustometId();
	void setOrderID(int oId);
	void setOrderDate(date oDate);
	void setTotalPrice(float tPrice);
	void setCustometId(int cId);
	void addLineItem(item anItem);

private:
	int oredrId;
	date orderDate;
	float totalPrice;
	item lineItems[20];
	int customerId;
};

```

```cpp
class customer {

public:
	int getCustometId();
	string getCustomerName();
	string getCustometAddress();
	int getCustometPhone();
	int getCustomerFax();
	void setCustometId(int cId);
	void setCustomerName(string cName);
	void setCustometAddress(string cAddress);
	void setCustometPhone(int cPhone);
	void setCustomerFax(int cFax)

private:
	int customerId;
	string customerName;
	int customerPhone;
	int customerFax;
};
```

## Abstraction and Encapsulation

`Abstraction` is a special case of `separation of concern` where we hide the inner complexities of the `class` through `encapsulation` and focus mostly on the external `interface` it provides.

Consider,

```cpp
void selectionSort(int a[], int size) {
	int i, j, min, temp;
	
	for(i = 0; i < size –1; i++) {
		min = i;
		
		for (j = i; j < size; j++) {
			if (a[j] < a[min])
				min = j;
		}
		
		temp = a[i];
		a[i] = a[min];
		a[min] = temp;
	}
}
```

We can chop this down into different auxiliary functions, such as:

```cpp
void swap(int &x, int &y) {
	int temp;
	temp = x;
	x = y;
	y = temp;
}
```

```cpp
int indexOfMinimumValue(int a[], int from, int to) {
	int i, min;
	min = from;
	
	for (i = from+1; i < to; i++)
		if (a[i] < a[min]) min = i;
	
	return min;
}
```

Then we can combine them together into the main function.

```cpp
void selectionSort(int a[], int size) {
	int i, min;
	
	for (i = 0; i < size; i++) {
		min = indexOfMinimumValue(a, i, size);
		swap(a[i], a[min]);
	}
}
```

Not only that our code is more readable now, but it has produced 2 auxiliary functions which are generic in nature and can be re-used elsewhere.

## Function Oriented Vs Object Oriented

In the #functional-programming design, the decomposition revolves around #function .  
On the other hand, in #object-oriented-programming design, the decomposition revolves around `data`.

Problem with #functional-programming is that the side effects of functions are not localized.  
Any function can access any data from anywhere.  
This makes it very hard to figure out from _where_ the data is being manipulated.

On the other end, #object-oriented-programming solves this problem by localizing the data and the functions which manipulate it, together.  
This localizes the side effects and are easier to look into.
