# How to set up

You should have `docker` and `docker-compose`.

```bash
cd /home/user/git/AuthService
docker-compose up -d
```

# Tables creation 

```SQL
CREATE TABLE IF NOT EXISTS visitor_info(
id int auto_increment,
visit_time timestamp,
ip varchar(15),
value varchar(255),
userid int,
PRIMARY KEY id 
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS user(
id int auto_increment,
email varchar(100) UNIQUE,
password varchar(100),
name varchar(100),
PRIMARY KEY id
) ENGINE=INNODB;
```

# Usage examples

```bash
curl -X POST "localhost:80/register" -d "email=aaa@bbb.ru&password=123123&name=aaa"
curl -X POST "localhost:80/login" -d "email=aaa@bbb.ru&password=123123" -c cookies.txt
curl -X GET "localhost:80/test?key=some_value" -b cookies.txt
```