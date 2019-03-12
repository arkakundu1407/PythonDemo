pipeline {
   environment {
    registry = "arkakundu1407/docker-pipeline"
    registryCredential = 'dockerhub'
    dockerImage = ''
    containerId = sh(script: 'docker ps -aqf "name=java-app"', returnStdout: true) //to store your container id , so that it can be deleted
  }
  agent any
    stages 
    {
        stage('Building image') {
      steps{
        script {
          //will pisck registry from variable defined
          //dockerImage = docker.build registry + ":$BUILD_NUMBER"
           dockerImage = docker.build registry
        }
      }
    }
     
       stage('Push Image') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
     
       stage('Aqua MicroScanner') {
        steps{
       aquaMicroscanner imageName:'arkakundu1407/docker-pipeline:latest', notCompliesCmd: 'exit 1', onDisallowed: 'fail', outputFormat: 'html'
       
        }
    }
       
       stage("Sonar scanner"){
          steps{
       
            sh "/opt/sonar/bin/sonar-scanner \
  -Dsonar.projectKey=webapp \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://52.172.31.38:9000 \
  -Dsonar.login=af8120918acf2a231c35e9d7c2e7317b3f82156e"
         
          }
       }
      /*stage('Cleanup') {
      when {
                not { environment ignoreCase: true, name: 'containerId', value: '' }
        }
      steps {
        sh 'docker stop ${containerId}'
        sh 'docker rm ${containerId}'
      }
    }*/
       
       
             
    stage('Server Hardening') {
      steps {
         
        sh 'git clone https://github.com/CISOfy/lynis'
        sh 'mv lynis /usr/local/'
         sh 'chown -R root:root /usr/local/lynis'
         sh '/usr/local/lynis/lynis audit system'
      }
    }
    /*stage('Remove Unused docker image') {
      steps{
        sh "docker rmi -f $registry:$BUILD_NUMBER"
      }
    }*/
stage ('Deploy application') {
       steps {
           kubernetesDeploy(
               kubeconfigId : 'kubeconfig',
               configs : 'Application.yml',
               enableConfigSubstitution : false
           )
       }
     }

 }
}
