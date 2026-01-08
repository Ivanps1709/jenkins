pipeline {
    agent any

    stages {
        stage('Copia de Seguridad/Limpieza') {
            steps {
                echo 'Limpiando contenedores antiguos...'
                // Detiene el contenedor anterior si existe para evitar conflictos de puerto
                sh 'docker stop mi-app-python-container || true'
                sh 'docker rm mi-app-python-container || true'
            }
        }

        stage('Build (Construir Imagen)') {
            steps {
                echo 'Construyendo la imagen de Docker...'
                sh 'docker build -t mi-app-python:latest .'
            }
        }

        stage('Test (Opcional)') {
            steps {
                echo 'Verificando que la imagen existe...'
                sh 'docker images | grep mi-app-python'
            }
        }

        stage('Deploy (Ejecutar)') {
            steps {
                echo 'Lanzando el contenedor...'
                sh 'docker run -d -p 5000:5000 --name mi-app-python-container mi-app-python:latest'
            }
        }
    }
}
