# Full Pipeline construction on the Cloud to determinate the best location for e-scooters based on weather and crowds predictions. 
Gans (e-scooters renting company) has seen that its operational success depends on having a good prediction of their e-scooters parked where users need them. This project task will be to collect data from external sources that can potentially help Gans predict e-scooter movement by creating the all automated system in the cloud. 


## 1. Project Description
Ideally, scooters get rearranged organically by having certain users moving from point A to point B, and then an even number of users moving from point B to point A. There are some elements that create asymmetries. Here are some of them:

- Weather conditions, for example: Whenever it starts raining, e-scooter usage decreases drastically.
- Increment of people's trafic in specific area and hours of the city, for example: airplanes with back-pack young tourists lands, a lot of scooters are needed close to the airport.

There are some actions that the company can perform to solve these asymmetries, namely:

- Use a truck to move scooters around.
- Create economic incentives for users to pick or leave scooters in certain areas, like the images below shows.:


## **Objectives**
Since data is needed every day, in real time and accessible by everyone in the company, the challenge is going to be to assemble and automate a data pipeline in the cloud. to achieve this task was required the following:

1) Python scripts for data collection from different APIs sources
2) Create a relational data base (DB) from scratch using MySQL into AWS Cloud Compute Service (RDS)
3) Automate the data collection to the DB using the AWS Lambda funtions



## ***Project Summary***
The all Data Engineering Pipeline is now running in the Cloud:

* Initial cities and airports dataframe was collected in CSV files
* Data Base was created in the cloud (RDS) and initial dataframes updated
* weather and flights dataframes are running and automaticatly updating in the cloud (Lambda) 


Now that the weather & flights prediction is available in the database, updating in real time and accessible by everyone, it will be easy to make a good prediction of the right place and time of the day to locate the e-scooters and provide a valueable insights for Gans company.

## ***For more detailed information***

check the jupyther notebook or index.html file attached in the Documentation folder.
