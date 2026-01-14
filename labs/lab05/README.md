<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

***

Салют :wave:,<br>
Данная лабораторная работа посвещена изучению Docker и как с ним работать. Эта лабораторная работа послужит подпоркой для старта в выявлении и определении уязвимостей на уровне сканирования контейнеров при сборке приложений. 

Для сдачи данной работы также будет требоваться ответить на дополнительыне вопросы по описанным темам.

***

## Структура репозитория лабораторной работы

```bash
lab05
├── client
│   ├── client.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── README.md
├── server
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── source
    ├── Dockerfile
    ├── hello.py
    ├── image.tar
    └── requirements.txt
```

***

## Материал

- **Контейнеризация**

Сборка приложения включает создание контейнерного образа, в котором упаковано приложение с конфигурациями, что бы приложение функционировало. `Docker` основан на использовании общих функций ядра `ОС Linux` (`cgroups`, `namespace`) для изоляции и управления ресурсами.

> **Образ** — это статический, неизменяемый шаблон, на базе которого создаются контейнера с ОС, приложением, зависимостями, библиотекакм и конфигурационными файлами. Нужен для создания воспроизводимой, неизменяемой среды выполнения приложений в контейнерах.

Для сборки образов используется `Dockerfile`, где прописаны версии зависимостей и инструкции, минимизирующие разрешения и атаки. Это инструкции, где описывается, как собрать образ. Впоследствии собирается контейнер.

> **Контейнер** — это изолированная среда выполнения приложения с необходимыми зависимостями, кодом, системными утилитами, библиотеками и настройками. Исползует не собственну гостеву ОС, а ядро хостовой ОС и имеет своё собственное файловое пространство, процессы и сеть.

После сборки образа формируется контейнер, которые являются изолированными средами выполнения для достижения цели переносимости, воспроизведения.

> **Контейнеризация** — это технология, позволяющая упаковать приложение вместе со всеми его зависимостями, библиотеками, настройками и средой выполнения в единый изолированный виртуальный контейнер. 

- **Namespaces**

Необходимы для организации изолированных рабочих пространств, - контейнеров. Когда мы запускаем контейнер, `Docker` создает набор пространств имен для данного контейнера, что создает изолированный уровень в своем простанстве имен и не имеет доступа к внешней системе. Пространство имен:

> - pid: для изоляции процесса
> - net: для управления сетевыми интерфейсами
> - ipc: для управления IPC ресурсами. (ICP: InterProccess Communication)
> - mnt: для управления точками монтирования
> - utc: для изолирования ядра и контроля генерации версий(UTC: Unix timesharing system)

- **Cgroups**

Необходимы для контрольных групп в изоляции, где предоставляется приложению только те ресурсы, которые указываем. Позволяют разделять ресурсы железа и устанавливать пределы, ограничения.

```bash
$ docker container run d \
        —e NGINX_HOST xxx.xxx \
        —p 8080:80 \
        –-v "$PWD/html" usr/share/nginx/html \
        —memory=50m \
        —cpus="2.5" \
        nginx
```

-  **Основные проблемы**

    - образ может содержать устаревшие или уязвимые версии библиотек CVE (Common Vulnerabilities and Exposures)
    - поддельные и злонамеренные образы
    - отсутствие подписей и проверки целостности
    - ошибка конфигурации и избыток прав — образы с избыточными правами доступа, запуском от root или с небезопасными настройками
    - присутствие секретов и конфиденциальных данных в образах
    - отсутствие регулярного обновления из-за неподдерживаемых образов

