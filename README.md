# MyTranslation


🔗[My Translation](https://qmffnxod.store/)
- 번역 작업 및 관리 툴
- Main Page
![](https://user-images.githubusercontent.com/104023868/227980816-1246c98a-6c2b-4f03-924b-9bec38f17b48.png)

##### 🚩 프로젝트 목적
- 글로서리에 단어 중복 등록으로 인한 오탈자 발생 및 번역-검수 시 엑셀파일을 주고 받는 불편함을 개선
- 번역 작업의 편리성과 효율성을 향상

##### 📌 주요기능
- 로그인
  - OAuth2.0 구글 로그인인
- 번역 프로젝트 등록
  - 업로드 할 엑셀 파일은 [num/remark/원본데이터] 세 가지 칼럼으로 구성
  - S3 업로드 - DB 저장
- 번역, 체크 작업
  - 한일 번역 시 파파고API로 번역문 호출
  - 번역 데이터 페이지 네이션
  - 자동저장 (로컬스토리지에 임시저장 후 10초 마다 저장)
- 글로서리 등록
  - 카테고리 별 단어 등록
  - 글로서리에 등록된 단어 Marker표시
- 검수 완료 시 담당 작가에게 메일 발송

##### 📌 기술 스택 및 사용 라이브러리
- Backend
![React](https://img.shields.io/badge/Python-white?style=flat&logo=Python&logoColor=3776A) ![React](https://img.shields.io/badge/Django-white?style=flat&logo=Django&logoColor=092E20) ![React](https://img.shields.io/badge/DjangoRestFramework-white?style=flat&logo=djangorestframework&logoColor=092E20) ![React](https://img.shields.io/badge/MySQL-white?style=flat&logo=Mysql&logoColor=4479A1) ![React](https://img.shields.io/badge/S3-white?style=flat&logo=amazons3&logoColor=569A31) 
![React](https://img.shields.io/badge/Celery-white?style=flat&logo=celery&logoColor=37814A) ![React](https://img.shields.io/badge/Scrapy-white?style=flat&logo=scrapy&logoColor=499848) 

- Frontend
![React](https://img.shields.io/badge/Javascript-white?style=flat&logo=javascript&logoColor=F7DF1E) ![React](https://img.shields.io/badge/React-white?style=flat&logo=react&logoColor=61DAFB) ![React](https://img.shields.io/badge/CloudFront-white?style=flat&logo=amazonaws&logoColor=232F3E) ![React](https://img.shields.io/badge/GihubActions-white?style=flat&logo=githubactions&logoColor=2088FF)
![React](https://img.shields.io/badge/ChakraUI-white?style=flat&logo=chakraui&logoColor=319795) ![React](https://img.shields.io/badge/ReactQuery-white?style=flat&logo=reactquery&logoColor=FF4154) ![React](https://img.shields.io/badge/ReactHookForn-white?style=flat&logo=reacthookform&logoColor=EC5990) ![React](https://img.shields.io/badge/ReactMarker-white?style=flat&logo=reactmarker&logoColor=EC5990) 

- Deployment
![React](https://img.shields.io/badge/Docker-white?style=flat&logo=docker&logoColor=2496ED) ![React](https://img.shields.io/badge/EC2-white?style=flat&logo=amazonec2&logoColor=FF9900) ![React](https://img.shields.io/badge/RDS-white?style=flat&logo=amazonrds&logoColor=527FFF) ![React](https://img.shields.io/badge/Nginx-white?style=flat&logo=nginx&logoColor=009639) ![React](https://img.shields.io/badge/Gunicorn-white?style=flat&logo=gunicorn&logoColor=499848)

##### 📌 페이지 캡처
- 번역 프로젝트 작업 화면
![](https://user-images.githubusercontent.com/104023868/227997001-0e7344fe-fad6-479a-a7bc-065ecbf4c0d7.png)

- 글로서리 단어 등록
![](https://user-images.githubusercontent.com/104023868/227997438-c68367ba-1668-4e55-829c-aa090de43930.png)

- 글로서리 등록 단어 Marker
![](https://user-images.githubusercontent.com/104023868/227997887-97eb84ac-25b5-43d7-9983-a6759b1544f5.png)
![](https://user-images.githubusercontent.com/104023868/227997935-88fe6c21-9230-46c1-91a4-6ab16d2fecd9.png)
