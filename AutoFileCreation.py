from ctypes import Array
from hmac import new
import shutil
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
is_mac = os.getenv('IS_MAC')
example_model_name = os.getenv('EXAMPLE_MODEL_NAME')
new_model_name = os.getenv('NEW_MODEL_NAME')
app_name = os.getenv('APP_NAME')
destination = os.getenv('ROOT_FOLDER')
your_name = os.getenv('YOU_NAME')
add_matching_assignment_model = os.getenv('ADD_MATCHING_ASSIGNMENT_MODEL')
add_matching_assignment_orchestration_files = os.getenv('ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES')
add_matching_assignment_coordination_files = os.getenv('ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES')

missing_vars = []

if not is_mac:
    missing_vars.append('IS_MAC')
if not example_model_name:
    missing_vars.append('EXAMPLE_MODEL_NAME')
if not new_model_name:
    missing_vars.append('NEW_MODEL_NAME')
if not app_name:
    missing_vars.append('APP_NAME')
if not destination:
    missing_vars.append('ROOT_FOLDER')
if not your_name:
    missing_vars.append('YOUR_NAME')
if not add_matching_assignment_model:
    missing_vars.append('ADD_MATCHING_ASSIGNMENT_MODEL')
if not add_matching_assignment_model:
    missing_vars.append('ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES')
if not add_matching_assignment_model:
    missing_vars.append('ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES')

if missing_vars != []:
    print(f'Missing environment variables: {", ".join(missing_vars)}')
    raise ValueError('Environment variables must be set')

