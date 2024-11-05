---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-04
---

<span style="color: gray;">Dated: 04-11-2024</span>

# Lecture No. 2

## Steps Involved in Statistical Research Project

- Topic and significance of the study
- Objective of your study
- Methodology for data collection
	- Source of your data
	- Sampling methodology
	- Instrument for collecting data

For the `study objective`, it should be clear that what is it we are trying to find out.  
For the `data collection`, we need to consider:

- Source of your data (the statistical population)
- Sampling Methodology
- Instrument for collecting data

## Collection of Data

This is the most important part of statistical work.  
There are two methods

### Complete Enumeration

This is also called `census`.  
It is the collection of whole field and is costly and time consuming because it requires a large number of enumerators and supervisory staff.

### Partial Enumeration

This is associated with a sample.

### Primary Data

The `data` which has been collected and has not gone into any statistical treatment is called `primary data`.

#### Collection of Primary Data

##### Direct Personal Investigation

The investigator personally interviews the people of concern and the data therefore, is considered accurate.  
It can be costly due to the vast area but is beneficial for laboratory experiments.  
`Errors` can be introduced due to personal bias of the investigator.

##### Indirect Investigation

It is adopted for extensive inquiries.  
The informants might hesitate to share information for any reason.  
Therefore, the people who have the information are interviewed.

##### Collection through Questionnaires

These are a list of inquiry questions with some space for the information.  
These are sent through email and are good for extensive inquiries because they are cheap.  
However, the down side is that the respondents don't really care and provide information that is either incomplete or full of errors.  
The questions should be brief and easy to understand.

##### Collection through Enumerators

This method involves trained enumerators assisting informants in accurately completing schedules or questionnaires.  
It provides the most reliable data when the enumerator is skilled and experienced.  
Ideal for large-scale government inquiries, it is typically too costly for private individuals or institutions.

##### Collection through Local Sources

This method relies on agents or local correspondents to gather and report information using their own judgment.  
It is cost-effective and quick but provides only estimates.

### Secondary Data

The `data` that have been collected, classified, tabulated or presented in some form for a certain purpose, are called `secondary` data.

#### Collection of Secondary Data

- Officials e.g. the publications of the Statistical Division, Ministry of Finance, the Federal and Provincial Bureaus of Statistics, Ministries of Food, Agriculture, Industry, Labour, etc.
- Semi-Official, e.g., State Bank of Pakistan, Railway Board, Central Cotton Committee, Boards of Economic Inquiry, District Councils, Municipalities, etc.
- Publications of Trade Associations, Chambers of Commerce, etc
- Technical and Trade Journals and Newspapers
- Research Organizations such as universities, and other institutions

## Sampling

Why sample? Because accessing the entire population is rare.  
Even annual `censuses` are impractical for most countries.  
Thus, we use samples to infer conclusions about larger populations.

### Population

A `statistical population` is a group sharing a characteristic, with variations among members.

#### Examples

##### Finite

- IQ's of all children in a school.

##### Infinite

- Barometric pressure
- A flight of migrating ducks in Canada

### Frame

The target population is all college students in Punjab, while the sampled population is students from five surveyed colleges.  
A clear definition of the population is crucial.  
To sample randomly from a finite population, we need a complete list of its elements, called the `frame`.

### Sampling Frame

A `sampling frame` is a complete list of all elements in a population, such as the BCS students of Virtual University of Pakistan on February 15, 2003.  
It should be free from defects, including inaccuracies, incompleteness, duplication, and outdated information.  
A sample, which is a part of the population, can represent it only to a limited extent; larger samples are more likely to reflect the population accurately.  
As sample size approaches population size, they become more identical.  
Statistical sampling aims to assess how accurately the sample describes the population, acknowledging potential compromises in accuracy while recognizing its value in data-based research.

#### Advantages of Sampling

