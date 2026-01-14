<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<img alt="Ubuntu Package Version" src="https://img.shields.io/ubuntu/v/ubuntu-wallpapers">

<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ who | wc -I
$ id
$ whoami
$ hostnamectl
```

(ssh localhost)
```bash
$ who
user     tty2         2025-11-30 00:31 (tty2)
user     pts/5        2025-12-01 03:57 (127.0.0.1)
```

```bash
$ id
uid=1000(user) gid=1000(user) groups=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),134(lxd),135(sambashare),999(docker)
```
Выводится:
- id пользователя (uid)
- группа пользователя (gid)
- группы в которых состоит пользователь

```bash
$ whoami
user
```
вывод имени пользователя

```bash
$ hostnamectl
 Static hostname: production
       Icon name: computer-vm
         Chassis: vm
      Machine ID: af929eab89bd477e9120fab4fb6a451e
         Boot ID: 7d690ffe01e9441d905ba8d8a5a511f2
  Virtualization: oracle
Operating System: Ubuntu 22.04.5 LTS              
          Kernel: Linux 6.8.0-87-generic
    Architecture: x86-64
 Hardware Vendor: innotek GmbH
  Hardware Model: VirtualBox
```

информация о системе

- [x] 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.

```bash
$ tree -L 1 -d ~/
/home/user/
├── CLionProjects
├── Desktop
├── Documents
├── Downloads
├── go
├── goprj
├── Music
├── Pictures
├── production-server-main
├── Public
├── semaphore
├── snap
├── Templates
└── Videos
```
- `-L 1` - глубина
- `-d` - только директории

- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.

```bash
$ sudo file -s /dev/sda3
/dev/sda3: Linux rev 1.0 ext4 filesystem data, UUID=c61eb2d7-856c-4d47-9a5e-f117b36edf32
```
- `-s` - просмотр устройств

```bash
$ df -h -T /dev/sda3
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda3      ext4   39G   29G  7,8G  79% /
```
- `-h` - human readable
- `-T` - показать тип ФС

- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi
$ locate hello.py
$ sudo updatedb
$ locate hello
$ touch screen
$ find ~ -name screen
$ locate screen
$ sudo updated
$ locate screen
```

```bash
$ which vi
/usr/bin/vi

$ echo $PATH
/home/user/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/user/go/bin:/home/user/goprj/bin
```
Поиск исполняемого файла в $PATH

```bash
$ locate hello.py
/home/user/Documents/RISKI/course_labs/labs/lab02/exmpl_hello.py
/home/user/Documents/RISKI/course_labs/labs/lab05/source/hello.py
/home/user/Documents/RISKI/lab01/hello.py
/home/user/Documents/blockchain/hello-world/deploy_hello.py
/snap/gnome-3-38-2004/112/usr/lib/x86_64-linux-gnu/peas-demo/plugins/pythonhello/pythonhello.py
...
```
Поиск `hello.py` в `/var/lib/plocate/plocate.db`

```bash
$ sudo updatedb
```
Обновление `/var/lib/plocate/plocate.db`

```bash
$ touch screen
-rw-rw-r-- 1 user user    0 дек  1 04:29 screen
```
Создание файла `screen`

```bash
$ find ~ -name screen
/home/user/Documents/RISKI/course_labs/labs/lab02/screen
```

Поиск в `~` файла `screen`

```bash
$ locate screen | grep RISKI
/home/user/Documents/RISKI/course_labs/labs/lab02/screen
```


- [x]  5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

```py
import pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
pygame.display.set_mode(window_size) # Создаем окно

# Задаем цвет фона
bg_color = (255, 255, 255)
pygame.draw.rect(screen, bg_color, [0, 0, screen_width, screen_height], 1)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
pygame.display.flip() # Обновляем экран
```

- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.
```bash
git commit -S -m "lab2.6"
```
- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups
$ useradd smallman
$ userdel smallman -rf
$ useradd smallman
$ passwd smallman
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ passwd smallman
$ id smallman
$ groupadd -g 1500 readgroup
$ usermod -aG readgroup smallman
$ chmod 666 screen 
```

```bash
$ groups
user adm cdrom sudo dip plugdev lpadmin lxd sambashare docker
```

Список групп

```bash
$ useradd smallman
```
Создает пользователя без домашней папки и пароля

```bash
$ userdel smallman -rf
userdel: smallman mail spool (/var/mail/smallman) not found
userdel: smallman home directory (/home/smallman) not found
```

Удаляет пользователя
- `-r` - удаление домашней папки (ошибки)
- `-f` - force - даже если залогинен

```bash
$ useradd smallman
$ passwd smallman

