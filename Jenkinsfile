pipeline{
  agent any
  stages {
          stage('执行Python脚本') {
                                  steps {
                                          bat 'python main.py'
                                          // One or more steps need to be included within the steps block.
                                        }
                                  }
          }
  post {
        always {
                emailext body: '嘻嘻嘻嘻嘻嘻', subject: '流水线测试', to: '798864699@qq.com'
    // One or more steps need to be included within each condition's block.
                }
        }

  }