def main():
    # ------ Start: Put each set of file names and locations here
    # TODO: add back the below line for when making a new model
    # model_file_name = f'{new_model_name}.cs'
    
    # Main model + other models in scope (i.e. ModelState, ModelStatus, etc.) (folder of files)
    example_location_str = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\'
    copy_and_alter_dir_files(example_location_str, example_model_name, new_model_name)

    # Model Exceptions (folder of files)
    example_exceptions_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\Exceptions\\'
    copy_and_alter_dir_files(example_exceptions_location, example_model_name, new_model_name)

    # TODO: alter the StorageBoker and IStorageBroker by adding Configure to OnModelCreating
    
    # IStorageBrokers (single files)
    i_storage_file_name = 'IStorageBroker._s.cs'
    location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
    copy_example_to_new_file(i_storage_file_name, location, example_model_name, new_model_name)

    # Storage Brokers (single files)
    storage_file_name = 'StorageBroker._s.cs'
    location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
    copy_example_to_new_file(storage_file_name, location, example_model_name, new_model_name)
    
    # Configuration for Storage Broker (single files)
    storage_file_name = 'StorageBroker._s.Configurations.cs'
    location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
    copy_example_to_new_file(storage_file_name, location, example_model_name, new_model_name)
    
    # Controllers (single files)
    controller_file_name = '_sController.cs'
    location = f'{destination}{app_name}.Api\\Controllers\\'
    copy_example_to_new_file(controller_file_name, location, example_model_name, new_model_name)
    
    # Services
    example_dir_path_str = f'{destination}{app_name}.Api\\Services\\Foundations\\{example_model_name}s'
    copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
    
    # Acceptance Tests APIs
    example_dir_path_str = f'{destination}{app_name}.Api.Tests.Acceptance\\APIs\\{example_model_name}s'
    copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
    
    # Acceptance Tests Brokers (single files)
    example_dir_path_str = f'{destination}{app_name}.Api.Tests.Acceptance\\Brokers\\'
    broker_file_name = 'APIBroker._s.cs'
    copy_example_to_new_file(broker_file_name, example_dir_path_str, example_model_name, new_model_name)
    
    # Unit Tests
    example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Foundations\\{example_model_name}s'
    copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)

    if add_matching_assignment_model:
        # Assignment Models (folder of files)
        example_assignment_name = f'{example_model_name}Assignment'
        new_assignment_name = f'{new_model_name}Assignment'
        example_location_str = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_assignment_name}s\\'
        copy_and_alter_dir_files(example_location_str, example_model_name, new_model_name);
    
        # Assignment Exceptions
        example_exceptions_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_assignment_name}s\\Exceptions\\'
        copy_and_alter_dir_files(example_exceptions_location, example_model_name, new_model_name)
        
        # Assignment IBrokers (single files)
        i_storage_file_name = 'IStorageBroker._s.cs'
        location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
        copy_example_to_new_file(i_storage_file_name, location, example_assignment_name, new_assignment_name,)

        # Assignment Brokers (single files)
        storage_file_name = 'StorageBroker._s.cs'
        location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
        copy_example_to_new_file(storage_file_name, location, example_assignment_name, new_assignment_name)
        
        # Configuration for Assignment Storage Broker (single files)
        storage_file_name = 'StorageBroker._s.Configurations.cs'
        location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
        copy_example_to_new_file(storage_file_name, location, example_assignment_name, new_assignment_name)
    
        # Assignment Services
        example_dir_path_str = f'{destination}{app_name}.Api\\Services\\Foundations\\{example_assignment_name}s'
        copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
        
        # Assignment Controllers
        controller_file_name = '_sController.cs'
        location = f'{destination}{app_name}.Api\\Controllers\\'
        copy_example_to_new_file(controller_file_name, location, example_model_name, new_model_name)
        
        # Assignment Acceptance Tests APIS
        example_dir_path_str = f'{destination}{app_name}.Api.Tests.Acceptance\\APIs\\{example_assignment_name}s'
        copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_assignment_name)
        
        # Assignment Acceptance Tests Brokers (single files)
        example_dir_path_str = f'{destination}{app_name}.Api.Tests.Acceptance\\Brokers\\'
        broker_file_name = 'ApiBroker._s.cs'
        copy_example_to_new_file(broker_file_name, example_dir_path_str, example_assignment_name, new_assignment_name)
        
        # Unit Tests
        example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Foundations\\{example_assignment_name}s'
        copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
        
        if add_matching_assignment_coordination_files:
            # Assignment Coordinations models folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Models\\Coordinations\\{example_assignment_name}s\\Exceptions\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)
            
            # Assignment Coordinations service folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Services\\Coordinations\\{example_assignment_name}s\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)

            # Assignment Coordinations Unit Tests
            example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Coordinations\\{example_assignment_name}s'
            copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
            
        if add_matching_assignment_orchestration_files:
            orchestration_example_assignment_name = f'{example_assignment_name}Detail'
            
            # Assignment Orchestration Models folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Models\\Orchestrations\\{orchestration_example_assignment_name}s\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)
            
            # Assignment Orchestrations Model Exceptions folder   
            example_orchestration_service_path_str = f'{destination}{app_name}.Api\\Models\\Orchestrations\\{orchestration_example_assignment_name}s\\Exceptions\\'
            copy_and_alter_dir_files(example_orchestration_service_path_str, example_model_name, new_model_name)
              
            # Assignment Orchestrations Service folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Services\\Orchestrations\\{orchestration_example_assignment_name}s\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)
            
            # Assignment Orchestrations Unit Tests
            example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Orchestrations\\{orchestration_example_assignment_name}s'
            copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
    
# ------ End: Put each set of file names and locations here

def get_camel_case(word):
    return word[0].lower() + word[1:]

def get_snake_case(word):
    return word[0].lower() + word[1:]
    
# Works on service files for Coordinations, Foundations, or Orchestrations, on both the model and the modelAssignment (if applicable)
def copy_and_alter_dir_files(example_dir_path_str, curr_example_model_name, curr_new_model_name):
    new_directory_str = example_dir_path_str.replace(curr_example_model_name, curr_new_model_name)

    if is_mac == 'true':
        new_directory_str = new_directory_str.replace('\\', '/')
        example_dir_path_str = example_dir_path_str.replace('\\', '/')

    new_directory_path = Path(new_directory_str)

    # Check if the file already exists
    if new_directory_path.is_file():
        print(f'{new_directory_str} already exists, skipping')
    else:
        # Ensure parent directory exists before creating the file
        new_directory_path.parent.mkdir(parents=True, exist_ok=True)
    
    example_directory = Path(example_dir_path_str)

    # Loop over files in the directory
    for example_path in example_directory.iterdir():
        if example_path.is_file():
            # Process each file
            example_path_str = str(example_path)
            new_file_path_str = example_path_str.replace(curr_example_model_name, curr_new_model_name)
            new_file_path = Path(new_file_path_str)

            # Create new file and change content to match new model
            copy_and_alter_single_file(example_path_str, new_file_path, curr_example_model_name, curr_new_model_name)
            
