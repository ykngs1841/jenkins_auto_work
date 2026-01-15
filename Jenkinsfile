pipeline {
    agent any

    environment {
        BUILD_DATE = new Date().format('yyMMdd')
        BUILD_FILE = "build_result_${BUILD_DATE}.txt"
        BUILD_DIR  = "build/${BUILD_DATE}_#${BUILD_NUMBER}"   
    }

    stages {

        stage('Build') {
            steps {
                echo "Building project on build_result_${BUILD_DATE}..."   

                sh '''
                docker run --rm \
                  -v "$WORKSPACE:/app" \
                  -w /app \
                  jenkins-build-env \
                  python build.py build/${BUILD_DATE}_#${BUILD_NUMBER}   
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'build/**', fingerprint: true
            }
        }
    }

    post {
        success {
            emailext (
                subject: "Jenkins Build SUCCESS: ${JOB_NAME} #${BUILD_NUMBER}",   
                body: """

The build completed successfully.

- Job: ${JOB_NAME}
- Build Number: ${BUILD_NUMBER}
- Build Date: ${BUILD_DATE}

The attached file is the output of this build.

                """,
                to: "kyungsuyoon09@gmail.com, ykngs1841@naver.com, ykngs1841@gmail.com",
                attachmentsPattern: "build/**/*.txt"   
            )
        }

        failure {
            emailext (
                subject: "Jenkins Build FAILED: ${JOB_NAME} #${BUILD_NUMBER}",   
                body: """
Build failed.
Check the Jenkins console log:
${BUILD_URL}
                """,
                to: "kyungsuyoon09@gmail.com, ykngs1841@naver.com, ykngs1841@gmail.com"
            )
        }
    }
}
