# 0x05. Processes and signals

## Tasks

### 0. What is my PID

Write a Bash script that displays its own PID. </br>

File:[0-what-is-my-pid](0-what-is-my-pid)

### 1. List your processes

Write a Bash script that displays a list of currently running processes. </br>

Requirements:

  - Must show all processes, for all users, including those which might not have a TTY
  - Display in a user-oriented format
  - Show process hierarchy </br>

File:[1-list\_your\_processes](1-list_your_processes)

### 2. Show your Bash PID

Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. </br>

Requirements:

  - You cannot use pgrep
  - The third line of your script must be # shellcheck disable=SC2009 </br>

File:[2-show\_your\_bash\_pid](2-show_your_bash_pid)

### 3. Show your Bash PID made easy

Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash. </br>

Requirements:

  - You cannot use ps </br>

File:[3-show\_your\_bash\_pid\_made\_easy](3-show_your_bash_pid_made_easy)

### 4. To infinity and beyond

Write a Bash script that displays To infinity and beyond indefinitely. </br>

Requirements:

  - In between each iteration of the loop, add a sleep 2 </br>

File:[4-to\_infinity\_and\_beyond](4-to_infinity_and_beyond)

### 5. Don't stop me now!

We stopped our 4-to\_infinity\_and\_beyond process using ctrl+c in the previous task, there is actually another way to do this. </br>

Write a Bash script that stops 4-to\_infinity\_and\_beyond process. </br>

Requirements:

  - You must use kill </br>

File:[5-dont\_stop\_me\_now](5-dont_stop_me_now)

### 6. Stop me if you can

Write a Bash script that stops 4-to\_infinity\_and\_beyond process. </br>

Requirements:

  - You cannot use kill or killall </br>

File:[6-stop\_me\_if\_you\_can](6-stop_me_if_you_can)

### 7. Highlander

Write a Bash script that displays:

  - To infinity and beyond indefinitely
  - With a sleep 2 in between each iteration
  - I am invincible!!! when receiving a SIGTERM signal

Make a copy of your 6-stop\_me\_if\_you\_can script, name it 67-stop\_me\_if\_you\_can, that kills the 7-highlander process instead of the 4-to\_infinity\_and\_beyond one.

File:[7-highlander](7-highlander)

### 8. Beheaded process

Write a Bash script that kills the process 7-highlander. </br>

File:[8-beheaded\_process](8-beheaded_process)

