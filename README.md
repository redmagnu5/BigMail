# BigMail
Console app for sending bulk email.

```bash
                              ________________________________
                                ____  _       __  __       _ _
                               | __ )(_) __ _|  \/  | __ _(_) |
                               |  _ \| |/ _` | |\/| |/ _` | | |
                               | |_) | | (_| | |  | | (_| | | |
                               |____/|_|\__, |_|  |_|\__,_|_|_|

                               ________ |___/ Mass Mailer _____
                                Author: redmagnu5@github.com

                              Email list must be a basic text file (.txt) and have the
                              following structure:

                                       user@domain
                                       user2@domain
                                       user3@domain
                                         .....



                              PLEASE DO NOT USE FOR SPAMMING
```

## Installation
Clone the repo:
```bash
      git clone https://github.com/redmagnu5/BigMail.git
```
Change directory:
```bash
      cd BigMail
```
```bash
      python3 setup.py install
```

## Usage
```bash
      cd Bigmail
```
```bash
      python3 bigmail.py
```

Email template must be configured in config.yaml located the module directory:
BigMail/config.yaml. Specify From, Subject, name of attachment, and body of the
email here.


Optional arguments:

-v verbose, verbose
-p filepath, file path of binary payload to attach to emails
