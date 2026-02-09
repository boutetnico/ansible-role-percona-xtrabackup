import pytest


def test_percona_xtrabackup_package_installed(host):
    package = host.package("percona-xtrabackup-84")
    assert package.is_installed


@pytest.mark.parametrize(
    "path,username,groupname,mode",
    [
        ("/usr/bin/xtrabackup", "root", "root", 0o755),
        ("/usr/bin/xbstream", "root", "root", 0o755),
        ("/usr/bin/xbcloud", "root", "root", 0o755),
    ],
)
def test_xtrabackup_binaries_installed(host, path, username, groupname, mode):
    f = host.file(path)
    assert f.exists
    assert f.is_file
    assert f.user == username
    assert f.group == groupname
    assert f.mode == mode


def test_xtrabackup_version(host):
    """Test that xtrabackup can be executed and returns version."""
    cmd = host.run("xtrabackup --version")
    assert cmd.rc == 0
    assert "xtrabackup" in cmd.stderr.lower() or "xtrabackup" in cmd.stdout.lower()


def test_xbstream_version(host):
    """Test that xbstream can be executed."""
    cmd = host.run("xbstream --help")
    assert cmd.rc == 0


def test_xbcloud_help(host):
    """Test that xbcloud can be executed."""
    cmd = host.run("xbcloud --help")
    assert cmd.rc == 0
    assert "xbcloud" in cmd.stdout or "xbcloud" in cmd.stderr
