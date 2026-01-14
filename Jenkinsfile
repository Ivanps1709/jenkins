pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Análisis de Calidad (SonarQube)') {
            steps {
                script {
                    // Selecciona la herramienta que configuramos en Jenkins
                    def scannerHome = tool 'sonar-scanner'
                    
                    // Ejecuta el análisis enviándolo al servidor configurado
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=mi-app-python"
                    }
                }
            }
        }

        stage('Build & Deploy') {
            steps {
                // Aquí mantienes tus comandos de la Fase 2
                sh 'docker build -t mi-app-python .'
                sh 'docker stop contenedor-python || true && docker rm contenedor-python || true'
                sh 'docker run -d -p 5000:5000 --name contenedor-python mi-app-python'
            }
        }
    }
}
