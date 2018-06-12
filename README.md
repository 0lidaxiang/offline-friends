# offline-friends
Design of Wearable Electronics Applications, CS3043701 course of NTUST in 2018.


## task

1. [x] read data from MCS and HTML5-GPS

2. [x] flush every minutes
3. [x] write the data into database
4. [x] read the data from database
5. [ ] compute GPS in one city
6. [ ] compyte stepFrequency of one user
7. [ ] front end pages

## library
```
sudo pip3 install mysqlclient
```

## database
```
source ./documents/database/version1.0.sql;
DROP TABLE user;
DELETE FROM user where id = 3;

INSERT INTO user  (nickname, age, gender, city, location, longitude, latitude, stepFrequency, heartBeat)    VALUES  ( "A2", "22", "0", "taipei", "daan", "","", "", "" );

INSERT INTO user  (nickname, age, gender, city, location, longitude, latitude, stepFrequency, heartBeat, stepStartTime, hobby)    VALUES  ( "A1", "24", "1", "taipei", "daan", "","", "", "" , "", "read novel, draw"), ( "A2", "22", "0", "taipei", "daan", "","", "", "" , "", "read novel");

UPDATE user SET gender='1' WHERE id= 4 ;
UPDATE user SET stepFrequency='1' WHERE nickname="A1";
UPDATE user SET heartBeat='1' WHERE nickname="A1";
```
