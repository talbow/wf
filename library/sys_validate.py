#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import json

def run_module():
    module_args = dict(
        json_input=dict(type='str', required=True)
    )

    # Initialize the result dictionary
    result = dict(
        changed=False,
        message=''
    )

    # Create the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Retrieve the JSON data from the module's parameters
    json_input = module.params['json_input']

    try:
        data = json.loads(json_input)
        
        # Validate the API version
        api_version = data.get('API_Version', None)
        if api_version == "4.0":
            result['message'] = f"API_Version is valid: {api_version}"
        else:
            module.fail_json(msg=f"API_Version is invalid or missing: {api_version}")

    except json.JSONDecodeError as e:
        module.fail_json(msg=f"Invalid JSON input: {str(e)}")

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
