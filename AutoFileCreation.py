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

if missing_vars != []:
    print(f'Missing environment variables: {", ".join(missing_vars)}')
    raise ValueError('Environment variables must be set')

new_model_item_name_camel_case = new_model_name[0].lower() + new_model_name[1:]
example_model_name_camel_case = example_model_name[0].lower() + example_model_name[1:]

def main():
    # ------ Start: Put each set of file names and locations here

    # Models
    model_file_name = f'{new_model_name}.cs'
    location = f'{destination}{app_name}.Api\\Models\\Foundations\\{new_model_name}s\\'
    example_exceptions_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\Exceptions\\'
    create_basic_model(model_file_name, location, example_exceptions_location)
    
    # ModelState 
    new_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{new_model_name}\\{new_model_name}State.cs'
    old_location = new_location.replace(new_model_name, example_model_name);
    copy_single_file(old_location, new_location);

    # Assignment Models
    Array<string> assignmentFiles;
    assignmentFiles =  ['AssignmentStatus', 'AssignmentState', 'Assignment'];
    
    for file_name in assignmentFiles:
        new_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{new_model_name}Assignments\\{new_model_name}{file_name}.cs'
        old_location = new_location.replace(new_model_name, example_model_name);
        copy_single_file(old_location, new_location);
        

    example_exceptions_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\Exceptions\\'
    
    # The model is already made so this will just copy in the exceptions
    create_basic_model(model_file_name, location, example_exceptions_location)
    
    # TODO: alter the StorageBoker and IStorageBroker by adding Configure to OnModelCreating
    
    # IStorages
    i_storage_file_name = 'IStorageBroker._s.cs'
    location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
    copy_example_to_new_file(i_storage_file_name, location)

    # Storages
    storage_file_name = 'StorageBroker._s.cs'
    location = f'{destination}{app_name}.Api\\Brokers\\Storages\\'
    copy_example_to_new_file(storage_file_name, location)
    
    # Controllers
    controller_file_name = '_sController.cs'
    location = f'{destination}{app_name}.Api\\Controllers\\'
    copy_example_to_new_file(controller_file_name, location)
    
    # Services
    example_service_path_str = f'{destination}{app_name}.Api\\Services\\Foundations\\{example_model_name}s'
    create_service_files(example_service_path_str)

    # Coordinations folder + Exceptions
    example_coordination_service_path_str = f'{destination}{app_name}.Api\\Services\\Coordinations\\{example_model_name}Assignments'
    create_service_files(example_coordination_service_path_str)
    
    # TODO Orchestrations folder + Exceptions

    
    # TODO: copy each file in that folder and replace the model name with the new model name
    # Acceptance Tests
    # example_acceptance_tests = f'{destination}{app_name}.Api.Tests.Acceptance\APIs\\{example_model_name}'
    
    
# ------ End: Put each set of file names and locations here

def create_service_files(example_service_path_str):
    new_service_directory_str = example_service_path_str.replace(example_model_name, new_model_name)

    if is_mac == 'true':
        new_service_directory_str = new_service_directory_str.replace('\\', '/')
        example_service_path_str = example_service_path_str.replace('\\', '/')

    new_service_directory_path = Path(new_service_directory_str)

    # Check if the file already exists
    if new_service_directory_path.is_file():
        print(f'{new_service_directory_str} already exists, skipping')
    else:
        # Ensure parent directory exists before creating the file
        new_service_directory_path.parent.mkdir(parents=True, exist_ok=True)
    
      
    example_directory = Path(example_service_path_str)

    # Loop over files in the directory
    for example_path in example_directory.iterdir():
        if example_path.is_file():
            # Process each file
            example_path_str = str(example_path)
            new_file_path_str = example_path_str.replace(example_model_name, new_model_name)
            new_file_path = Path(new_file_path_str)

            # Create new file and change content to match new model
            copy_single_file(example_exceptions_path, new_file_path)
            
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
    
        template_file = os.path.join(os.path.dirname(__file__), 'ModelTemplate.txt')

        with open(template_file, 'r') as file:
            template_content = file.read()
        
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
    
    example_exceptions_directory = Path(example_exceptions_location_str)

    # Ensure the directory exists
    example_exceptions_directory.mkdir(parents=True, exist_ok=True)

    # Loop over files in the directory
    for example_exceptions_path in example_exceptions_directory.iterdir():
        if example_exceptions_path.is_file():
            # Process each file
            example_exceptions_path_str = str(example_exceptions_path)
            new_file_path_str = example_exceptions_path_str.replace(example_model_name, new_model_name)
            new_file_path = Path(new_file_path_str)

            # Create new file and change content to match new model
            copy_single_file(example_exceptions_path, new_file_path)
                
def copy_single_file(example_file_path, new_file_path):
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
        content = content.replace(example_model_name, new_model_name)
        content = content.replace(example_model_name_camel_case, new_model_item_name_camel_case)

        # Write modified content back to the new file
        with open(new_file_path, 'w') as file:
            file.write(content)

        print(f'Created {new_file_path}')
                    
def copy_example_to_new_file(fill_in_file_name, file_path):
    new_file_name = fill_in_file_name.replace('_', new_model_name)
    
    if is_mac == 'true':
        file_path = file_path.replace('\\', '/')

    example_item_file_name = fill_in_file_name.replace('_', example_model_name)
    new_file_path = f'{file_path}{new_file_name}'

    copied_file_path = Path(new_file_path)
    
    if copied_file_path.is_file():
        print(f'{new_file_path} already exists, skipping')
        
    else:
        shutil.copyfile(f'{file_path}{example_item_file_name}', new_file_path)

        # Replace content
        with open(new_file_path, 'r') as file: content = file.read()

        # Replace all instances of the title case variable
        content = content.replace(example_model_name, new_model_name)

        # Replace all instances of the camelCase variable
        content = content.replace(example_model_name_camel_case, new_model_item_name_camel_case)

        # Write the modified content back to the file
        with open(new_file_path, 'w') as file: file.write(content)
        print(f'Created {new_file_path}')

if __name__ == "__main__":
    main()
