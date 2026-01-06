
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building project...'

                // 가짜 산출물 생성 (실무에선 빌드 결과물)
                bat '''
                GitHub -> Jenkins connection test > build_result.txt
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'build_result.txt', fingerprint: true
            }
        }
    }

    post {
        success {
            emailext (
                subject: "Jenkins Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
빌드가 성공적으로 완료되었습니다.

Job: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}

첨부된 파일은 이번 빌드의 산출물입니다.
""",
                to: "kyungsuyoon09@gmail.com",
                attachmentsPattern: "build_result.txt"
            )
        }

        failure {
            emailext (
                subject: "Jenkins Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "빌드가 실패했습니다. Jenkins 콘솔 로그를 확인하세요.",
                to: "kyungsuyoon09@gmail.com",
            )
        }
    }
}
