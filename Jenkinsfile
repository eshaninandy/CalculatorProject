pipeline {
    agent {
        label 'node-1'
    }
    stages {
        stage('Set up Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                '''
            }
        }
        stage('Run Tests in Parallel') {
            parallel {
                stage('Addition Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_addition
                        '''
                    }
                }
                stage('Addition Loop Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_addition_loop
                        '''
                    }
                }
                stage('Subtraction Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_subtraction
                        '''
                    }
                }
                stage('Multiplication Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_multiplication
                        '''
                    }
                }
                stage('Division Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_division
                        '''
                    }
                }
                stage('Combined Operations') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_combined_operations
                        '''
                    }
                }
                stage('More Complex Expression') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_more_complex_expression
                        '''
                    }
                }
                stage('Square Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_square
                        '''
                    }
                }
                stage('Square Root Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_sqrt
                        '''
                    }
                }
                stage('Square Combined Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_square_combined
                        '''
                    }
                }
                stage('Square Root Combined Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_sqrt_combined
                        '''
                    }
                }
                stage('Square and Sqrt Loop Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_square_and_sqrt_loop
                        '''
                    }
                }
                stage('Complex Operations Tests') {
                    steps {
                        sh '''
                        . venv/bin/activate
                        python -m unittest test_calc.TestCalculator.test_complex_operations
                        '''
                    }
                }
                stage('Nested Operations Tests') {
                    steps {
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
