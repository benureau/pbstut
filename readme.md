This is a small tutorial to show how to use the MCIA Avakas cluster, and in particular job arrays.

# First!

To connect to the cluster, use ssh.

## Generate a Key

On your *local* machine, replacing the email by yours:
```
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

## SSH Config

To allow you to connect to avakas by simply typing `ssh avakas`, modify your `~/.ssh/config` file by adding the following lines:

```
Host avakas
    User fbenurea
    HostName avakas.mcia.univ-bordeaux.fr
    IdentityFile ~/.ssh/id_rsa
    IdentitiesOnly=yes
```

Replace `fbenurea` by *your username* given to you to connect to avakas.

## Tips: Kill a SSH Session

Sometimes, ssh connections are interrupted (e.g. when you loose internet), and can seem stuck. To immediately kill a ssh connection, type:

```
<Enter> + '~' + '.'
```

## Sending and Receiving Files

To send files to avakas, assuming you did follow the "SSH Config" step above, you can use the `ssh/push.sh` script.
```
cd ssh/
./push.sh
```

To get results files from avakas, after the jobs have finished, the `ssh/pull.sh` script is provided. Do first modify it by replacing my username (the same as the ssh config) by yours.
```
cd ssh/
./pull.sh
```


# Simple Job

In the `simple/` directory, you'll find the a minimalistic set of files to run a job on Avakas.

1. Go to the simple directory: `cd simple/`
2. Modify the `job.pbs` file to set your username and queue name.
3. Push your changes to avakas: `./push.sh`
4. Go to avakas: `ssh avakas`
5. Go to the tutorial directory on avakas: `cd ~/tutorial/simple`
6. Submit your job: `qsub job.pbs`
7. Monitor the state of your jobs with qstat `qstat -u <your_username>`
8. When the previous command does not show anything, your job has finished (or crashed).
9. This job does not produce any result files, but `.out` and `.err` files should have been created in the current directory, logging the standard and error output (respectively) of the script.

# Array Job

```
cd arrays/
```

Job arrays are more complex. Here we create a set of configuration files, that describes the different parameters for each job of the job array we want to launch. After you correctly set your username and queues in `job_array.pbs`, to create the config files, do:

To launch the job array:
```
./run_array.sh
```
You notice that the job array is submitted instantaneously, it does not take longer with more jobs in it.

Use `qstat` to monitor the state of your job array:
```
qstat -u <your_username>
```
To see jobs individually:
```
qstat -nltu <your_username>
```


After `qstat` reports no ongoing jobs, to check that the results file have been correctly produced, use:
```
python prepare.py --check
```

That's all folks!
