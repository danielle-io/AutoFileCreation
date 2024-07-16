About
This project will follow The Standard project structure for Models, Brokers, and Services. It will also create the necessary files for the project to run. 

Assumptions
You have a project that follows the standard project structure for Models, Brokers, and Services, and an existing model (with all of these corresponding files) that you want to use as a template for creating al of the new files.

The files created include
I. Models
	1. Model under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A corresponding Foundations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A corresponding Orchestrations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A corresponding Coordinations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type 



Instructions
1. Create a .env with the following (add your values & if running on a Mac, set IS_MAC=True):

	IS_MAC=False
    ADD_MATCHING_ASSIGNMENT_FILES=True
    ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES=True
    ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES=True
	EXAMPLE_MODEL_NAME=<var goes here>
	NEW_MODEL_NAME=<var goes here>
	APP_NAME=<var goes here>
	ROOT_FOLDER_=<var goes here>
	YOUR_NAME=<var goes here>

2. Open the project file AutoFileCreation.pyproj and run
