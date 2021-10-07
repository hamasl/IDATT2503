# Task 5
Task is to fuzzer test the edit function in the string_editor.h file, and corre3ct the mistakes found. This should be done via Gitlab-CI.

## Running CI
### On gitlab
To run ci on gitlab just push the project, and gitlab should automatically run CI.

### Locally
Install gitlab-runner through
```
wget https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb
sudo dpkg -i gitlab-runner_amd64.deb
```
To run fuzzer testing use:
```
sudo gitlab-runner exec docker fuzzer-testing
```

To run manual testing use:
```
sudo gitlab-runner exec docker manual-testing
```