-  **Контекст безопасности**

    - Не задавать пользователей с правами «root» для работы сервисов внутри контейнеров. 
        > Если для функционирования сервиса не требуются расширенные привилегии, то в Dockerfile необходимо явно прописать учетную запись пользователя с минимально необходимыми правами.
    - Не запускать контейнеры в привилегированном режиме. 
        > Ключ «--privileged» отключает все средства изоляции (наложенные cgroup – контроллером устройства) docker-контейнера. Запуск контейнера с таким ключом обеспечит ему доступ к файловой системе и блочным устройствам (например, жесткому диску) хоста. Контейнеры должны быть запущены в непривилегированном режиме. Если контейнеру нужны дополнительные привилегии для корректной работы, то необходимо явно прописать или удалить требуемые docker capabilities.
    - Не отключать профили безопасности Docker. 
        > По умолчанию для запуска контейнеров Docker использует профили безопасности Linux, лучше использовать профили AppArmor, SELinux, grsecurity, seccomp, - позволяют ограничить активности контейнера, обеспечивая контроль сети, использования дополнительных возможностей (docker capabilities), контроль обращений к файловой системе хоста и пр. Контейнеры должны работать с активными профилями безопасности Docker, не docker-default. Если необходимо использовать другой профиль, то это можно сделать с помощью --security-opt.
    - Не допускать запуск контейнеров, использующих тип сети «host»
        > В режиме Host контейнер использует ту же сеть, что и хост, т.е. контейнерная сеть не изолируется от сети Docker хоста и контейнер не получает собственный IP-адрес, что дает доступ к REST API daemon docker изнутри контейнера, а также к устройствам, расположенным в сети хоста. Для реализации сетевого взаимодействия между контейнерами, они должны запускаться в режиме bridge или none.
    - Не разрешать доступ к docker.socket изнутри контейнера. Не подключать docker socket в контейнер без необходимости, либо с использованием плагинов авторизации. 
    - Не использовать секреты в открытом виде в Docker-файлах образов. По возможности не использовать переменные окружения и не хранить секреты внутри контейнера. Хранение и управление секретами возложить на сторонний сервис.
    - Ограничивать и контролировать использование ресурсов контейнерами. Указывать ограничения на уровне самого ПО или на уровне контейнеров для использования ресурсов хоста.
    - Контролировать качество базовых образов контейнеров. Использовать официальные образы и использовать образы с минимально необходимым набором инструментов.
    - Сканировать образы на наличие уязвимостей и проверки требований ИБ (Compliance Checks)

- **Дополнительно**

