import os

# ---- Start: Variable Changes ----
app_name = 'appName.Core'
destination_path = 'C:/Users/pathGoesHere'

# Keep singular and in titlecase
new_model_item_name = 'CareAnimal'
example_item_name = 'CarePerson'
# ---- End Variable Changes ----

new_model_item_name_camel_case = new_model_item_name[0].lower() + new_model_item_name[1:]
example_item_name_camel_case = example_item_name[0].lower() + example_item_name[1:]

def main():
	# ------ Start: Put each set of file names and locations here

	# IStorage
	i_storage_file_name = IStorageBroker._s.cs
	location =  f'{destination_path}{app_name}.Api/Brokers/Storages/'
	copy_example_to_new_file(i_storage_file_name, location)

	# Storage
	storage_file_name = StorageBroker._s.cs
	location =  f'{destination_path}{app_name}.Api/Brokers/Storages/'
	copy_example_to_new_file(storage_file_name, location)

	# ------ End: Put each set of file names and locations here

def copy_example_to_new_file(storage_file_name, file_path, new_model_item_name):
	# Copy to empty file
	file_name = storage_file_name.replace('_', new_model_item_name)
	example_item_file_name = file_name.replace('_', example_item_name)
	new_file_path = f'{location}{file_name}'
	example_file.copyfile(f'{location}{example_item_file_name}', new_file_path)
	
	# Replace content
	with open(file_path, 'r') as file: content = file.read()
    
	# Replace all instances of the title case variable
	content = content.replace(example_item_name, new_model_item_name)
    
	# Replace all instances of the camelCase variable
	content = content.replace(example_item_name_camel_case, new_model_item_name_camel_case)
	
	# Write the modified content back to the file
	with open(file_path, 'w') as file: file.write(content)

if __name__ == "__main__":
	main()