New password: 
BAD PASSWORD: The password is shorter than 8 characters
Retype new password: 
passwd: password updated successfully
```

Установка пароля для пользователя

```bash
$ sudo usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
$ getent passwd smallman 

smallman:x:1502:1502:Hach Hachov Hacherovich,239,45-67,499-239-45-33:/home/smallman:/bin/sh
```

Изменяет комментарий для пользователя

```bash
uid=1502(smallman) gid=1502(smallman) groups=1502(smallman),1600(readgroup)
```

smallman добавлен в `readgroup`

- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.

```
-rw-rw-rw- 1 user user 0 дек  1 04:29 screen

$ sudo chgrp readgroup screen
$ ls -la screen 
-rw-r----- 1 user readgroup 0 дек  1 04:29 screen
```
- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt
$ setfacl -m u:smallman:rw nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt
$ getfacl nmapres.txt

# file: nmapres.txt
# owner: user
# group: user
user::rw-
user:smallman:rw-
group::rw-
group:readgroup:r--
mask::rw-
other::r--
```

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.

```bash
$ getent group | cut -d: -f1
root
daemon
bin
sys
adm
tty
disk
...
```

- `getent group` - получить записи из /etc/group
- `cut -d:` - обрезать по разделителю `:`
- `-f1` - вывести первое поле

- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)

```
$ cd ~/Documents/RISKI/course_labs && tree -a -p -u -g -I '.git'

[drwxrwxr-x user     user    ]  .
├── [-rw-rw-r-- user     user    ]  APPENDIX.md
├── [drwxrwxr-x user     user    ]  artifacts
│   ├── [drwxrwxr-x user     user    ]  art_cheatsheet
│   │   ├── [-rw-rw-r-- user     user    ]  Docker_Image_Security_Best_Practices.pdf
│   │   └── [-rw-rw-r-- user     user    ]  gitscm.jpg
│   ├── [drwxrwxr-x user     user    ]  cheatsheet
│   │   ├── [-rw-rw-r-- user     user    ]  CHEATSHEET_DOCKERIGNORE.md
│   │   ├── [-rw-rw-r-- user     user    ]  CHEATSHEET_DOCKER.md
│   │   ├── [-rw-rw-r-- user     user    ]  CHEATSHEET_GH_CLI.md
│   │   ├── [-rw-rw-r-- user     user    ]  CHEATSHEET_GITIGNORE.md
│   │   └── [-rw-rw-r-- user     user    ]  CHEATSHEET_GIT.md
│   ├── [drwxrwxr-x user     user    ]  exmpls
│   │   ├── [-rw-rw-r-- user     user    ]  Аналитический отчет по уязвимости PrintNightmare.pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Пример - Multisignature - Безопасности криптовалютных платежей.pdf
│   │   └── [-rw-rw-r-- user     user    ]  Пример_аналитических_отчетов_по_задачам_ИБ.pdf
│   ├── [drwxrwxr-x user     user    ]  owasp
│   │   ├── [-rw-rw-r-- user     user    ]  OWASP_Top_10_CICD_Risks.pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Авторизация (Authorization).pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Атаки на клиентов (Client-side Attacks).pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Аутентификация (Authentication).pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Выполнение кода (Command Execution).pdf
│   │   ├── [-rw-rw-r-- user     user    ]  Логические атаки (Logical Attacks).pdf
│   │   └── [-rw-rw-r-- user     user    ]  Разглашение информации (Information Disclosure).pdf
│   └── [drwxrwxr-x user     user    ]  ppt
│       └── [-rw-rw-r-- user     user    ]  Лекция_Управление Рисками ИБ_intro.pdf
├── [drwxrwxr-x user     user    ]  assets
│   ├── [drwxrwxr-x user     user    ]  logotype
│   │   ├── [-rw-rw-r-- user     user    ]  logo2.jpg
│   │   └── [-rw-rw-r-- user     user    ]  logo.jpg
│   └── [drwxrwxr-x user     user    ]  style
│       └── [-rw-rw-r-- user     user    ]  style.css
├── [-rw-rw-r-- user     user    ]  CODE_OF_CONDUCT.md
├── [-rw-rw-r-- user     user    ]  CONTRIBUTING.md
├── [-rw-rw-r-- user     user    ]  .dockerignore
├── [-rw-rw-r-- user     user    ]  .gitattributes
├── [-rw-rw-r-- user     user    ]  .gitignore
├── [drwxrwxr-x user     user    ]  labs
│   ├── [drwxrwxr-x user     user    ]  lab01
│   │   ├── [-rw-rw-r-- user     user    ]  README.md
│   │   └── [-rw-rw-r-- user     user    ]  typersteel.py
│   ├── [drwxrwxr-x user     user    ]  lab02
│   │   ├── [-rw-rw-r-- user     user    ]  exmpl_hello.py
│   │   ├── [-rw-rw-r-- user     user    ]  nmapres.txt
│   │   ├── [-rw-rw-r-- user     user    ]  pygamesteel.py
│   │   ├── [-rw-rw-r-- user     user    ]  README.md
│   │   └── [-rw-r----- user     readgroup]  screen
│   ├── [drwxrwxr-x user     user    ]  lab03
│   │   ├── [-rw-rw-r-- user     user    ]  exmp_targets.txt
│   │   └── [-rw-rw-r-- user     user    ]  README.md
│   ├── [drwxrwxr-x user     user    ]  lab04
│   │   └── [-rw-rw-r-- user     user    ]  README.md
│   ├── [drwxrwxr-x user     user    ]  lab05
│   │   ├── [drwxrwxr-x user     user    ]  client
│   │   │   ├── [-rw-rw-r-- user     user    ]  client.py
│   │   │   ├── [-rw-rw-r-- user     user    ]  Dockerfile
│   │   │   └── [-rw-rw-r-- user     user    ]  requirements.txt
│   │   ├── [-rw-rw-r-- user     user    ]  docker-compose.yml
│   │   ├── [-rw-rw-r-- user     user    ]  README.md
│   │   ├── [drwxrwxr-x user     user    ]  server
│   │   │   ├── [-rw-rw-r-- user     user    ]  app.py
│   │   │   ├── [-rw-rw-r-- user     user    ]  Dockerfile
│   │   │   └── [-rw-rw-r-- user     user    ]  requirements.txt
│   │   └── [drwxrwxr-x user     user    ]  source
│   │       ├── [-rw-rw-r-- user     user    ]  Dockerfile
│   │       ├── [-rw-rw-r-- user     user    ]  hello.py
│   │       └── [-rw-rw-r-- user     user    ]  requirements.txt
│   └── [drwxrwxr-x user     user    ]  lab06
│       └── [-rw-rw-r-- user     user    ]  README.md
├── [-rw-rw-r-- user     user    ]  LICENSE.md
├── [-rw-rw-r-- user     user    ]  NOTICE.md
├── [-rw-rw-r-- user     user    ]  README.md
└── [-rw-rw-r-- user     user    ]  SECURITY.md
```

