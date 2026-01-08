# jenkins_auto_work
PR 업로드시, Build 및 배포 자동화 목적으로 과제 진행 

GitHub
 └─ Jenkinsfile
 └─ build.py
 └─ src/main.cpp

Jenkins
 ├─ Stage: Build
 │    └─ python build.py
 ├─ Stage: Archive
 │    ├─ build/*.exe
 │    └─ build/*.txt
 └─ Post
      └─ Email Notification
