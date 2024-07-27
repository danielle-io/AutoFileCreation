About
This project will follow The Standard project structure for Models, Brokers, and Services. It will also create the necessary files for the project to run. 

Assumptions
You have a project that follows the standard project structure for Models, Brokers, and Services, and an existing model (with all of these corresponding files) that you want to use as a template for creating al of the new files.

The files created include
I. Models
	1. Model under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type 

II: Brokers
	1. Broker under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type

III: Services
	1. Service under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type

IV: Unit Tests
	1. Test under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type

V: Acceptance Tests
	1. Acceptance test under Foundations for the new type
		a. The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		a. The Exceptions folder with exceptions files for the new assignment type

Instructions
1. Create a .env with the following (add your values & if running on a Mac, set IS_MAC=True):

	IS_MAC=False
    OVERWRITE_FILES=False
    ADD_MATCHING_ASSIGNMENT_FILES=True
    ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES=True
    ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES=True
	EXAMPLE_MODEL_NAME=<var goes here>
	NEW_MODEL_NAME=<var goes here>
	APP_NAME=<var goes here>
	ROOT_FOLDER_=<var goes here>
	YOUR_NAME=<var goes here>

2. Open the project file AutoFileCreation.pyproj and run
