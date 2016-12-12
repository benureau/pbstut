from __future__ import print_function
import sys, os, random, json

import prepare


pbs_arrayid = int(sys.argv[1])
print('started job {}!'.format(pbs_arrayid))


def save_results(results):
    """Save the results of the job"""
    directory = prepare.rootpath
    os.makedirs(directory, exist_ok=True) # making sure the directory exists

    filepath = os.path.join(directory, 'results_{}.json'.format(pbs_arrayid))
    with open(filepath, 'w') as f:
        json.dump(results, f)
    print('saved results in {}'.format(filepath))


if False: # let's intentionally fail job number 1, 3, 4, 5
    print('error', file=sys.stderr)
    sys.exit(1)
else:
    # loading parameters
    configpath = os.path.join(prepare.rootpath, 'config_{}.json'.format(pbs_arrayid))
    with open(configpath, 'r') as f:
        params = json.load(f)

    # producing results
    results = {'pbs_arrayid': pbs_arrayid,
               'random_draw': random.uniform(params['min'], params['max'])}

    # saving resutls
    save_results(results)
    print('finished')
