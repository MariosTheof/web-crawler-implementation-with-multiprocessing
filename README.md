# A concurrent web crawler that downloads webpages.
A cli crawler implementation that downloads websites, with multithreading written in python. I chose threads because I/O to disk or to network can have unpredictable delays.
Threads allow you to ensure that I/O latency does not delay unrelated parts of your application. The crawling was done with the requests library and BeautifulSoup4 for parsing the html. The download itself was done with wget, even though download_files.py almost has the same functionality.  
I choose to use wget instead because the --timestamp flag allowed the program to speed up as it did not have to re-download every file, but at the same time if a file with the same
name changed it would check the timestamp and download it anew.
The end result will be a folder with all the files needed to view the site locally.

The user can specify the depth that the crawler will go to, 
it is however recommended that depth is kept to around 2-3, as the volumes of pages that need to be downloaded can become huge.

The user can also specify the number of threads/workers that will work on the task of crawling through a website and downloading it. Their numbers can sometimes drastically improve 
the program's efficiency. 
For example :

Lastly, the user can choose a website of his choosing to download.




### How to build
```
1. Clone repo into a folder
2. Create image with dockerfile :
sudo docker build -t yourusername/parallelwebcrawl
```
### How to run

1. Run container in interactive with interactive shell : 
sudo docker run -it yourusename/parallelwebcrawl
or you can do sh as well.
2. Answer the questions from the command line. (make sure to give a valid url) 
If you used the 'sh' option container shell run : 
  python ./cmd_application.py
3. When the program finishes (it might take 1 or 2 minutes), it creates a folder in the container for all the websites that were downloaded (html,css,js,img etc.)
4. In order to transfer it to the host(locally), we use the command :
sudo docker cp *container_name*:/usr/src/app/*website_name* .

#### Example run :
```
1. sudo docker run -it --name gates1 captainmarios/parallelwebcrawl
2. ** Answer cmd promts * 
  > 2
  > 5
  > https://www.gatesnotes.com
3. Wait for program to finish.
3. sudo docker cp gates1:/usr/src/app/www.gatesnotes.com .
4. View the downloaded folder in my local directory.
```
## How can it be improved
- Add flag options.
- Extend cli inteface. Maybe add the option for time limit
-  URL validity checker.
- Use processes instead of multithreading.
