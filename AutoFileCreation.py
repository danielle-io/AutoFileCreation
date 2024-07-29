from ctypes import Array
from hmac import new
import shutil
import os
from tkinter import N
from dotenv import load_dotenv
from pathlib import Path
import re

def str_to_bool(value, field_name):
    if value == 'True':
        return True
    elif value == 'False':
        return False
    else:
        raise ValueError(f"Modify your .env file to contain True or False for boolean type: {field_name}, current value is {value}")
   
# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
is_mac = str_to_bool(os.getenv('IS_MAC'), 'IS_MAC')
overwrite_files = str_to_bool(os.getenv('OVERWRITE_FILES'), 'OVERWRITE_FILES')
example_model_name = os.getenv('EXAMPLE_MODEL_NAME')
new_model_name = os.getenv('NEW_MODEL_NAME')
app_name = os.getenv('APP_NAME')
destination = os.getenv('ROOT_FOLDER')
add_matching_assignment_model = str_to_bool(os.getenv('ADD_MATCHING_ASSIGNMENT_MODEL'), 'ADD_MATCHING_ASSIGNMENT_MODEL')
add_matching_assignment_orchestration_files = str_to_bool(os.getenv('ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES'), 'ADD_MATCHING_ASSIGNMENT_ORCHESTRATION_FILES')
add_matching_assignment_coordination_files = str_to_bool(os.getenv('ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES'), 'ADD_MATCHING_ASSIGNMENT_COORDINATION_FILES')

startup_file_path = f'{destination}{app_name}.Api\\Startup.cs'
storage_broker_registration_path_str = f'{destination}{app_name}.Api\\Brokers\\Storages\\StorageBroker.cs'

missing_vars = []

if not example_model_name:
    missing_vars.append('EXAMPLE_MODEL_NAME')
if not new_model_name:
    missing_vars.append('NEW_MODEL_NAME')
if not destination:
    missing_vars.append('ROOT_FOLDER')
if not app_name:
    missing_vars.append('APP_NAME')

if missing_vars != []:
    print(f'Missing environment variables: {", ".join(missing_vars)}')
    raise ValueError('Environment variables must be set')

def main():
    # ------ Start: Put each set of file names and locations here
    
    # Main model + other models in scope (i.e. ModelState, ModelStatus, etc.) (folder of files)
    example_location_str = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\'
    new_directory_path = copy_and_alter_dir_files(example_location_str, example_model_name, new_model_name)

    # Model Exceptions (folder of files)
    example_exceptions_location = f'{destination}{app_name}.Api\\Models\\Foundations\\{example_model_name}s\\Exceptions\\'
    copy_and_alter_dir_files(example_exceptions_location, example_model_name, new_model_name)
    
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
    
    # Register the model in the storage broker
    register_model(storage_broker_registration_path_str, new_model_name)

    # Controllers (single files)
    controller_file_name = '_sController.cs'
    location = f'{destination}{app_name}.Api\\Controllers\\'
    copy_example_to_new_file(controller_file_name, location, example_model_name, new_model_name)
    
    # Services
    example_dir_path_str = f'{destination}{app_name}.Api\\Services\\Foundations\\{example_model_name}s'
    copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
    
    # Register the new service
    register_service(startup_file_path, new_model_name, "Foundation")
    
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
        
        # Register the model in the storage broker
        register_model(storage_broker_registration_path_str, new_assignment_name)
    
        # Assignment Services
        example_dir_path_str = f'{destination}{app_name}.Api\\Services\\Foundations\\{example_assignment_name}s'
        copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
        
        # Register the new service
        register_service(startup_file_path, new_assignment_name, 'Foundation')
        
        # Assignment Controllers
        controller_file_name = '_sController.cs'
        location = f'{destination}{app_name}.Api\\Controllers\\'
        copy_example_to_new_file(controller_file_name, location, example_assignment_name, new_assignment_name)
        
        # Assignment Acceptance Tests APIS
        example_dir_path_str = f'{destination}{app_name}.Api.Tests.Acceptance\\APIs\\{example_assignment_name}s'
        copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
        
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

            # Register the Assignment Coordinations service
            register_service(startup_file_path, new_assignment_name, 'Coordination')
        
            # Assignment Coordinations Unit Tests
            example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Coordinations\\{example_assignment_name}s'
            copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
            
        if add_matching_assignment_orchestration_files:
            orchestration_example_assignment_name = f'{example_assignment_name}Detail'
            orchestration_new_assignment_name = f'{new_assignment_name}Detail'
            
            # Assignment Orchestration Models folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Models\\Orchestrations\\{orchestration_example_assignment_name}s\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)
            
            # Assignment Orchestrations Model Exceptions folder   
            example_orchestration_service_path_str = f'{destination}{app_name}.Api\\Models\\Orchestrations\\{orchestration_example_assignment_name}s\\Exceptions\\'
            copy_and_alter_dir_files(example_orchestration_service_path_str, example_model_name, new_model_name)
              
            # Assignment Orchestrations Service folder 
            example_coordination_service_path_str = f'{destination}{app_name}.Api\\Services\\Orchestrations\\{orchestration_example_assignment_name}s\\'
            copy_and_alter_dir_files(example_coordination_service_path_str, example_model_name, new_model_name)   
            
            # Register the Assignment Orchestration service
            register_service(startup_file_path, orchestration_new_assignment_name, 'Orchestration')
            
            # Assignment Orchestrations Unit Tests
            example_dir_path_str = f'{destination}{app_name}.Api.Tests.Unit\\Services\\Orchestrations\\{orchestration_example_assignment_name}s'
            copy_and_alter_dir_files(example_dir_path_str, example_model_name, new_model_name)
    
