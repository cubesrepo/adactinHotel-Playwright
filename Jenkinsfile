pipeline{
    agent any

    environment{
        VENV_DIR = "${WORKSPACE}/venv"
        PYTHON_BIN = "/Users/leonardacube/PycharmProjects/saucedemo-Playwright/.venv/bin/python3.14"
    }
    stages{
        stage('Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/cubesrepo/adactinHotel-Playwright.git'
            }
        }
        stage('Install dependencies'){
            steps{
                sh '''
                    ${PYTHON_BIN} -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install -r utilities/requirements.txt
                    playwright install
                '''
            }
        }
        stage('Run playwright tests'){
            steps{
                sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest -v --alluredir-reports/allure-results
                '''
            }
        }
    }
    post{
        always{
            echo "Generating allure report"
            steps([$class: 'AllureReportPublisher',
                results: [[path: 'reports/allure-results']],
                includeProperties: false,
                jdk: ''
            ])
            echo "Cleaning up workspace"
            cleanWsc()
        }
        success{
            echo "Test passed successfully"
        }
        failure{
            echo "Test failed!"
        }
    }
}