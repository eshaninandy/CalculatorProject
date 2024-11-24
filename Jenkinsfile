pipeline {
    agent {
        label 'node-1'
    }
    environment {
        REPO_URL = 'https://github.com/eshaninandy/CalculatorProject/' // GitHub repository URL
        WORKSPACE_DIR = "/tmp/${JOB_NAME}-${BUILD_NUMBER}" // Unique workspace per job and build
    }
    stages {
        stage('Checkout Repository') {
            steps {
                script {
                    dir(WORKSPACE_DIR) { // Ensure unique workspace
                        echo "Checkout the repository from ${REPO_URL} into ${WORKSPACE_DIR}..."
                        sh '''
                        if [ -d "repo" ]; then
                        rm -rf repo
                        fi
                        git clone -b main ${REPO_URL} repo
                        '''
                    }
                }
            }
        }
        stage('Set up Virtual Environment') {
            steps {
                script {
                    dir(WORKSPACE_DIR) {
                        sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        '''
                    }
                }
            }
        }
        stage('Run Tests in Parallel') {
            parallel {
                stage('Addition Tests') {
                    steps {
                        script {
                            dir(WORKSPACE_DIR) {
                                sh '''
                                . venv/bin/activate
                                python -m unittest test_calc.TestCalculator.test_addition
                                '''
                            }
                        }
                    }
                }
                stage('Addition Loop Tests') {
                    steps {
                        script {
                            dir(WORKSPACE_DIR) {
                                sh '''
                                . venv/bin/activate
                                python -m unittest test_calc.TestCalculator.test_addition_loop
                                '''
                            }
                        }
                    }
                }
                stage('Subtraction Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_subtraction
                            '''
                        }
                        }
                    }
                }
                stage('Multiplication Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_multiplication
                            '''
                        }
                        }
                    }
                }
                stage('Division Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_division
                            '''
                        }
                        }
                    }
                }
                stage('Combined Operations') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_combined_operations
                            '''
                        }
                        }
                    }
                }
                stage('More Complex Expression') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_more_complex_expression
                            '''
                        }
                        }
                    }
                }
                stage('Square Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_square
                            '''
                        }
                        }
                    }
                }
                stage('Square Root Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_sqrt
                            '''
                        }
                        }
                    }
                }
                stage('Square Combined Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_square_combined
                            '''
                        }
                        }
                    }
                }
                stage('Square Root Combined Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_sqrt_combined
                            '''
                        }
                        }
                    }
                }
                stage('Square and Sqrt Loop Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_square_and_sqrt_loop
                            '''
                        }
                        }
                    }
                }
                stage('Complex Operations Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_complex_operations
                            '''
                        }
                        }
                    }
                }
                stage('Nested Operations Tests') {
                    steps {
                        script {
                        dir(WORKSPACE_DIR) {
                            sh '''
                            . venv/bin/activate
                            python -m unittest test_calc.TestCalculator.test_nested_operations
                            '''
                        }
                        }
                    }
                }
            }
        }
    }
}
