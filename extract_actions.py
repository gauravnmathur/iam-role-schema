import os
import sys
import glob
import json

def main(roles_dir):
    primitive_actions = set()
    primitive_action_allowed_types = set()

    for filename in glob.glob(os.path.join(roles_dir, '*.json')):
        fc = open(filename, 'r').read()
        rjson = json.loads(fc)

        for statement in rjson['statements']:
            for action in statement['actions']:
                primitive_actions.add(action)
            for allowed_type in statement['allowed_types']:
                primitive_action_allowed_types.add(allowed_type)


    pa = json.dumps(list(primitive_actions))
    with open('role_actions.json', 'w') as fp:
        fp.write(pa)
    
    pa = json.dumps(list(primitive_action_allowed_types))
    with open('role_allowed_types.json', 'w') as fp:
        fp.write(pa)

    print "Generated list of actions (role_actions.json) and allowed types (role_allowed_types.json)"
if __name__ == "__main__":
    main(sys.argv[1])
