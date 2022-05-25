# Flask Application

This repository contains flask application code. We can deploy The entire stack - MySQL, Redis, and the backend application using docker swarm .
Once we execute this though docker stack deploy, it will create entire stack with four application replicas, Redis and MySQL database.
We can scale this web application by launching multiple backend application containers. 
          
    Backend application
        Model the following in the primary database
        i. Identifier
        ii. Name
        iii. Amount of gold 
    Application Endpoints
        a. Create player
            i. Store Identifier and Name in MySQL
            ii. Store Identifier and Gold in Redis
        b. Get player
            i. Retrieve Identifier and Name from the MySQL
            ii. Retrieve Gold from Redis 


## Table of Contents
    1. Getting started
    2. Local deployment
    3. Testing
### Getting started
#### Requirements
    Docker latest version should be installed in local machine.
#### Clone the repository 
    git clone https://github.com/navojha/docker-compose-flask-mysql-redis.git
    cd docker-compose-flask-mysql-redis

    $tree
     .   
    ├──Dockerfile
    ├──README.md
    ├──app.py
    ├──docker-compose.yml
    ├──requirements.txt
    └──templates
### Local deployment
     The entire stack - MySQL, Redis, and the backend application - will be deployable using docker swarn

    $docker-compose build

    $docker stack deploy -c docker-compose.yml mydeployment

    Creating network mydeployment_default
    Creating service mydeployment_app
    Creating service mydeployment_redis
    Creating service mydeployment_mysql


    $docker service ls

    ID             NAME                 MODE         REPLICAS   IMAGE                PORTS
    o9ws1rojddga   mydeployment_app     replicated   4/4        flask-redis:1.0      *:8083->8083/tcp
    t2ba9tbdqzcs   mydeployment_mysql   replicated   1/1        mysql:8.0            
    8if9cwkp02z8   mydeployment_redis   replicated   1/1        redis:6.2.7-alpine   

    $docker stack ps mydeployment

    ID             NAME                   IMAGE                NODE             DESIRED STATE   CURRENT STATE                ERROR     PORTS
    i1lqikc29tya   mydeployment_app.1     flask-redis:1.0      docker-desktop   Running         Running about a minute ago             
    o8crjgzsoqqo   mydeployment_app.2     flask-redis:1.0      docker-desktop   Running         Running about a minute ago             
    o2vpwhaninnf   mydeployment_app.3     flask-redis:1.0      docker-desktop   Running         Running about a minute ago             
    vad0irgl6weh   mydeployment_app.4     flask-redis:1.0      docker-desktop   Running         Running about a minute ago             
    wo8vyr5n7w3i   mydeployment_mysql.1   mysql:8.0            docker-desktop   Running         Running 44 seconds ago                 
    jl75g73wsi39   mydeployment_redis.1   redis:6.2.7-alpine   docker-desktop   Running         Running about a minute ago             

    $docker service scale mydeployment_app=20

    mydeployment_app scaled to 20
    overall progress: 20 out of 20 tasks 
    1/20: running   [==================================================>] 
    2/20: running   [==================================================>] 
    3/20: running   [==================================================>] 
    4/20: running   [==================================================>] 
    5/20: running   [==================================================>] 
    6/20: running   [==================================================>] 
    7/20: running   [==================================================>] 
    8/20: running   [==================================================>] 
    9/20: running   [==================================================>] 
    10/20: running   [==================================================>] 
    11/20: running   [==================================================>] 
    12/20: running   [==================================================>] 
    13/20: running   [==================================================>] 
    14/20: running   [==================================================>] 
    15/20: running   [==================================================>] 
    16/20: running   [==================================================>] 
    17/20: running   [==================================================>] 
    18/20: running   [==================================================>] 
    19/20: running   [==================================================>] 
    20/20: running   [==================================================>] 
    verify: Service converged 


### Testing
##### Create Player Table
localhost:8083
This will create the player table.
![VPC Created](https://github.com/navojha/docker-compose-flask-mysql-redis/blob/main/Screenshots/Table_Created.png?raw=true)

##### Insert records in Player
    localhost:8083/Createplayer
    This End Point will use to enter the Player data.
![VPC Created](https://github.com/navojha/docker-compose-flask-mysql-redis/blob/main/Screenshots/Create_player.png?raw=true)

#### Player Created
![VPC Created](https://github.com/navojha/docker-compose-flask-mysql-redis/blob/main/Screenshots/Player_created.png?raw=true)

#### Get Player Detail
    http://localhost:8083/Getplayer
    This endpoint will Retrieve Identifier and Name from the MySQL and Retrieve Gold from Redis. 
![VPC Created](https://github.com/navojha/docker-compose-flask-mysql-redis/blob/main/Screenshots/Get_Player.png?raw=true)
