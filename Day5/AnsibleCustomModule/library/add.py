#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(value1, value2):
    return value1 + value2 

def main():
    module = AnsibleModule(
		argument_spec=dict (
			first_number=dict(type='float', required=True),
			second_number=dict(type='float', required=True)
		)
    )

    val1 = module.params['first_number'] 
    val2 = module.params['second_number'] 

    response = add( val1, val2)

    result = dict(
	message=response,
	changed=False
    )

    module.exit_json(**result)
    #module.fail_json(msg='Fatal error occurred.')

main()
