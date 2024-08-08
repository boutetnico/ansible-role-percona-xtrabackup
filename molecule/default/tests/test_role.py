import pytest


@pytest.mark.parametrize(
    "name",
    [
        ("percona-xtrabackup-83"),
    ],
)
def test_packages_are_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/usr/bin/xtrabackup", "root", "root", 0o755),
    ],
)
def test_wp_cli_is_installed(host, path, username, groupname, mode):
    path = host.file(path)
    assert path.exists
    assert path.is_file
    assert path.user == username
    assert path.group == groupname
    assert path.mode == mode
