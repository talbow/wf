#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def validate_json(data, data_type):
    match data_type:
        case 'vol':
            # Perform validation for 'vol' type JSON data
            if 'volume' in data and isinstance(data['volume'], (int, float)):
                return True, "Valid 'vol' JSON data"
            else:
                return False, "Invalid 'vol' JSON data"
            
        # Add other cases here as needed
        case _:
            return False, "Unknown data type"

def run_module():
    module_args = dict(
        json_data=dict(type='dict', required=True),
        data_type=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    json_data = module.params['json_data']
    data_type = module.params['data_type']

    is_valid, message = validate_json(json_data, data_type)
    result['message'] = message

    if not is_valid:
        module.fail_json(msg=message, **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
