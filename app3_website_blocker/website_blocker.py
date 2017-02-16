import time
from datetime import datetime as dt

hosts_temp ="hosts"
hosts_path="/etc/hosts" # or hosts_path=r"C\Windows\System32\drivers\etc\hosts" for windows
redirect="127.0.0.1"

# add list of website that you want to block
website_list=["www.facebook.com","facebook.com"]


#Using while loop so the script is constantly running
while True:
    # if statment to check if the current time is within working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours between 9 and 5")

        #open hosts file and read contents
        with open(hosts_path, 'r+') as file:
            content=file.read()

            # check if websites are already in the file
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0) #pointer goes to the beginning of file content.

            # check each line for content of websites are in host file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Fun hours")
    time.sleep(5)


# to implement in background use sudo crontab -e & add line : @reboot python3 /home/alexl/vagrant/python_megacourse/app3_website_blocker
