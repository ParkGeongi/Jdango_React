insert into users(users_id, user_email, password, user_name, phone, birth,
                address, job, user_interests)
values ('1', 'hong@test.com', '1', '장순이', '010-1224-5678', '2000-01-01',
                '서울시 도봉구', '개발자', '영화');

insert into users(users_id, user_email, password, user_name, phone, birth,
                address, job, user_interests)
values ('2', 'mang@test.com', '1', '마아니', '010-8462-1568', '2002-08-16',
                '서울시 강남구', '사업가', '게임');


insert into posts(title, content)

values ('RNN과 LSTM을 이해해보자', '이번 포스팅에서는 Recurrent Neural Networks(RNN)과
                        RNN의 일종인 Long Short-Term Memory models(LSTM)에 대해 알아보도록 하겠습니다.');

insert into posts(title, content)

values ('GAN의 개념과 이해', '지난 아티클에서 소개했던 지도학습은 인공지능 기술의 폭발적인 발전을 선도해왔습니다.
        하지만, 모든 데이터에 대한 정답을 개발자가 알려줘야 학습이 가능하다는 특징 때문에 소요 시간 및 리소스의 한계라는
        단점이 있고 궁극적으로 인공지능이 가야 할 방향과도 다소 거리가 있습니다.');
