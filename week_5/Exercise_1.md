# Ex1 Use data from Danmarks Statistik - Databanken

1. Go to https://www.dst.dk/da/Statistik/	statistikbanken/api
2. Open 'Konsol' and click 'Start Konsol'
3. In the console at pt. 1: choose 'Retrieve tables' pt. 2: choose get request and json format and pt. 3: execute:
	1. check the result
	2. in the code below this same get request is used to get information about all available data tables in 'databanken'.
4. Change pt. 1 in the console to 'Retrieve data' pt 2: get request and Table id: 'FOLK1A', format: csv, delimiter: semicolon and click: 'Variable and value codes' and choose some sub categories (Hint: hover over the codes to see their meaning). Finally execute and see what data you get.
5. With data aggregation and data visualization answer the following questions:
	1. What is the change in pct of divorced danes from 2008 to 2020? **126,98 %** [Request here](https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Default&delimiter=Semicolon&civilstand=F&tid=2008K1%2C2020K1)
	2. Which of the 5 biggest cities has the highest percentage of 'Never Married'? **København = 412.512** [Request here](https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1&OMR%C3%85DE=851%2C101%2C630%2C751%2C461&CIVILSTAND=U)
	3. Show a bar chart of changes in marrital status in Copenhagen from 2008 till now. 
	4. Show a bar chart of 'Married' and 'Never Married' for all ages in DK (Hint: 2 bars of different color).