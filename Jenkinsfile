#!groovy
node('xnetPython') {

	currentBuild.result = "SUCCESS"
	
	try{
		stage('Checkout'){
			// Checkout the repository from scm
			echo "Cheking out source"
			echo "Testing environment variables: @{env."
			checkout scm
		}		
		
		stage('Testing'){
			// Run tox with the tox-integration.ini file in the root of the repository
			echo "Running Tox integration script"
			sh 'tox -c tox-integration.ini'
		}
		
	}
		
	catch (err) {
		currentBuild.result = "FAILURE"
		throw err
	}	

}