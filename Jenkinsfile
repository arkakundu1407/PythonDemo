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
        stage('Unit Testing') {
      steps{
        script { 
          sh 'python /var/jenkins_home/workspace/webapp-python-project/posts/tests.py'
        }
         
      }
    } 
       stage("SonarQube Code Analysis"){
          steps{
           sh 'rm -rf scanlatest.html'
            sh "/opt/sonar/bin/sonar-scanner \
  -Dsonar.projectKey=webapp-python \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://13.71.84.138:9000 \
  -Dsonar.login=874439216ca48df33aaddfb5b7e1b06219329746"
         
             //error('Pipeline failed due to SonarQube quality test failures')
          }
       }
     stage('Building image') {
      steps{
        script {
          //will pisck registry from variable defined
          //dockerImage = docker.build registry + ":$BUILD_NUMBER"
          dockerImage = docker.build registry
           //sh 'sed "s/latest/$BUILD_NUMBER/g" Application.yml > Application1.yml'
           //sh 'mv Application1.yml Application.yml'
        }
      }
    }

       
      stage('Pushing Image to DockerHub') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
 
        stage('Aqua Security Image Scanner') {
        steps{
           
           aquaMicroscanner imageName:'arkakundu1407/docker-pipeline:latest' , notCompliesCmd: 'exit 1', onDisallowed: 'fail', outputFormat: 'html'
           
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
       
       
           
    stage('Lynis Server Hardening') {
      steps {
         
        sh 'git clone https://github.com/CISOfy/lynis'
         sh 'rm -rf /usr/local/lynis'
        sh 'mv lynis /usr/local/'
         sh 'chown -R root:root /usr/local/lynis'
         sh '/usr/local/lynis/lynis audit system > /var/jenkins_home/workspace/webapp-python-project/hardening-output.txt'
         step([$class: 'ArtifactArchiver', artifacts: 'hardening-output.txt'])
      }
    }
   /* stage('Remove Unused docker image') {
      steps{
        sh "docker rmi -f $registry:$BUILD_NUMBER"
      }
    }*/
stage ('Deploying Application to AKS Cluster') {
       steps {
           kubernetesDeploy(
               kubeconfigId : 'kubeconfig',
               configs : 'Application.yml',
               enableConfigSubstitution : false
           )
       }
     }
              stage('Arachni Security Scanner') {
         steps {
             
            arachniScanner checks: '*', scope: [pageLimit: 3], url: 'http://13.71.114.235:80/posts/', userConfig: [filename: 'myConfiguration.json'], format: 'json'            
            sh "unzip arachni-report-json.zip arachni-report.json"
            step([$class: 'ArtifactArchiver', artifacts: 'arachni-report.json'])
         }
      }

 }
}
