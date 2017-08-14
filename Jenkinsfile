#!groovy
node('xnetPython') {

	currentBuild.result = "SUCCESS"

	// Environment variables to configure the hardware for testing. This scope applies to all stages
	environment {
		CAN_FIXTURE_IN_INTERFACE = 'CAN1'
		CAN_FIXTURE_OUT_INTERFACE = 'CAN2'
		LIN_FIXTURE_IN_INTERFACE = 'LIN1'
		LIN_FIXTURE_OUT_INTERFACE = 'LIN2'
	}

	try{
		stage('Checkout'){
			// Checkout the repository from scm
			echo "Checking out source"
			checkout scm
		}

		stage('EnvironmentSetup'){
			// Stage to setup environment variables and ensure correct testing environment.
			bat 'pip install --upgrade setuptools'
		}

		stage('Testing'){
			// Run tox with the tox-integration.ini file in the root of the repository
			echo "Running Tox integration script"
			try {
				bat 'tox -c tox-integration.ini -e py27-test -- --can-in-interface CAN1 --can-out-interface CAN2 --lin-in-interface LIN1 --lin-out-interface LIN2'
				bat 'tox -c tox-integration.ini -e py34-test -- --can-in-interface CAN1 --can-out-interface CAN2 --lin-in-interface LIN1 --lin-out-interface LIN2'
			} finally {
				step([$class: 'CoberturaPublisher', coberturaReportFile: 'coverage.xml'])
				junit "junit/*.xml"
			}
		}
	}
	catch (err) {
		currentBuild.result = "FAILURE"
		emailextrecipients([[$class: 'CulpritsRecipientProvider'], [$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']])
	}
}