- `-a` - все файлы включая скрытые
- `-p` - права доступа
- `-u` - владелец
- `-g` - группа
- `-I '.git'` - исключить `.git'`

- [ ] 13. Выведите процессы которые у вас запущены в термине и вне его.
```bash
$ ps -ef --forest | grep $$
user      318294  318293  0 03:57 pts/5    00:00:00          \_ -bash
user      371954  318294  0 05:30 pts/5    00:00:00              \_ ps -ef --forest
user      371955  318294  0 05:30 pts/5    00:00:00              \_ grep --color=auto 318294
```

- `-e` - Все процессы
- `-f` - полный формат
- `--forest` - деревом
- `$$` - PID терминала

***

## Links

- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)
- [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
- [cd](https://en.wikipedia.org/wiki/Cd_(command))
- [cp](https://en.wikipedia.org/wiki/Cp_(Unix))
- [echo](https://en.wikipedia.org/wiki/Echo_(command))
- [env](https://en.wikipedia.org/wiki/Env_(shell))
- [file](https://en.wikipedia.org/wiki/File_(command))
- [ls](https://en.wikipedia.org/wiki/Ls)
- [mkdir](https://en.wikipedia.org/wiki/Mkdir)
- [mv](https://en.wikipedia.org/wiki/Mv)
- [ps](https://en.wikipedia.org/wiki/Ps_(Unix))
- [pwd](https://en.wikipedia.org/wiki/Pwd)
- [rm](https://en.wikipedia.org/wiki/Rm_(Unix))
- [touch](https://en.wikipedia.org/wiki/Touch_(Unix))
- [apt](http://help.ubuntu.ru/wiki/apt)
- [brew](https://brew.sh)
- [npm](https://docs.npmjs.com)

Copyright (c) 2025 Elijah S Shmakov

![Logo](../../assets/logotype/logo.jpg)