1. Savings in time and money
	- Although unit costs are higher in a sample, total costs are lower due to the smaller sample size.
	- Sample surveys are quicker than full investigations, minimizing variations over time.
	- Fewer data points allow for faster and more precise processing and analysis.
2. More detailed information can be obtained from each sample unit.
3. Possibility of follow ups
	1. Queries and omissions can be addressed through follow-ups, which may not be possible in complete surveys.
4. Sampling is essential for destructive tests or when dealing with an effectively infinite population.

### Errors

#### Sampling Errors

It is the difference between the estimate derived from the `sample`(the statistic) and the true population value (the parameter).  
They arise because they cannot exactly represent the population.  

$$\text{Sampling error} = \overline X - \mu$$

#### Non Sampling Errors

In addition to sampling errors, non-sampling errors can occur during data collection, even in complete counts. Main sources of non-sampling errors include

- Defective sampling frames.
- Faulty reporting due to personal bias.
- Investigator negligence or indifference.
- Non-response to mail questionnaires.  

These errors can be minimized by

- Following up on non-responses.
- Providing proper investigator training.
- Correctly processing collected data.  

`Sampling errors` include partial non-response (respondent answers some questions) and total non-response (respondent answers none).  
Non-response issues are prevalent in human populations, especially in mail surveys, where response rates can drop to 15-20%.  
Providing information about the survey's purpose can boost interest and response rates, particularly if benefits for respondents are highlighted.

Sending a prepaid addressed envelope with the questionnaire can also encourage responses. Despite these efforts, some non-response is inevitable, necessitating decisions on the number of recalls, approaching respondents multiple times to secure answers.

Finally, it’s important to determine the duration of data collection; extending the survey over time increases the potential for variations in respondents' attitudes. A defined cut-off date is essential. The next step is to explore sampling methods, focusing on the distinction between non-random and random sampling.

##### Random Sampling

Statistical sampling theory assumes that sample units are selected randomly, typically using a lottery method for random sampling.

##### Types of Random Samples

- Simple Random Sampling
- Stratified Random Sampling
- Systematic Sampling
- Cluster Sampling
- Multi-stage Sampling, Etc

###### Simple Random Sampling

In this sampling method, every element of the parent population has an equal chance of being included in the sample, making simple random sampling equally likely for all samples.  
There is often confusion around random sampling, with haphazard selection mistakenly viewed as equivalent.  
For instance, a market researcher may stop women shoppers at random in a busy area, believing he is conducting simple random sampling.  
However, this approach can introduce bias, as he might preferentially question young, attractive women or those carrying brand X products.

Even without intentional bias, human selection is typically poor and subjective due to inherent psychological traits that hinder objectivity.  
While traditional random sampling involves drawing names from a hat, which can be cumbersome, a more efficient method is using random number tables.  
These tables contain digits from 0 to 9 arranged randomly, ensuring a lack of systematic patterns.

```
2315754859018372599376249708869523036744
0554555043105374350890611837441096221343
1487160350324043622350051003221154380834
3897674951940517585378805901943242871695
9731261718997553087094251258415488210513
1174269381443393087232797331182264706850
4336128859110164562393009004994364074036
9380620478382680449155751189325847552571
4954013181084298418769538296617773809527
3676872633379482156941959686704527483880
0709252392246271260706558453446733845320
4331001081448638030752555161488974294647
6157006360061736377563148951233501746993
3135283799107791894131579764486258486919
5704886526277959368290529565463506532254
0924344200687210713730729757360929827650
9795535018408948832952230825212253261587
9373259570437819888556671668269599644569
7262111225009226826435666594347168751867
6102074418453712079495917378669953619378
9783985474330559171845473541442203423000
8916097192222329063735055454898843816361
2596688220628717926502823528628491954883
8144331719050495480674690075676501716545
1132254931423623438608624976674224523245
```

These are generated according to certain mathematical principles so the each digit has the same chance of selection.

###### Example

