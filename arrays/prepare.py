import argparse
import json
import os


# username on the cluster
username = 'fbenurea'
# where the computation will happen
rootpath = '/scratch/{}/tutorial/arrays/'.format(username)


def parameter_generator():
    """Return a dict of index -> parameters"""
    params = {}
    index = 0
    for rand_max in [1.0, 100.0, 1000.0]:
        for rand_min in [-1.0, -5000.0]:
            params[index] = {'max': rand_max, 'min': rand_min}
            index += 1
    return params


def write_configs():
    """Write the parameter configuration files, one for each job"""
    for index, params in parameter_generator().items():
        configpath = os.path.join(rootpath, 'config_{}.json'.format(index))
        with open(configpath, 'w') as f:
            json.dump(params, f)


def check_missing():
    """Check if allo jobs finished correctly"""

    print('Checking for missing results files...')

    # find missing files
    missing = set()
    for idx, params in enumerate(parameter_generator()):
        for filepath in [os.path.join(rootpath, 'results_{}.json'.format(idx))]:
            if not os.path.exists(filepath):
                print('error: `{}` not found'.format(filepath))
                missing.add(idx)


    if len(missing) > 0:
        # generate command for incomplete jobs
        missing = sorted(missing)
        array_idx = []
        for i, idx in enumerate(missing):
            if i != 0 and missing[i-1] == idx - 1:
                array_idx[-1].append(idx)
            else:
                array_idx.append([idx])
        cmd_idx = []
        for idx in array_idx:
            if len(idx) == 1:
                cmd_idx.append('{}'.format(idx[0]))
            else:
                cmd_idx.append('{}-{}'.format(idx[0], idx[-1]))
        cmd = './run_array.sh {}'.format(','.join(cmd_idx))
        print("\nTo run incomplete jobs (assuming no job is still running), run:\n{}".format(cmd))
    else:
        print('All present!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', action='store_true', default=False)
    parser.add_argument('--count', action='store_true', default=False)
    parser.add_argument('--check', action='store_true', default=False)
    args = parser.parse_known_args()[0]

    if args.path:
        print(rootpath)
    elif args.count:
        print(len(parameter_generator()) - 1)
    elif args.check:
        check_missing()
    else:
        write_configs()
