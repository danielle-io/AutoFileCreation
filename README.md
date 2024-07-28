# About
This project will follow The Standard project structure. Using an example model, you can create a new model with all of the corresponding files, such as Models, Brokers, Services, Controllers, Unit and Acceptance Tests. It will also register your service and model in the storage broker by modifying those existing files.

This script helps you speed up the process of getting all of your files created, but you will still want to build your project and fix any potential errors after each run. You can create one new model (and a matching assignment model for it if you'd like) per run of this script. If your example model has fields your new model does not, you will likely have to fix those references for your project to properly build. This is why simple examples and simple new models are best to start with, and then you can continue to add to your new model after the files are generated.

# Assumptions
You have a project that follows The Standard project structure and an existing model (with all of these corresponding files) that is already in your project that you want to use as a template for creating all of the new files. This includes Unit and Acceptance test projects.

## Project Structure
If your project is not sturctured in the following way, you will need to fork this repo and modify the code so that it will work for you:
	
	- {app_name}.Api\\Brokers\\Storages\\
	- {app_name}.Api\\Controllers\\
	- {app_name}.Api\\Services\\Foundations\\
	- {app_name}.Api.Tests.Acceptance\\APIs\\
	- {app_name}.Api.Tests.Acceptance\\Brokers\\
	- {app_name}.Api.Tests.Unit\\Services\\Foundations\\

## Optional Parameters
If you want your model to have an assignment model that goes with it (this is useful for linking a user with a model, for example), you can set the `ADD_MATCHING_ASSIGNMENT_FILES` parameter to `True` in the `.env` file. This will only work if your example model has an assignment model for it. You can also do the same for orchestration and coordination assignment files by setting those parameters to True as well, but again, you must have those for your example model already.

# Recommendations
Use a very simple example model, and if you don't have one, create one to go off of. Fields and therefore validations should be very limited so that your new model does not have much to remove once you generate the files. If you are referencing lots of fields that are not in the new model, there will be more cleanup to do after you run this. It's better to start with a simple example model and a simple model, and then manually add to your generated files to cover all of the validations and tests.

# Instructions
1. Create a .env file in your project directory with the following:

	```
	IS_MAC=False
	OVERWRITE_FILES=False
	ADD_MATCHING_ASSIGNMENT_FILES=False
	ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES=False
	ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES=False
	EXAMPLE_MODEL_NAME=<var goes here>
	NEW_MODEL_NAME=<var goes here>
	APP_NAME=<var goes here>
	ROOT_FOLDER_=<var goes here>
	```

	Modify these values to fit your project.
	- If using Windows, `IS_MAC` should be `False`, if on a Mac, set to `True`
	- `OVERWRITE_FILES` should be `True` <b>only</b> if you are okay with overwriting any files that already exist for your new model. For example, if you created unit tests and want to keep those rather than create modified copies from your example model's unit tests, do not set this to `True`. Note: your model itself will not be overwritten even if this is set to `True`, just all other generated files.
	- `ROOT_FOLDER` should generally look like this (but with your path to your project): `C:\Users\whatever-is-here\source\repos\my-github-name\myapp.core\`

2. Open the project file AutoFileCreation.pyproj and run

# Files Created
1. Models
	1. Model under Foundations for the new type
		- The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment model for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type 

2. Brokers
	1. Broker under Foundations for the new type
		- The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment broker for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type

3. Services
	1. Service under Foundations for the new type
		- The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment service for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type

4. Unit Tests
	1. Test under Foundations for the new type
		- The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment test for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type

5. Acceptance Tests
	1. Acceptance test under Foundations for the new type
		- The Exceptions folder with exceptions files for the new type
	2. A Corresponding Foundations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	3. A Corresponding Orchestrations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type
	4. A Corresponding Coordinations Assignment acceptance test for the new type (if ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES is set to True)
		- The Exceptions folder with exceptions files for the new assignment type


# Files Modified
1. The model will be registered in the storage broker through modifying `StorageBroker.cs`
2. The service will be registered through modifying `Startup.cs`