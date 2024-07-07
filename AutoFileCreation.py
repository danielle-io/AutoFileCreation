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
    create_basic_model(model_file_name, location)
    
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

# ------ End: Put each set of file names and locations here

def create_basic_model(model_file_name, file_path):
    # Add to empty file
    new_file_path = f'{file_path}{model_file_name}'
    copied_file_path = Path(new_file_path)

    if is_mac == 'true':
        file_path = file_path.replace('\\', '/')
    
    if copied_file_path.is_file():
        print(new_file_path + ' already exists, skipping')
        
    else:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    
        template_file = os.path.join(os.path.dirname(__file__), 'ModelTemplate.txt')

        with open(template_file, 'r') as file:
            template_content = file.read()
        
        template_content = template_content.replace('{your_name}', your_name)
        template_content = template_content.replace('{app_name}', app_name)
        template_content = template_content.replace('{new_model_name}', new_model_name)

        with open(new_file_path, 'w') as file:
            file.write(template_content)
            
       print(f'Created {new_file_path}')

def copy_example_to_new_file(fill_in_file_name, file_path):
    # Copy to empty file
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
