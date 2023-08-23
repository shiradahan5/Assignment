# Devops Home Assignment - Shira Dahan
Sample Calculator Application and Jenkins Pipeline
This repository contains a sample calculator application implemented in Python, along with a Jenkins pipeline to build, test, and deploy the application. The project demonstrates the integration of Jenkins pipelines, Git version control, and basic unit testing.

Project Structure
The repository is organized as follows:

bash
Copy code
/                           # Repository root
|-- files/                  # Directory for application files
|   |-- SampleApplication.py # Main calculator application
|   |-- requirements.txt     # List of required Python packages
|
|-- Jenkinsfile             # Declarative Jenkins pipeline configuration
|-- README.md               # Project documentation
Sample Application
The SampleApplication.py file contains a basic calculator application with two functions: add_numbers and multiply_numbers. Additionally, it includes unittests to verify the accuracy of these functions.

Jenkins Pipeline
The Jenkinsfile defines a three-stage pipeline:

Build: Installs required Python packages from requirements.txt.
Test: Executes the unittests defined in SampleApplication.py.
Deploy: Placeholder for potential deployment steps (can be customized).
Running the Pipeline
To run the Jenkins pipeline:

Create a new Jenkins pipeline job.
Connect the job to your Git repository.
Specify the Jenkinsfile in the repository as the pipeline configuration.
Trigger the pipeline job execution.
Notes
Unittests are executed as part of the pipeline's test stage. Test results are displayed in the Jenkins console output.
The pipeline can be customized to accommodate your specific needs.
Ensure that your Git repository is properly integrated with Jenkins.
