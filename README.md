# PassMaester (previously auth_manager)
PassMaester is a password manager that generates cryptographically secure passwords using a special in-house algorithm, and securely stores and manages them for you.

**Changelog:**
* Changed Application name to PassMaester, repo name remains same to avoid linking issues.
* Fixed user password entry security vulnerability.
* Fixed (rare) crashes that used to occur on PassMaester's first run.
* Fixed PassMaester not starting issue due to incorrect username.
* Enabled auto-update and auto installation of pyAesCrypt.
* Fixed an instance where PassMaester won't start if multiple Python installations are present on a machine.

**Dependencies:**
* pyAesCrypt from PyPI

**Python 3.7+ is required for this application. If you don't have it installed, get it here: https://www.python.org/downloads/.**

Running the launcher will automatically install (or update, if an outdated version is already installed) the dependency required. If you want to learn more about pyAesCrypt or want to verify if you are running the latest version of pyAesCrypt, you can visit this link: https://pypi.org/project/pyAesCrypt/.

**Note:** The repo name is still kept as auth_manager so that people with outdated links to the current repo can still access it. Once a cool-off period passes, this repo will be renamed as PassMaester.
