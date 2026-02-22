For miss configuration example I'm gonna use ftp anon login, it doesn't have to be a bad thing all the time, but if we add upload option or put some credentials in the ftp directory it will be a vulnerability.

For the vulnerable ftp server to be set we need to:
1. Install the vsftpd to put up the ftp server `sudo apt install vsftpd`
2. Create the directory that will be the anon_root for our ftp server`mkdir ftp` , it has to have specific permissions for the upload to be possible `chmod 777 ftp`
3. Put an example file inside this directory `echo example > ftp/example.txt`
4. Add the following lines to the config file located in /etc/vsftpd.conf
```cmd
anonymous_enable=YES # this lets anonymous login for the server (login: "anonymous", password "")
anon_root=/home/serverowasp/ftp # sets the directory of the anonymous user.
write_enable=YES # enables writting files in ftp
anon_upload_enable=YES # anonymous user can upload files 
anon_mkdir_write_enable=YES # anonymous user can make directories
```
3. Then we can just run the server `sudo systemctl enable vsftpd` if its already up we need to restart it to load the config `sudo systemctl restart vsftpd`
4. We can connect to the ftp server and check if the files are loaded `ftp <ip of your ftp server>
5. Try to get the example.txt file `get example.txt` and put a file in there `put example2.txt`

### What is *Security Missconfiguration*
It occurs when system are deployed with default settings, unnecessary features enabled, or improper access controls.
In this case, the FTP server allows anonymous authentication and grants file upload permissions. This configuration exposes internal resources without requiring valid credentials.

### Missconfigration details
It is very insecure cause a threat actor can get into our system and get very important credentials that can get him into the network or put a file that may compromise it. 

```
anonymous_enable=YES
writable_enable=YES
anon_upload_enable=YES
```

This configuration violates the principle of least privilege by granting unrestricted access to unauthenticated users.

### Exploitation steps
1. Connect to FTP `ftp <ip of your ftp server>
2. Enter the `login: anonymous password:` 
3. Check whats in the directory you're in `ls -la`
4. Download the file u found inside of there `get example.txt`
5. Upload something inside of the server `put example-upload`
This demonstrates that unauthenticated users can access and modify server files.

### Impact
If exploited, this missconfiguration may result in:

 - Unauthorized access to sensitive files

- Exposure of credentials or configuration data

- Upload of malicious files

- Hosting of malware or illegal content

- Potential pivoting point for further attacks

If sensitive configuration files are stored in the FTP directory, attackers may escalate privileges or compromise the entire system.

### Mitigation 
To mitigate the vulnerability: 
1. Disable anonymous login `anonymous_enable=NO`
2. Remove upload permission for anonymous users `anon_upload_enable=NO`
3. Restrict directory permissions (use `chmod` for it and change it for your liking)
4. Apply a firewall rules
5. If you really wanna use anonymous login remember to follow the least privilege principles and configure your ftp server well

### Educational note
This configuration was intentionally deployed in a controlled lab environment for educational purposes.
I personally was shocked when ive found out some people really missocnfigure their servers like that, and I'd understand if u did too, but keep in mind that there are some developers that change the configuration for testing and forgot to change it back. Its just a usual human factor.