В случае, если возникает проблема с вызовом `docker buildx` для macos `silicon`, следует использовать вот [это](https://gist.github.com/Aeonitis/cbd9f8b61eaec5a8a024c0a42f415ca3) описание из gistup для фикса `samelink`.

***

## Задание

- [x] 1. Поставьте `Docker` и `buildkit`

```bash
$ brew install buildkit
$ brew install docker
```

- [x] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
# 1. Собираем образ с помощью Buildx (рекомендуемый способ в современных версиях Docker)
#    -t hellow-appsec-world  → задаём имя и тег образа
#    .                       → используем текущую директорию как контекст сборки (там должен быть Dockerfile)
docker buildx build -t hellow-appsec-world .

# 2. Запускаем контейнер из только что собранного образа
#    По умолчанию запустится команда, указанная в Dockerfile (CMD / ENTRYPOINT)
docker run hello-appsec-world

# 3. Запускаем контейнер в интерактивном режиме с терминалом
#    --rm      → автоматически удалить контейнер после завершения
#    -it       → интерактивный режим + псевдотерминал (можно работать внутри как в обычной консоли)
docker run --rm -it hello-appsec-world

# 4. Сохраняем образ в tar-архив (один из способов передать образ на другую машину без реестра)
#    -o hello.tar          → имя выходного файла
docker save -o hello.tar hello-appsec-world

# 5. Загружаем образ из tar-архива обратно в локальный docker
#    Очень полезно при переносе образа между серверами/машинами без интернета/реестра
docker load -i hello.tar
```

```
$ docker buildx build -t hello-appsec-world .
[+] Building 32.2s (13/13) FINISHED                              docker:default
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 429B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim        2.4s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 477B                                          0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9ef  19.3s
 => => resolve docker.io/library/python:3.11-slim@sha256:c24e9effa2821a68  0.0s
 => => sha256:3e731abb5c1dd05aef62585d392d31ad26089dc4c 14.36MB / 14.36MB  6.7s
 => => sha256:c24e9effa2821a6885165d930d939fec2af0dcf81 10.37kB / 10.37kB  0.0s
 => => sha256:89abad2fb0c3633705054018ae09caae4bd0e0febf5 1.75kB / 1.75kB  0.0s
 => => sha256:fa659464a114c340e31c7b7954a1aa679de7e7f5346 5.47kB / 5.47kB  0.0s
 => => sha256:119d43eec815e5f9a47da3a7d59454581b1e204b 29.77MB / 29.77MB  13.6s
 => => sha256:5b09819094bb89d5b2416ff2fb03f68666a5372c358 1.29MB / 1.29MB  2.0s
 => => sha256:0b2bf04f68e9f306a8a83f57c6ced322a23968bf3d5aceb 250B / 250B  2.7s
 => => extracting sha256:119d43eec815e5f9a47da3a7d59454581b1e204b0c34db86  2.9s
 => => extracting sha256:5b09819094bb89d5b2416ff2fb03f68666a5372c358cfd22  0.3s
 => => extracting sha256:3e731abb5c1dd05aef62585d392d31ad26089dc4c031730e  2.0s
 => => extracting sha256:0b2bf04f68e9f306a8a83f57c6ced322a23968bf3d5acebc  0.0s
 => [builder 2/4] WORKDIR /hello                                           0.5s
 => [builder 3/4] COPY requirements.txt .                                  0.1s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=  6.1s
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                      0.1s
 => [stage-1 4/6] COPY requirements.txt .                                  0.1s
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requ  2.6s
 => [stage-1 6/6] COPY hello.py .                                          0.2s
 => exporting to image                                                     0.3s
 => => exporting layers                                                    0.2s
 => => writing image sha256:5924a5d677362359e388c57598d5a9bfb16d574a8bb21  0.0s
 => => naming to docker.io/library/hello-appsec-world                      0.0s


$ docker run hello-appsec-world:latest
hello appsec world


$ docker run --rm -it hello-appsec-world
hello appsec world

$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

$ docker save -o hello.tar hello-appsec-world

$ docker load -i hello.tar
Loaded image: hello-appsec-world:latest

$ docker load -i image.tar
open image.tar: no such file or directory
```

- [x] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`

- [x] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 


- [x] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
$ sha256sum my-hello-appsec-world.tar hello.tar 
48dd67d8bdd92517262330137d087d05c23262936d8c10843940dc74af3145df  my-hello-appsec-world.tar
ecc541d200c18f2f85927f3b08c12705f6b773d6f68ed20823cff4b3891d8e59  hello.tar
```

- [x] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`. Размещение библиотек в следующем формате:

```
flask==2.2.3
requests==2.28.1
```

- [x] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

```bash
$ docker run my-hello-appsec-world-lib
h3ll0 mY app-$ec w0rld...
```

- [x] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ docker login

USING WEB-BASED LOGIN

i Info → To sign in with credentials on the command line, use 'docker login -u <username>'
         

Your one-time device confirmation code is: LHGX-RHSL
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…

WARNING! Your credentials are stored unencrypted in '/home/user/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded


$ docker tag my-hello-appsec-world-lib:latest shabalka/my-hello-appsec-world-lib

$ docker push shabalka/my-hello-appsec-world-lib
Using default tag: latest
The push refers to repository [docker.io/shabalka/my-hello-appsec-world-lib]
3de4a59cd5a9: Pushed 
131794093eed: Pushed 
1a785662836e: Pushed 
e75569934e93: Pushed 
f2611753a720: Pushed 
49d74831a287: Mounted from library/python 
5d89b1d5fc98: Mounted from library/python 
523062ea36b5: Mounted from library/python 
e50a58335e13: Mounted from library/python 
latest: digest: sha256:c798d18629119626e3272366935775100a347190c27700a4fb3c6e161867e66f size: 2198


$ docker inspect shabalka/my-hello-appsec-world-lib
[
    {
        "Id": "sha256:7ee9f2a180fbef7e460b189ea669c04572bbcaacf8dc580f7916d56098756b76",
        "RepoTags": [
            "my-hello-appsec-world-lib:latest",
            "shabalka/my-hello-appsec-world-lib:latest"
        ],
        "RepoDigests": [
            "shabalka/my-hello-appsec-world-lib@sha256:c798d18629119626e3272366935775100a347190c27700a4fb3c6e161867e66f"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-14T09:57:34.606938202+03:00",
        "DockerVersion": "",
        "Author": "",
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 135147358,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/v49a64ygwaoqgkkl70o4i3idl/diff:/var/lib/docker/overlay2/p44yql9qtxah3fyn8s4bafk5x/diff:/var/lib/docker/overlay2/kpmb44e9v1oh8shop55e5i3cy/diff:/var/lib/docker/overlay2/pk9aes08oetilxr11jj97i5pt/diff:/var/lib/docker/overlay2/ae90e128d376c6b0937e69c50e4eeaddb1ffbb238898f848275d7fc2deea6698/diff:/var/lib/docker/overlay2/76f8242262cbec4b34b7e01c6f5df5736859e0a7102ef9c9cfc64169d45f17c1/diff:/var/lib/docker/overlay2/d30d09bd806fc83ad4b83d0e353fc95de0667f31a325544fb9298c435e795201/diff:/var/lib/docker/overlay2/b5b9ebd3a4ba01d0636a89562969335fde21dd2db841d37271afdb1d2c55c5a8/diff",
                "MergedDir": "/var/lib/docker/overlay2/e22zlu2r6x8hwoh2q2tdaxre3/merged",
                "UpperDir": "/var/lib/docker/overlay2/e22zlu2r6x8hwoh2q2tdaxre3/diff",
                "WorkDir": "/var/lib/docker/overlay2/e22zlu2r6x8hwoh2q2tdaxre3/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e50a58335e1366e2581fe61794c1651afe2fe04e881e795aa166f24f4fc78d92",
                "sha256:523062ea36b5189e9ea6d7d86850296d1d7b5b4418109217e7ac12e13273fbba",
                "sha256:5d89b1d5fc98cb4fa0c3a8ac89cf83932b8b287e318b7761badd4b9ce58b3ecb",
                "sha256:49d74831a2871d1733e397932626f721303aef93edc180602b0877d68c6cbf5a",
                "sha256:f2611753a720500ae2651bec2ecd1f9390835ae615a1cf06bd9530efbec5db8f",
                "sha256:e75569934e9343feceadc119511a4cec77a60e78718f1ecc168c052ad415d8ea",
                "sha256:1a785662836e1d2301b5904344c6d2f0dd62ec3b5e9ba891a779df7cae396a84",
                "sha256:131794093eed69aaf81e7964c925b745c0980394a478fb638928ef9701aad739",
                "sha256:3de4a59cd5a9c31fefae91c3bbac2b84c1a73ae0d33ddeccfad8d1e8a384200b"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-14T10:06:03.016879801+03:00"
        },
        "Config": {
            "ArgsEscaped": true,
            "Cmd": [
                "python",
                "new_hello.py"
            ],
            "Entrypoint": null,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D", <!-- gitleaks:allow -->
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Labels": null,
            "OnBuild": null,
            "User": "",
            "Volumes": null,
            "WorkingDir": "/hello"
        }
    }
]

$ docker container create --name first my-hello-appsec-world-lib:latest 
a7bdae882fa4aa773e4a89727171606f6fcc1ab1885335d3abf2b9338d824d59
```

```bash
$ docker pull geminishkvdev/hello-appsec-world
Using default tag: latest
latest: Pulling from geminishkvdev/hello-appsec-world
no matching manifest for linux/amd64 in the manifest list entries

# Соберу изначальный hello-appsec-world как second
$ docker container create --name second hello-appsec-world:latest 
8b59226c82d1d956da7afc8890fafc33e461c861dc742ca269a65360bb865d9c
```

- [x] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Pull complete 
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest

root@434ea21e7a17:/# ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.0   4588  3840 pts/0    Ss   07:14   0:00 /bin/bash
root           8  0.0  0.0   7888  3968 pts/0    R+   07:15   0:00 ps aux
``` 

- USER: root (все процессы запущены от root, потому что в официальном образе ubuntu по умолчанию нет инструкции USER в Dockerfile → контейнер стартует от root).
- PID 1: это главный процесс контейнера (/bin/bash) — он всегда PID 1 внутри namespace контейнера.
- Процессов мало — это нормально для "голого" ubuntu без дополнительных сервисов.
- Нет других пользователей — только root
 

- [x] 10. Выведите оба контейнера first и second на терминал

```bash
$ docker ps -a -f name=first -f name=second

CONTAINER ID   IMAGE                              COMMAND                 CREATED          STATUS    PORTS     NAMES

8b59226c82d1   hello-appsec-world:latest          "python hello.py"       8 minutes ago    Created             second

a7bdae882fa4   my-hello-appsec-world-lib:latest   "python new_hello.py"   14 minutes ago   Created             first
```

- [x] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
$ docker-compose up --build
``` 

```
$ docker compose up --build
WARN[0000] /home/user/Documents/RISKI/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
#1 [internal] load local bake definitions
#1 reading from stdin 1.03kB done
#1 DONE 0.0s

#2 [server internal] load build definition from Dockerfile
#2 DONE 0.0s

#2 [server internal] load build definition from Dockerfile
#2 transferring dockerfile: 419B done
#2 DONE 0.1s

#3 [client internal] load build definition from Dockerfile
#3 transferring dockerfile: 425B done
#3 DONE 0.1s

#4 [client internal] load metadata for docker.io/library/python:3.11-slim
#4 ...

#5 [auth] library/python:pull token for registry-1.docker.io
#5 DONE 0.0s

#4 [client internal] load metadata for docker.io/library/python:3.11-slim
#4 DONE 1.3s

#6 [server internal] load .dockerignore
#6 transferring context: 2B done
#6 DONE 0.0s

#7 [client internal] load .dockerignore
#7 transferring context: 2B done
#7 DONE 0.1s

#8 [client builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:c24e9effa2821a6885165d930d939fec2af0dcf819276138f11dd45e200bd032
#8 CACHED

#9 [server internal] load build context
#9 transferring context: 842B 0.0s done
#9 DONE 0.1s

#10 [client internal] load build context
#10 transferring context: 576B 0.0s done
#10 DONE 0.1s

#11 [client builder 2/4] WORKDIR /app
#11 DONE 0.1s

#12 [client builder 3/4] COPY requirements.txt .
#12 DONE 0.1s

#13 [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#13 ...

#14 [server builder 3/4] COPY requirements.txt .
#14 DONE 0.1s

#15 [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#15 2.949 Requirement already satisfied: pip in /usr/local/lib/python3.11/site-packages (24.0)
#15 3.346 Collecting pip
#15 3.665   Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
#15 3.759 Downloading pip-25.3-py3-none-any.whl (1.8 MB)
#15 5.502    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 1.0 MB/s eta 0:00:00
#15 5.572 Installing collected packages: pip
#15 5.572   Attempting uninstall: pip
#15 5.572     Found existing installation: pip 24.0
#15 5.634     Uninstalling pip-24.0:
#15 6.030       Successfully uninstalled pip-24.0
#15 6.669 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#15 6.671 Successfully installed pip-25.3
#15 7.769 Collecting flask==2.3.3 (from -r requirements.txt (line 1))
#15 7.996   Downloading flask-2.3.3-py3-none-any.whl.metadata (3.6 kB)
#15 8.126 Collecting werkzeug==2.3.7 (from -r requirements.txt (line 2))
#15 8.183   Downloading werkzeug-2.3.7-py3-none-any.whl.metadata (4.1 kB)
#15 8.274 Collecting Jinja2>=3.1.2 (from flask==2.3.3->-r requirements.txt (line 1))
#15 8.356   Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
#15 8.433 Collecting itsdangerous>=2.1.2 (from flask==2.3.3->-r requirements.txt (line 1))
#15 8.486   Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
#15 8.595 Collecting click>=8.1.3 (from flask==2.3.3->-r requirements.txt (line 1))
#15 8.678   Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
#15 8.754 Collecting blinker>=1.6.2 (from flask==2.3.3->-r requirements.txt (line 1))
#15 8.806   Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
#15 ...

#13 [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#13 2.960 Requirement already satisfied: pip in /usr/local/lib/python3.11/site-packages (24.0)
#13 3.355 Collecting pip
#13 3.673   Downloading pip-25.3-py3-none-any.whl.metadata (4.7 kB)
#13 3.776 Downloading pip-25.3-py3-none-any.whl (1.8 MB)
#13 5.616    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 969.7 kB/s eta 0:00:00
#13 5.671 Installing collected packages: pip
#13 5.672   Attempting uninstall: pip
#13 5.676     Found existing installation: pip 24.0
#13 5.732     Uninstalling pip-24.0:
#13 6.040       Successfully uninstalled pip-24.0
#13 6.712 Successfully installed pip-25.3
#13 6.712 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#13 7.786 Collecting requests==2.28.1 (from -r requirements.txt (line 1))
#13 8.030   Downloading requests-2.28.1-py3-none-any.whl.metadata (4.6 kB)
#13 8.347 Collecting charset-normalizer<3,>=2 (from requests==2.28.1->-r requirements.txt (line 1))
#13 8.408   Downloading charset_normalizer-2.1.1-py3-none-any.whl.metadata (11 kB)
#13 8.520 Collecting idna<4,>=2.5 (from requests==2.28.1->-r requirements.txt (line 1))
#13 8.586   Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
#13 8.712 Collecting urllib3<1.27,>=1.21.1 (from requests==2.28.1->-r requirements.txt (line 1))
#13 8.778   Downloading urllib3-1.26.20-py2.py3-none-any.whl.metadata (50 kB)
#13 8.949 Collecting certifi>=2017.4.17 (from requests==2.28.1->-r requirements.txt (line 1))
#13 9.034   Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
#13 ...

#15 [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#15 9.006 Collecting MarkupSafe>=2.1.1 (from werkzeug==2.3.7->-r requirements.txt (line 2))
#15 9.048   Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
#15 9.140 Downloading flask-2.3.3-py3-none-any.whl (96 kB)
#15 9.303 Downloading werkzeug-2.3.7-py3-none-any.whl (242 kB)
#15 9.548 Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
#15 9.612 Downloading click-8.3.1-py3-none-any.whl (108 kB)
#15 9.844 Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
#15 9.997 Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
#15 10.30 Downloading markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
#15 ...

#13 [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#13 9.101 Downloading requests-2.28.1-py3-none-any.whl (62 kB)
#13 9.210 Downloading charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
#13 9.314 Downloading idna-3.11-py3-none-any.whl (71 kB)
#13 9.486 Downloading urllib3-1.26.20-py2.py3-none-any.whl (144 kB)
#13 9.621 Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
#13 9.763 Saved /wheels/requests-2.28.1-py3-none-any.whl
#13 9.764 Saved /wheels/charset_normalizer-2.1.1-py3-none-any.whl
#13 9.765 Saved /wheels/idna-3.11-py3-none-any.whl
#13 9.765 Saved /wheels/urllib3-1.26.20-py2.py3-none-any.whl
#13 9.767 Saved /wheels/certifi-2026.1.4-py3-none-any.whl
#13 DONE 10.4s

#15 [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt
#15 10.40 Saved /wheels/flask-2.3.3-py3-none-any.whl
#15 10.40 Saved /wheels/werkzeug-2.3.7-py3-none-any.whl
#15 10.40 Saved /wheels/blinker-1.9.0-py3-none-any.whl
#15 10.40 Saved /wheels/click-8.3.1-py3-none-any.whl
#15 10.40 Saved /wheels/itsdangerous-2.2.0-py3-none-any.whl
#15 10.40 Saved /wheels/jinja2-3.1.6-py3-none-any.whl
#15 10.40 Saved /wheels/markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl
#15 DONE 10.5s

#16 [client stage-1 3/6] COPY --from=builder /wheels /wheels
#16 ...

#17 [server stage-1 3/6] COPY --from=builder /wheels /wheels
#17 DONE 0.1s

#16 [client stage-1 3/6] COPY --from=builder /wheels /wheels
#16 DONE 0.2s

#18 [server stage-1 4/6] COPY requirements.txt .
#18 DONE 0.1s

#19 [client stage-1 4/6] COPY requirements.txt .
#19 DONE 0.2s

#20 [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt
#20 2.354 Looking in links: /wheels
#20 2.369 Processing /wheels/requests-2.28.1-py3-none-any.whl (from -r requirements.txt (line 1))
#20 2.384 Processing /wheels/charset_normalizer-2.1.1-py3-none-any.whl (from requests==2.28.1->-r requirements.txt (line 1))
#20 2.395 Processing /wheels/idna-3.11-py3-none-any.whl (from requests==2.28.1->-r requirements.txt (line 1))
#20 2.404 Processing /wheels/urllib3-1.26.20-py2.py3-none-any.whl (from requests==2.28.1->-r requirements.txt (line 1))
#20 2.413 Processing /wheels/certifi-2026.1.4-py3-none-any.whl (from requests==2.28.1->-r requirements.txt (line 1))
#20 2.490 Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
#20 2.769 Successfully installed certifi-2026.1.4 charset-normalizer-2.1.1 idna-3.11 requests-2.28.1 urllib3-1.26.20
#20 2.771 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#20 DONE 3.4s

#21 [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt
#21 2.335 Looking in links: /wheels
#21 2.349 Processing /wheels/flask-2.3.3-py3-none-any.whl (from -r requirements.txt (line 1))
#21 2.361 Processing /wheels/werkzeug-2.3.7-py3-none-any.whl (from -r requirements.txt (line 2))
#21 2.377 Processing /wheels/jinja2-3.1.6-py3-none-any.whl (from flask==2.3.3->-r requirements.txt (line 1))
#21 2.383 Processing /wheels/itsdangerous-2.2.0-py3-none-any.whl (from flask==2.3.3->-r requirements.txt (line 1))
#21 2.393 Processing /wheels/click-8.3.1-py3-none-any.whl (from flask==2.3.3->-r requirements.txt (line 1))
#21 2.396 Processing /wheels/blinker-1.9.0-py3-none-any.whl (from flask==2.3.3->-r requirements.txt (line 1))
#21 2.406 Processing /wheels/markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (from werkzeug==2.3.7->-r requirements.txt (line 2))
#21 2.464 Installing collected packages: MarkupSafe, itsdangerous, click, blinker, werkzeug, Jinja2, flask
#21 3.083 Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.3 blinker-1.9.0 click-8.3.1 flask-2.3.3 itsdangerous-2.2.0 werkzeug-2.3.7
#21 3.083 WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
#21 DONE 3.5s

#22 [server stage-1 6/6] COPY app.py .
#22 DONE 0.2s

#23 [client stage-1 6/6] COPY client.py .
#23 DONE 0.2s

#24 [client] exporting to image
#24 exporting layers
#24 exporting layers 0.3s done
#24 writing image sha256:ac1aabaf333391ad904a5e17f51f33820af16fdc498cce0b040fc949e006d189
#24 writing image sha256:ac1aabaf333391ad904a5e17f51f33820af16fdc498cce0b040fc949e006d189 0.0s done
#24 naming to docker.io/library/lab05-client 0.0s done
#24 DONE 0.4s

#25 [server] exporting to image
#25 exporting layers 0.4s done
#25 writing image sha256:8be51997ee301266216b87c9cf110b1d75a42a63cc3c1f485a4a45c273a5d6e8 done
#25 naming to docker.io/library/lab05-server done
#25 DONE 0.4s

#26 [client] resolving provenance for metadata file
#26 DONE 0.0s

#27 [server] resolving provenance for metadata file
#27 DONE 0.0s
[+] Running 5/5
 ✔ lab05-server              Built                                                                                               0.0s 
 ✔ lab05-client              Built                                                                                               0.0s 
 ✔ Network lab05_app_net     Created                                                                                             0.1s 
 ✔ Container lab05-server-1  Created                                                                                             0.1s 
 ✔ Container lab05-client-1  Created                                                                                             0.1s 
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.18.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.18.0.3 - - [14/Jan/2026 07:23:19] "GET / HTTP/1.1" 200 -
client-1  | 
client-1  |     <html>
client-1  |     <head><title>Colorful Output</title></head>
client-1  |     <body style="font-family: monospace; font-size: 24px;">
```

- Compose загружает локальные определения сборки (bake definitions).
- Начинается параллельная сборка двух сервисов: server и client.
- Для обоих сервисов загружается Dockerfile.
- Загружаются метаданные базового образа python:3.11-slim.
- Авторизуется в Docker Hub для скачивания образа.
- Загружаются .dockerignore файлы для обоих сервисов.
- Проверяется кэш: базовый слой FROM python:3.11-slim берётся из кэша.
- Загружается контекст сборки (файлы проекта) для server и client.
- В builder-стадии для client: создаётся WORKDIR /app, копируется requirements.txt.
- В builder-стадии для обоих сервисов: обновляется pip с 24.0 до 25.3.
- Pip предупреждает, что запуск от root может сломать права — рекомендует виртуальное окружение.
- Для server: собираются wheels из requirements.txt (flask==2.3.3 и его зависимости: werkzeug, jinja2, itsdangerous, click, blinker, markupsafe).
- Для client: собираются wheels из requirements.txt (requests==2.28.1 и его зависимости: urllib3, idna, charset-normalizer, certifi).
- Все скачанные wheels сохраняются в папку /wheels.
- В финальной стадии для client: копируются wheels из builder, копируется requirements.txt, устанавливаются пакеты только из локальных wheels.
- В финальной стадии для server: копируются wheels из builder, копируется requirements.txt, устанавливаются пакеты только из локальных wheels.
- Для server: копируется app.py.
- Для client: копируется client.py.
- Создаются итоговые образы: lab05-client и lab05-server.
- Записываются sha256-хэши новых образов.
- Разрешаются метаданные provenance (для безопасности и воспроизводимости).
- Создаётся сеть lab05_app_net.
- Создаются контейнеры lab05-server-1 и lab05-client-1.
- Запускаются контейнеры.

- [x] 12. Откройте соседнее окно терминала и и выведите на терминале http://localhost:8000

```
server-1  | 172.18.0.1 - - [14/Jan/2026 07:27:37] "GET / HTTP/1.1" 200 -
server-1  | 172.18.0.1 - - [14/Jan/2026 07:27:37] "GET /favicon.ico HTTP/1.1" 404 -
```

- [ ] 13. Остановите работу `docker-compose`.

```bash 
$ docker images
REPOSITORY                           TAG       IMAGE ID       CREATED          SIZE
shabalka/my-hello-appsec-world-lib   latest    7ee9f2a180fb   14 minutes ago   135MB
my-hello-appsec-world-lib            latest    7ee9f2a180fb   14 minutes ago   135MB
<none>                               <none>    ab813665e8c5   18 minutes ago   135MB
my-hello-appsec-world                latest    c0201d806359   28 minutes ago   135MB
hello-appsec-world                   latest    5924a5d67736   53 minutes ago   135MB
$ docker ps -a
CONTAINER ID   IMAGE                              COMMAND                 CREATED             STATUS                         PORTS                                         NAMES
09b4ede37d3e   lab05-client                       "python client.py"      7 minutes ago       Up 11 seconds                                                                lab05-client-1
7cdb32e42f41   lab05-server                       "python app.py"         7 minutes ago       Up 11 seconds                  0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   lab05-server-1
434ea21e7a17   ubuntu                             "/bin/bash"             16 minutes ago      Exited (0) 11 minutes ago                                                    objective_neumann
8b59226c82d1   hello-appsec-world:latest          "python hello.py"       18 minutes ago      Created                                                                      second
a7bdae882fa4   my-hello-appsec-world-lib:latest   "python new_hello.py"   23 minutes ago      Created                                                                      first
86cc7619ab86   my-hello-appsec-world-lib          "python new_hello.py"   33 minutes ago      Exited (0) 32 minutes ago                                                    hungry_goldwasser
94ce40b614ad   ab813665e8c5                       "python new_hello.py"   36 minutes ago      Exited (0) 36 minutes ago                                                    boring_moore
e81573e2dc7e   my-hello-appsec-world              "python new_hello.py"   46 minutes ago      Exited (0) 46 minutes ago                                                    musing_engelbart
384d80b4bbc7   hello-appsec-world:latest          "python hello.py"       About an hour ago   Exited (0) About an hour ago                                                 elegant_goldberg
518aa9c9c677   hello-appsec-world:latest          "python hello.py"       About an hour ago   Exited (0) About an hour ago                                                 lucid_wescoff
ced8c4312589   hello-appsec-world:latest          "python hello.py"       About an hour ago   Exited (0) About an hour ago                                                 laughing_goldberg

$ docker ps -q
09b4ede37d3e
7cdb32e42f41

$ docker images
REPOSITORY                           TAG       IMAGE ID       CREATED             SIZE
lab05-client                         latest    ac1aabaf3333   7 minutes ago       138MB
lab05-server                         latest    8be51997ee30   7 minutes ago       141MB
my-hello-appsec-world-lib            latest    7ee9f2a180fb   33 minutes ago      135MB
shabalka/my-hello-appsec-world-lib   latest    7ee9f2a180fb   33 minutes ago      135MB
<none>                               <none>    ab813665e8c5   36 minutes ago      135MB
my-hello-appsec-world                latest    c0201d806359   46 minutes ago      135MB
hello-appsec-world                   latest    5924a5d67736   About an hour ago   135MB
ubuntu                               latest    c3a134f2ace4   2 months ago        78.1MB

$ docker ps -q | xargs docker stop
09b4ede37d3e
7cdb32e42f41

$ docker compose down
WARN[0000] /home/user/Documents/RISKI/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 3/3
 ✔ Container lab05-client-1  Removed                                                                                             0.0s 
 ✔ Container lab05-server-1  Removed                                                                                             0.0s 
 ✔ Network lab05_app_net     Removed 
```

- [x] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

```
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.18.0.2:8000
server-1  | Press CTRL+C to quit
server-1  |  * Running on http://172.18.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 127.0.0.1 - - [14/Jan/2026 07:47:33] "GET / HTTP/1.1" 200 -
server-1  | 127.0.0.1 - - [14/Jan/2026 07:47:33] "GET / HTTP/1.1" 200 -
server-1  | 172.18.0.3 - - [14/Jan/2026 07:47:34] "GET / HTTP/1.1" 200 -
server-1  | 172.18.0.3 - - [14/Jan/2026 07:47:34] "GET / HTTP/1.1" 200 -
client-1  | 
client-1  |     <html>
server-1  | 127.0.0.1 - - [14/Jan/2026 07:47:43] "GET / HTTP/1.1" 200 -
server-1  | 127.0.0.1 - - [14/Jan/2026 07:47:43] "GET / HTTP/1.1" 200 -
client-1  |     <head><title>Colorful Output</title></head>
```

`docker-compose.yml`
```
networks:
  app_net:

services:
  server:
    build: ./server
    ports:
      - "8000:8000"
    networks:
      - app_net
    command: python app.py
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8000/"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  client:
    build: ./client
    networks:
      - app_net
    command: python client.py
    depends_on:
      server:
        condition: service_healthy
```

- [x] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.
 
***

## Links

- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)
- [GitHub Docs](https://docs.github.com/en)
- [Docker](https://docs.docker.com/)
- [Docker Engine overview](https://docs.docker.com/engine/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Docker Compose documentation](https://docs.docker.com/compose/)
- [Docker Hub](https://hub.docker.com/)
- [Docker security overview](https://docs.docker.com/engine/security/)

Copyright (c) 2025 Elijah S Shmakov

![Logo](../../assets/logotype/logo.jpg)