# ------ End: Put each set of file names and locations here

def register_model(storage_broker_path_str, new_model_name):
    new_directory_path = Path(storage_broker_path_str)
    
    if is_mac :
        storage_broker_path_str = Path(new_directory_path.as_posix())

    # Read content from the original file
    with open(new_directory_path, 'r') as file:
        content = file.read()

    new_str = f"Configure{new_model_name}(modelBuilder);"
    
       # Find the function definition
    function_pattern = r'(protected\s+override\s+void\s+OnModelCreating\(ModelBuilder\s+modelBuilder\)\s*\{)(.*?)(\})'
    match = re.search(function_pattern, content, re.DOTALL)
    
    if not match:
        raise ValueError("Function definition not found")
    
    # Extract the parts of the function
    function_start = match.group(1)
    function_body = match.group(2)
    function_end = match.group(3)

    # Check if the new string is already in the function body
    if new_str in function_body:
        print(f'The model {new_model_name} is already registered, skipping')
        return
    
    # Add the new line to the function body
    new_function_body = f'{function_body}\n\t\t\t{new_str}\n'
    
    # Reconstruct the function
    new_function = function_start + new_function_body + function_end
    
    # Replace the old function with the new one in the content
    new_content = content[:match.start()] + new_function + content[match.end():]
    
    # Write the modified content back to the file
    with open(new_directory_path, 'w') as file:
        file.write(new_content)
        
    print(f'Registered {new_model_name} model')
    