The following frequency table of distribution gives the ages of a population of 1000 teen-age college students in a particular country.  
Select a sample of 10 students using the random numbers table. Find the sample mean age and compare with the population mean age.

| Age(X) | No. of Students (f) |
| ------ | ------------------- |
| 13     | 6                   |
| 14     | 61                  |
| 15     | 270                 |
| 16     | 491                 |
| 17     | 153                 |
| 18     | 15                  |
| 19     | 4                   |
|        | 1000                |

How will we proceed to select our sample of size 10 from this population of size 1000?

**Step 1**: Allocate a sampling number to each student.

| AGE | No. of Students (f) | Cumulative Frequency (cf) |
| --- | ------------------- | ------------------------- |
| 13  | 6                   | 6                         |
| 14  | 61                  | 67                        |
| 15  | 270                 | 337                       |
| 16  | 491                 | 828                       |
| 17  | 153                 | 981                       |
| 18  | 15                  | 996                       |
| 19  | 4                   | 1000                      |
|     | 1000                |                           |

| AGE | No. of Students (f) | Cumulative Frequency (cf) | Sampling Numbers |
| --- | ------------------- | ------------------------- | ---------------- |
| 13  | 6                   | 6                         | 000 – 005        |
| 14  | 61                  | 67                        | 006 – 066        |
| 15  | 270                 | 337                       | 067 – 336        |
| 16  | 491                 | 828                       | 337 – 827        |
| 17  | 153                 | 981                       | 828 – 980        |
| 18  | 15                  | 996                       | 981 – 995        |
| 19  | 4                   | 1000                      | 996 – 999        |
|     | 1000                |                           |                  |

The first student is assigned the sampling number 000, the second 001, and the last student (1000th) 999.  
This system uses three-digit numbers instead of four-digit ones for simplicity.  
To select 10 random numbers, one can close their eyes and let their finger point to a spot on the random number table, reading three adjacent digits.  
In this example, the random numbers selected are 041, 103, 374, 171, 508, 652, 880, 066, 715, 471, which correspond to ages: 14, 15, 16, 15, 16, 16, 17, 15, 16, 16.

###### Explanation

| Age(x) | No. of Students (f) | $f \times x$ |
| ------ | ------------------- | ------------ |
| 13     | 6                   | 78           |
| 14     | 61                  | 854          |
| 15     | 270                 | 4050         |
| 16     | 491                 | 7856         |
| 17     | 153                 | 2601         |
| 18     | 15                  | 270          |
| 19     | 4                   | 76           |
|        | 1000                | 15785        |

The `population mean` is  

$$\mu = \frac{\sum fx}{\sum f} = \frac{15785}{1000}$$

$$= 15.785 \text{ years}$$

Ages selected in the `sample` are

- 14
- 15
- 16
- 15
- 16
- 16
- 17
- 15
- 16
- 16

$$\text{Sample mean age} = 15.6$$

$$\text{Sampling Error} = \overline X - \mu$$

$$= 15.6 - 15.785$$

$$= -0.185 \text{ years}$$

The small error results from using the random sampling method, which increases the likelihood that the sample accurately represents the population.  
This means that estimates derived from the sample closely reflect those from the population, as a sample is meant to be a miniature replica of it.  
There are also various other types of random sampling.

###### Other Sampling Types

- Stratified sampling (if the population is heterogeneous)
- Systematic sampling (practically, more convenient than simple random sampling)
- Cluster sampling (sometimes the sampling units exist in natural clusters)
- Multi-stage sampling

All these designs utilize random or quasi-random sampling, which is a form of probability sampling where each unit has a known (but not equal) chance of selection.  
This allows for objective calculation of estimate precision and reliability.  
Typically, multiple sampling techniques are combined in survey designs, and simple random samples or multi-stage designs are seldom used without stratification.  
It's essential to exercise care at every step to ensure the reliability of the results.