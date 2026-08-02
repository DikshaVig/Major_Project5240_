-- Create Database
Create database CustomerSegmentationDB;
-- Select Database
USE CustomerSegmentationDB;

-- Display Database
SHOW databases;
 
 CREATE TABLE customers (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    AnnualIncome INT,
    SpendingScore INT
);

DESC customers;
 
SELECT * FROM customers;

SELECT COUNT(*)
FROM customers;

CREATE TABLE prediction_history (
PredictionID INT AUTO_INCREMENT PRIMARY KEY,
Gender VARCHAR(10),
Age INT,
AnnualIncome INT,
SpendingScore INT,
PredictedCluster VARCHAR(100),
PredictionDate DATETIME DEFAULT CURRENT_TIMESTAMP
);

DESC prediction_history;

CREATE TABLE clusters (
ClusterID INT PRIMARY KEY,
ClusterName VARCHAR(100),
Description TEXT,
Recommendation TEXT
);

INSERT INTO clusters VALUES
(0,
'Budget Customers',
'Low income and low spending',
'Offer discounts and cashback'),

(1,
'Premium Customers',
'High income and high spending',
'Provide VIP membership'),

(2,
'Regular Customers',
'Average income and spending',
'Promote seasonal offers'),

(3,
'High Potential Customers',
'High income but low spending',
'Recommend premium products'),

(4,
'Careful Customers',
'Low income but high spending',
'Offer loyalty rewards');

SELECT * FROM clusters;

CREATE TABLE model_results (
Algorithm VARCHAR(100),
SilhouetteScore FLOAT,
DaviesBouldin FLOAT,
CalinskiHarabasz FLOAT,
SelectedModel VARCHAR(10)
);

INSERT INTO model_results VALUES
('KMeans',0.78,0.45,350,'YES'),
('Agglomerative',0.74,0.51,320,'NO'),
('DBSCAN',0.60,0.82,210,'NO'),
('GMM',0.76,0.49,340,'NO');

SELECT * FROM model_results;

SELECT COUNT(*)
FROM customers;

SELECT AVG(Age) FROM customers;

SELECT AVG(AnnualIncome) FROM customers;

SELECT AVG(SpendingScore) FROM customers;

SELECT COUNT(*) FROM customers WHERE Gender='Male';

SELECT COUNT(*) FROM customers WHERE Gender='Female';

SELECT * FROM customers WHERE AnnualIncome>80;

SELECT * FROM customers WHERE SpendingScore>80;

SELECT * FROM customers WHERE Age<30;

SELECT * FROM customers WHERE Age>50;

SELECT * FROM prediction_history;

SELECT * FROM prediction_history ORDER BY PredictionID DESC LIMIT 1;

DELETE FROM prediction_history;

SELECT COUNT(*) FROM prediction_history;

SELECT PredictedCluster,COUNT(*) AS TotalPredictions
FROM prediction_history
GROUP BY PredictedCluster ORDER BY TotalPredictions DESC;
SELECT * FROM model_results WHERE SelectedModel='YES';
SELECT * FROM model_results ORDER BY SilhouetteScore DESC LIMIT 1;
SELECT * FROM model_results ORDER BY SilhouetteScore DESC LIMIT 1;
SELECT * FROM model_results ORDER BY DaviesBouldin ASC LIMIT 1;
SELECT * FROM clusters WHERE ClusterID=3;
