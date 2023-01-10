create table users(
    users_id varchar(20) primary key,
    user_email varchar(20),
    password varchar(20),
    user_name varchar(20),
    phone varchar(20),
    birth varchar(20),
    address varchar(20),
    job varchar(20),
    user_interests varchar(20),
    token varchar(20)
)charset = utf8;

create table posts(
    post_id int AUTO_INCREMENT primary key,
    title varchar(100),
    content varchar(1000),
    create_at datetime DEFAULT CURRENT_TIMESTAMP,
    updated_at datetime ON UPDATE CURRENT_TIMESTAMP
)charset = utf8;