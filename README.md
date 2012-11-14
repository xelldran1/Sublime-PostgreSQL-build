Config
----------
After install, bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows), select **PostgreSQL build** and edit connection settings

set password in [pgpass](http://www.postgresql.org/docs/9.2/static/libpq-pgpass.html) file

Installing
----------
**With the [Package Control plugin](http://wbond.net/sublime_packages/package_control):** 
Add [my package channel](
https://github.com/cancerhermit/Sublime-package-channel)
url - 

	https://raw.github.com/cancerhermit/Sublime-package-channel/master/repositories.json

Bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select **PostgreSQL build** when the list appears. The advantage of using this method is that Package Control will automatically keep plugins up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/cancerhermit/Sublime-PostgreSQL-build) and copy the Sublime-PostgreSQL-build folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/cancerhermit/Sublime-PostgreSQL-build.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/