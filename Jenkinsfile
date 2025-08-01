pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = 'graphical-quest-467400-h7'
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }



    stages {
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github Repo to Jenkins'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/sohaibchachar/MLOPS_Project_HotelReservation']])
                }
            }
        }


        stage('Setting up our Virtual Environment and Installing dependancies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependancies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }



        stage('Building and pushing docker image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and pushing docker image to GCR'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/mlops-project1-hotelreservation:latest .

                        docker push gcr.io/${GCP_PROJECT}/mlops-project1-hotelreservation:latest
                        '''
                    }
                }

            }
        }


        stage('Deploying to Google Cloud Run'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key' , variable : 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Deploying to Google Cloud Run'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud run deploy mlops-project1-hotelreservation \
                            --image=gcr.io/${GCP_PROJECT}/mlops-project1-hotelreservation:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow=unauthenticated
                        '''
                    }
                }

            }
        }
    }
}