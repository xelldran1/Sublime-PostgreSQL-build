from sublime import active_window, error_message, message_dialog, packages_path, status_message
from sublime_plugin import WindowCommand
from os.path import basename, dirname, exists, join
from glob import glob
from shutil import copy


def package_path():
    """return this package path"""
    filename=glob(join(packages_path(),"*",basename(__file__)))[0]
    return dirname(filename)

def pgpass_tip():
    url="www.postgresql.org/docs/9.2/static/libpq-pgpass.html"
    status_message(url)
    message_dialog("psql get password from pgpass")
    status_message(url)

default_build=glob(join(package_path(),"*.sublime-build"))[0]
user_build=join(packages_path(),"User",basename(default_build))
if not exists(user_build):
    copy(default_build,user_build)
    active_window().open_file(user_build)
    message_dialog("edit PostgreSQL connection settings")
    pgpass_tip()

class PostgresqlDefaultSettingsCommand(WindowCommand):
    def run(self):
        global default_build
        try:
            self.window.open_file(default_build)
            pgpass_tip()
        except Exception, e:
            error_message(str(e))

class PostgresqlUserSettingsCommand(WindowCommand):
    def run(self):
        global user_build
        try:
            self.window.open_file(user_build)
            pgpass_tip()
        except Exception, e:
            error_message(str(e))