import shutil
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
example_item_name = os.getenv('EXAMPLE_ITEM_NAME')
new_value = os.getenv('NEW_VALUE')
app_name = os.getenv('APP_NAME')
destination = os.getenv('DESTINATION')
is_mac = os.getenv('IS_MAC')

if not example_item_name or not new_value or not app_name or not destination:
    raise ValueError("Environment variables 'EXAMPLE_ITEM_NAME' and 'NEW_VALUE' must be set")

new_model_item_name_camel_case = new_value[0].lower() + new_value[1:]
example_item_name_camel_case = example_item_name[0].lower() + example_item_name[1:]


def main():
    # ------ Start: Put each set of file names and locations here

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

def create_basic_model(fill_in_file_name, file_path):
    # Add to empty file
    new_file_name = fill_in_file_name.replace('_', new_value)
    
    if (is_mac == 'true'):
        file_path.replace('\\', '/')
    
    example_item_file_name = fill_in_file_name.replace('_', example_item_name)
    new_file_path = f'{file_path}{new_file_name}'
    file_content = 'This is the content of the new file.'

    with open(new_file_path, 'w') as file:
        file.write(content)

def copy_example_to_new_file(fill_in_file_name, file_path):
    # Copy to empty file
    new_file_name = fill_in_file_name.replace('_', new_value)
    if is_mac == 'true':
        file_path = file_path.replace('\\', '/')

    example_item_file_name = fill_in_file_name.replace('_', example_item_name)
    new_file_path = f'{file_path}{new_file_name}'

    copied_file_path = Path(new_file_path)
    if copied_file_path.is_file():
        print(new_file_path + ' already exists, skipping')
    else:
        shutil.copyfile(f'{file_path}{example_item_file_name}', new_file_path)

        # Replace content
        with open(new_file_path, 'r') as file: content = file.read()

        # Replace all instances of the title case variable
        content = content.replace(example_item_name, new_value)

        # Replace all instances of the camelCase variable
        content = content.replace(example_item_name_camel_case, new_model_item_name_camel_case)

        # Write the modified content back to the file
        with open(new_file_path, 'w') as file: file.write(content)
        print('Created '+new_file_path)


if __name__ == "__main__":
    main()
