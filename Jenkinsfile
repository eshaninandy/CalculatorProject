pipeline {
    agent {
        label 'node-1'
    }
    stages {
        stage('Run Complex Tests in Parallel') {
            parallel {
                stage('Addition Tests') {
                    steps {
                        sh 'python -m unittest test_calc.TestCalculator.test_addition_loop'
                    }
                }
                stage('Subtraction and Multiplication Tests') {
                    steps {
                        sh 'python -m unittest test_calc.TestCalculator.test_subtraction'
                    }
                }
                stage('Square and Sqrt Tests') {
                    steps {
                        sh 'python -m unittest test_calc.TestCalculator.test_square_and_sqrt_loop'
                    }
                }
                stage('Combined Operations') {
                    steps {
                        sh 'python -m unittest test_calc.TestCalculator.test_combined_operations'
                    }
                }
                stage('Complex Operations and Load Test') {
                    steps {
                        sh 'python -m unittest test_calc.TestCalculator.test_complex_operations'
                    }
                }
            }
        }
    }
}
