# Steps for setting up functional smoke test - Selenium in python (including docker)
Setup the selenium and dependent executable libraries from section below.
Smoke test can be executed either in local machine (headless and UI) or docker container/environment (headless)

# Local machine selenium python test environment setup 
1. Launch Power shell to install and setup
2. Python should be installed (3.7 or more),
3. VS Code/any suitable editor should be installed to view/modify the code/settings
4. python --version should show a valid installation version
5. pip install -r requirements.txt (would download selenium and other libraries necessary to run test) 
6. Verify the libraries installed using 'pip list' command 
7. Download the latest scalar code from GitHub in local
8. Open the GitHub downloaded code (verification-scripts/smokeTest2.2)
9. Use /resources/config_variables.json to update user credentials or any of below settings
10. Using the webpage https://www.base64encode password should be encrypted 
11. Save all the changes before execution

# Docker local machine setup 
1. Docker Desktop (community version) needs to be setup in local
2. Verify installation using 'docker --version' 
3. Ensure your credentials added to docker-users group
4. 'selenium/standalone-chrome' image needs be pulled from docker hub using command:
   docker pull selenium/standalone-chrome
5. stop all running containers selenium/standalone-chrome and run below command:
   docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:latest

# Local machine execution 
## UI Execution
1. To execute in normal UI (visual) mode, edit 'is_normal_headless' as well as 'is_docker_headless' variables both to 'False' 
2. Launch 'Power shell' and 'change directory' to verification-scripts/smokeTest2.2
3. Run command 'python3.9 smoketest.py' to view the execution launching in you monitor
4. Verify test execution status under section 'Test Report and validation'

## Headless execution
1. To execute in normal headless mode, edit 'is_normal_headless' variable to 'True' and 'is_docker_headless' variable value to 'False'
2. Launch 'Power shell' and 'change directory' to verification-scripts/smokeTest2.2
3. Run command 'python smoketest.py' (execution occurs silent in background)
4. Verify test execution status under section 'Test Report and validation'

## Docker execution
1. To run test in dockerized headless mode, change 'is_docker_headless' variable value to 'True'
2. Run below commands from project folder directory path 
   (a) docker build -t smoke-test-client .  (Builds the code as client for recent changes done in VS Code editor)
   (b) docker run -it smoke-test-client (Runs the client )
3. Verifying the test execuiton needs to be done while test is in progress using command: 
   docker exec -it <container-id> sh and do ls (directory list) > and navigate to respective folders to verify test execution status under section 'Test Report and validation'

## For debug purpose in docker one can use below commands
1. docker ps
2. docker inspect <conainer-id>
3. docker exec -it <container-id> sh (while execution inprogress) and then do ls (directory list) > and navigate to respective folders to verify
4. docker run -it smoke-test-client /bin/bash (one can execute the test inside the container)
5. docker system prune (to clear cache of docker - dangling images and free memory)
6. docker restart <container_id> to restart the docker container in case of TimeOut or unable to start session issues etc.

# Test Report and validation
1. Open text file under 'run_logs' folder to know the status (Pass/Fail having exception) 
2. Open 'output_screenshots' to have 3 screenshot files single and 2 parameter graphs of Summary page
