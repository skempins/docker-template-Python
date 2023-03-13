# Template for Dockerized Python

Use as a starting point for developing a Python 3 application.

This has been customized to work with *Microsoft Visual Studio Code (VSCode)* using the *Remote - Containers* extension.

To develop with this template, install the following:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Micosoft Visual Studio Code](https://code.visualstudio.com/)
- [VSCode Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Key elements of this template

### Password Handling

This uses a local host file method of password handling which mimics Docker Secrets.

The `util/systempassword.py` contains the Python class for looking up credentials.  In the `passwordlookup.py` example code, these lines utilize this class to lookup the user password:

```python
import util.systempassword

mypasswords = util.systempassword.SystemPassword(passwordfile="/run/secrets/systempasswords")
password = mypasswords.lookupPassword(systemname=systemname, username=username)  # type: ignore
```

### VSCode settings

The `devcontainer.json` file is used only by VSCode during development and specifies `mounts`, `runArgs`, and `containerEnv` settings.  More information about modifying this file can be found in Docker build documentation: <https://docs.docker.com/engine/reference/builder/>.

#### mounts

The `mounts` setting line is used in conjunction with the password handling method to map the location of the `systempasswords` file to the container.

```config
, "mounts": ["source=C:\\TEMP\\docker-secrets,target=/run/secrets,type=bind,consistency=cached"]
```

Be sure to update the value `C:\\TEMP\\docker-secrets` to the location on your PC where your `systempasswords` file is located.  The code (when running in the container) expects to find this file in the directory `/run/secrets`.  

#### runArgs

The `runArgs` setting line specifies two Docker container runtime settings:

```config
, "runArgs": ["--dns-search=mydomain.com", "--hostname=pythonapp"]
```

To properly resolve host IP addresses, the DNS search domain is specified with the `--dns-search=sjrwmd.com` setting.  This setting causes the container to automatically update the `/etc/resolv.conf` file with `search sjrwmd.com` and allows non-fully qualified host names to be resolved when performing DNS lookups.

The `--hostname=pythonapp` setting sets the hostname of the container, which can be benefical because this value is sent to backend servers.  Including this setting is optional, and does not affect the container operation.

#### containerEnv

The `containerEnv` is used to dynamically specify the system and username values for the password lookup.  This keeps the container portable and aleviates hard-coding of these values.

```config
, "containerEnv": {"SYSTEM": "systemname", "USER": "username"}
```

## Customization

### app

The `app` directory is where all application code should reside.  The container is configured to execute `app/app.py`.  Do not change this name without changing the container configuration in `.devcontainer/Docker` and `.devcontainer/devcontainer.json`.

### requirements.txt

Customize this file with Python application requirements. The container build will reference this file by executing `pip3 install -r requirements.txt` to install supporting libraries.

### .devcontainer/Dockerfile

This file is the specification used to build the container.  More information about modifying this file can be found in Docker build documentation: https://docs.docker.com/engine/reference/builder/

### .devcontainer/devcontainer.json

This file is used specifically by VSCode and the Remote-Containers extension to build the container within VSCode.
