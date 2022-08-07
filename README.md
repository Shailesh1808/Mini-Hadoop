# Yet-another-Hadoop-BD2_020_059_307_319
###### Big Data Project for Semester 5
The commands for our YAH project are:

-------SETTING UP THE NEW DFS--------------<br>
sudo python3 hdfs.py -setup <config file><br><br>
  
-------LOADING AN EXISTING DFS--------------<br>
sudo python3 hdfs.py -load <dfs_config file><br><br>
  
-------MAKING A NEW DIRECTORY IN THE FILE SYSTEM---------<br>
sudo python3 hdfs.py -mkdir <directory name><br><br>

-------STORING A FILE IN THE CREATED DIRECTORY IN THE FILE SYSTEM-------<br>
sudo python3 hdfs.py -put <file_path> <directory name><br><br>

-------DISPLAY THE CONTENTS OF THE STORED FILE------------<br>
sudo python3 hdfs.py -cat <path of file in filesystem><br><br>
  
-------REMOVING A FILE FROM THE FILE SYSTEM---------------<br>
sudo python3 hdfs.py -rm <path of file in filesystem><br><br>
  
-------REMOVING A DIRECTORY FROM THE FILE SYSTEM-------------<br>
sudo python3 hdfs.py -rmdir <directory name><br><br>
  
-------LISTING ALL THE FILES IN A DIRECTORY------------------<br>
sudo python3 hdfs.py -ls [optional- directory name]
