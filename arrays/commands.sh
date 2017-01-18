# command to run to use the code

python prepare.py --check # check that result files are present (they are not)
python prepare.py # write config files
./run_array.sh # launch the job array
qstat -u fbenurea # check the status of your job array
qstat -u fbenurea # check the status of your job array
python prepare.py --check # check (again) that result files are present
