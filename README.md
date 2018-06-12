# offline-friends
Design of Wearable Electronics Applications, CS3043701 course of NTUST in 2018.


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
INSERT INTO user  (nickname, age, gender, city, location, longitude, latitude, stepFrequency, heartBeat, stepStartTime)    VALUES  ( "A1", "24", "1", "taipei", "daan", "","", "", "" , ""), ( "A2", "22", "0", "taipei", "daan", "","", "", "" , "");

UPDATE user SET gender='1' WHERE id= 4 ;
UPDATE user SET stepFrequency='1' WHERE nickname="A1";
UPDATE user SET heartBeat='1' WHERE nickname="A1";
```
