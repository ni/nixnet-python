#!groovy
node('xnetPython') {

	currentBuild.result = "SUCCESS"

	// Environment variables to configure the hardware for testing. This scope applies to all stages
	environment {
		NIXNET_FIXTURE_IN_INTERFACE = 'CAN1'
		NIXNET_FIXTURE_OUT_INTERFACE = 'CAN2'
	}

	try{
		stage('Checkout'){
			// Checkout the repository from scm
			echo "Cheking out source"
			checkout scm
		}

		stage('EnvironmentSetup'){
			// Stage to setup environment variables and ensure correct testing evironment.
			bat 'pip install --upgrade setuptools'
		}

		stage('Testing'){
			// Run tox with the tox-integration.ini file in the root of the repository
			echo "Running Tox integration script"
			try {
				bat 'tox -c tox-integration.ini'
			} finally {
				step([$class: 'CoberturaPublisher', coberturaReportFile: 'coverage.xml'])
				junit "junit/*.xml"
			}
		}
	}
	catch (err) {
		currentBuild.result = "FAILURE"
	}
}
