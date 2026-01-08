pipeline {
    agent any

    environment {
        BUILD_DATE = new Date().format('yyMMdd') 
        BUILD_FILE = "build_result_${BUILD_DATE}.txt" 
    } //Build 변수 선언 및 파일 적용

    stages {

        stage('Build') {
            steps {
                echo "Building project on ${env.BUILD_DATE}..."

                bat """
                "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" build.py
                """
            }
        } // 추후 배포 패키지 파일로 대체

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            } // Build 산출물 저장
        }
    }

    post {
        success {
            emailext (
                subject: "Jenkins Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """

                       The build completed successfully.

                       Job: ${env.JOB_NAME}
                       Build Number: ${env.BUILD_NUMBER}
                       Build Date: ${env.BUILD_DATE}
                       
                       The attached file is the output of this build.

                        """,
                to: "kyungsuyoon09@gmail.com, ykngs1841@naver.com, ykngs1841@gmail.com",
                attachmentsPattern: "${env.BUILD_FILE}"
            )
        }

        failure {
            emailext (
                subject: "Jenkins Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                         Build failed. 
                         Check the Jenkins console log: ${env.BUILD_URL}
                     """,
                to: "kyungsuyoon09@gmail.com, ykngs1841@naver.com, ykngs1841@gmail.com"
            )
        }
    }
}
