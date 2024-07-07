import shutil
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
    
# Retrieve environment variables
example_item_name = os.getenv('EXAMPLE_ITEM_NAME')
new_value = os.getenv('NEW_VALUE')
app_name = os.getenv('APP_NAME')
destination = os.getenv('DESTINATION')

if not example_item_name or not new_value or not app_name or not destination:
    raise ValueError("Environment variables 'EXAMPLE_ITEM_NAME' and 'NEW_VALUE' must be set")

new_model_item_name_camel_case = new_value[0].lower() + new_value[1:]
example_item_name_camel_case = example_item_name[0].lower() + example_item_name[1:]

def main():
	# ------ Start: Put each set of file names and locations here

	# IStorage
	i_storage_file_name = 'IStorageBroker._s.cs'
	location =  f'{destination}{app_name}.Api/Brokers/Storages/'
	copy_example_to_new_file(i_storage_file_name, location)

	# Storage
	storage_file_name = 'StorageBroker._s.cs'
	location =  f'{destination}{app_name}.Api/Brokers/Storages/'
	copy_example_to_new_file(storage_file_name, location)

	# ------ End: Put each set of file names and locations here

def copy_example_to_new_file(storage_file_name, file_path):
	# Copy to empty file
	file_name = storage_file_name.replace('_', new_value)
	example_item_file_name = file_name.replace('_', example_item_name)
	new_file_path = f'{file_path}{file_name}'
	shutil.copyfile(f'{file_path}{example_item_file_name}', new_file_path)
	
	# Replace content
	with open(file_path, 'r') as file: content = file.read()
    
	# Replace all instances of the title case variable
	content = content.replace(example_item_name, new_value)
    
	# Replace all instances of the camelCase variable
	content = content.replace(example_item_name_camel_case, new_model_item_name_camel_case)
	
	# Write the modified content back to the file
	with open(file_path, 'w') as file: file.write(content)

if __name__ == "__main__":
	main()