def register_service(startup_path, new_model_name, service_type):
    new_directory_path = Path(startup_path)

    if is_mac :
        new_directory_path = Path(new_directory_path.as_posix())
        
    # Read content from the original file
    with open(new_directory_path, 'r') as file:
        content = file.read()

    new_str = f'services.AddTransient<I{new_model_name}{service_type}Service, {new_model_name}{service_type}Service>();'
    if service_type == "Foundation":
        new_str = f'services.AddTransient<I{new_model_name}Service, {new_model_name}Service>();'

    print(f'Adding service: {new_str}')

    # Find the function definition for AddServices
    function_pattern = r'(private\s+static\s+void\s+AddServices\(IServiceCollection\s+services\)\s*\{[^}]*\})'
    match = re.search(function_pattern, content, re.DOTALL)
    if not match:
        raise ValueError("Function definition not found")

    import_str = f'using {app_name}.Api.Services.{service_type}s.{new_model_name}s;\n'

    # Check if the import is already in the file
    if import_str not in content:
        # Find the last import statement
        import_pattern = r'using\s+.*?;\n'
        last_import = re.findall(import_pattern, content)[-1] if re.findall(import_pattern, content) else ''
        
        # Add the new import statement after the last one
        content = content.replace(last_import, last_import + import_str)
    else:
        print(f'The import for {new_model_name} is already in the startup file.')

    # Extract the parts of the function
    function_full = match.group(1)
    function_minus_bracket = function_full[:-1]

    # Check if the new string is already in the function body
    if new_str in function_full:
        print(f'The service for {new_model_name} is already registered, skipping')
        return
    
    # Change the } to a newline with the new service and a }
    function_end = f'\t{new_str}\n\t\t' + "}"

    function_updated = function_minus_bracket + function_end
    
    # Replace the old function with the new one in the content
    updated_content = content.replace(function_full, function_updated)

    # Write the modified content back to the file
    with open(new_directory_path, 'w') as file:
        file.write(updated_content)

    print(f'Added service configuration for {new_model_name}')

def get_camel_case(word):
    return word[0].lower() + word[1:]
    
# Works on service files for Coordinations, Foundations, or Orchestrations, on both the model and the modelAssignment (if applicable)
def copy_and_alter_dir_files(example_dir_path_str, curr_example_model_name, curr_new_model_name):
    new_directory_str = example_dir_path_str.replace(curr_example_model_name, curr_new_model_name)

    new_directory_path = Path(new_directory_str)
    example_directory = Path(example_dir_path_str)

    if is_mac :
        new_directory_path = Path(new_directory_path.as_posix())
        example_directory = Path(example_directory.as_posix())

    # Check if the file already exists
    if new_directory_path.is_file():
        print(f'{new_directory_str} already exists, skipping')
    else:
        # Ensure parent directory exists before creating the file
        new_directory_path.parent.mkdir(parents=True, exist_ok=True)
    

    # Loop over files in the directory
    for example_path in example_directory.iterdir():
        if example_path.is_file():
            # Process each file
            example_path_str = str(example_path)
            new_file_path_str = example_path_str.replace(curr_example_model_name, curr_new_model_name)
            new_file_path = Path(new_file_path_str)

            # Create new file and change content to match new model
            copy_and_alter_single_file(example_path_str, new_file_path, curr_example_model_name, curr_new_model_name)
            
    return new_directory_path 
                
def copy_and_alter_single_file(example_file_path_str, new_file_path, curr_example_model_name, curr_new_model_name):
    main_model_path =  Path(f'{destination}{app_name}.Api\\Models\\Foundations\\{new_model_name}s\\{new_model_name}.cs')
    
    if is_mac :
        example_file_path_str = example_file_path_str.replace('\\', '/')
        new_file_path = Path(new_file_path.as_posix())
        main_model_path = Path(main_model_path.as_posix())

    if new_file_path.is_file():        
        if not overwrite_files:
            print(f'{new_file_path} already exists, skipping')
            
            return
        
        # Do not overwrite an existing main model file
        elif (str(main_model_path) in str(new_file_path)):
            print('Main model file already exists, skipping')
            
            return
        else:
            print(f'{new_file_path} already exists, overwriting')

    # Ensure parent directory exists before copying the file
    new_file_path.parent.mkdir(parents=True, exist_ok=True)
        
    # Copy file
    shutil.copyfile(example_file_path_str, new_file_path)

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
    new_file_path = f'{file_path}{new_file_name}'
    copied_file_path = Path(new_file_path)

    if is_mac:
        copied_file_path = Path(copied_file_path.as_posix())

    example_item_file_name = fill_in_file_name.replace('_', curr_example_model_name)

    if copied_file_path.is_file():
        if not overwrite_files:
            print(f'{new_file_path} already exists, skipping')
                        
            return
        else:
            print(f'{new_file_path} already exists, overwriting')
       
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
