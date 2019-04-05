#!/usr/bin/python

import subprocess
from ansible.module_utils.basic import AnsibleModule

def getIP():
    return subprocess.check_output(["hostname"] + ["-i"])

def main():
    module = AnsibleModule( argument_spec=dict() )

    response = getIP()

    result = dict(
	message=response,
	changed=False
    )

    module.exit_json(**result)
    #module.fail_json(msg='Fatal error occurred.')

main()
