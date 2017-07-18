#!groovy
node('xnetPython01') {

	currentBuild.result = "SUCCESS"
	
	try{
		stage('Test'){
			// test script to checkout the scm
			echo "Cheking out SCM"
			//checkout scm
		}		
	}
	
	catch (err) {
		currentBuild.result = "FAILURE"
		throw err
	}	
	
}