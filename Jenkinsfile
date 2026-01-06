
pipeline {
    agent any
    
    environment {
              BUILD_DATE = new Date().format('yyMMdd')
    }
    stages {

        stage('Build') {
            steps {
                echo 'Building project...'

                // 가짜 산출물 생성 (실무에선 빌드 결과물)
                bat '''
                echo Build result for Jenkins demo > build_result.txt
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
The build completed successfully.

Job: ${env.JOB_NAME}
Build Number: ${env.BUILD_NUMBER}

The attached files are the output of this build.
""",
                to: "kyungsuyoon09@gmail.com",
                attachmentsPattern: "build_result.txt"
            )
        }

        failure {
            emailext (
                subject: "Jenkins Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "Build failed. Check the Jenkins console log.",
                to: "kyungsuyoon09@gmail.com",
            )
        }
    }
} // test change