def create_basic_model(model_file_name, file_path_str, example_exceptions_location_str):
    # Add to empty file
    new_file_path_str = f'{file_path_str}{model_file_name}'
    new_exceptions_directory_str = example_exceptions_location_str.replace(example_model_name, new_model_name)

    if is_mac == 'true':
        new_file_path_str = new_file_path_str.replace('\\', '/')
        example_exceptions_location_str = example_exceptions_location_str.replace('\\', '/')
        new_exceptions_directory_str = new_exceptions_directory_str.replace('\\', '/')

    new_file_path = Path(new_file_path_str)

    # Check if the file already exists
    if new_file_path.is_file():
        print(f'{new_file_path_str} already exists, skipping')
    else:
        # Ensure parent directory exists before creating the file
        new_file_path.parent.mkdir(parents=True, exist_ok=True)
    
        # Create the file using the ModelTemplate.txt file
        template_file = os.path.join(os.path.dirname(__file__), 'ModelTemplate.txt')

        with open(template_file, 'r') as file:
            template_content = file.read()
        
        # Replace placeholders in the content
        template_content = template_content.replace('{your_name}', your_name)
        template_content = template_content.replace('{app_name}', app_name)
        template_content = template_content.replace('{new_model_name}', new_model_name)

        # Create the file (if it doesn't exist)
        if not new_file_path.exists():
            with open(new_file_path, 'w') as file:
                # Optionally, write initial content to the file
                file.write(template_content)

            print(f'{new_file_path_str} created successfully')
        else:
            print(f'{new_file_path_str} already exists, skipping')
            
        print(f'Created {new_file_path_str}')
                
def copy_and_alter_single_file(example_file_path, new_file_path, curr_example_model_name, curr_new_model_name):
    if is_mac == 'true':
        example_file_path = example_file_path.as_posix()
        new_file_path = new_file_path.as_posix()

    if new_file_path.is_file():
        print(f'{new_file_path} already exists, skipping')
    else:
        # Ensure parent directory exists before copying the file
        new_file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        shutil.copyfile(example_file_path, new_file_path)

        # Read content from the original file
        with open(new_file_path, 'r') as file:
            content = file.read()

        # Replace placeholders in the content
        content = content.replace(curr_example_model_name, curr_new_model_name)
        example_camel_case_name = get_camel_case(curr_example_model_name)
        new_camel_case_name = get_camel_case(curr_new_model_name)
        content = content.replace(example_camel_case_name, new_camel_case_name)

        # Write modified content back to the new file
        with open(new_file_path, 'w') as file:
            file.write(content)

        print(f'Created {new_file_path}')    
                    
def copy_example_to_new_file(fill_in_file_name, file_path, curr_example_model_name, curr_new_model_name):
    new_file_name = fill_in_file_name.replace('_', curr_new_model_name)
    
    if is_mac == 'true':
        file_path = file_path.replace('\\', '/')

    example_item_file_name = fill_in_file_name.replace('_', curr_example_model_name)
    new_file_path = f'{file_path}{new_file_name}'

    copied_file_path = Path(new_file_path)
    
    if copied_file_path.is_file():
        print(f'{new_file_path} already exists, skipping')
        
    else:
        shutil.copyfile(f'{file_path}{example_item_file_name}', new_file_path)

        # Replace content
        with open(new_file_path, 'r') as file: content = file.read()

        # Remove Assignment from the name (if it exists) to fix any issues with missing replacements
        curr_example_model_name = curr_example_model_name.replace('Assignment', '')
        curr_new_model_name = curr_new_model_name.replace('Assignment', '')
        
        # Replace all instances of the title case variable
        content = content.replace(curr_example_model_name, curr_new_model_name)

        # Replace all instances of the camelCase variable
        example_camel_case_name = get_camel_case(curr_example_model_name)
        new_camel_case_name = get_camel_case(curr_new_model_name)
        content = content.replace(example_camel_case_name, new_camel_case_name)
        # Write the modified content back to the file
        with open(new_file_path, 'w') as file: file.write(content)
        print(f'Created {new_file_path}')

if __name__ == "__main__":
    main()
