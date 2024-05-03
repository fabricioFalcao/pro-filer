import pytest
import os
from datetime import date

from pro_filer.actions.main_actions import show_details  # NOQA


@pytest.fixture(autouse=True)
def mock_file_path(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir(parents=True)
    file_path = dir_path / "test.txt"
    file_path.write_text("Chiquinha era mais legal que Pitty.")
    return dir_path


def test_with_directory_path(capsys, mock_file_path):
    path = str(mock_file_path)
    context = {"base_path": path}

    show_details(context)

    captured = capsys.readouterr()
    assert (
        captured.out
        == f"File name: test_dir\nFile size in bytes: {os.path.getsize(path)}\nFile type: directory\nFile extension: [no extension]\nLast modified date: {date.fromtimestamp(os.path.getmtime(path))}\n"
    )


def test_with_file_path(capsys, mock_file_path):
    path = f"{mock_file_path}/test.txt"
    context = {"base_path": path}

    show_details(context)

    captured = capsys.readouterr()
    assert (
        captured.out
        == f"File name: test.txt\nFile size in bytes: {os.path.getsize(path)}\nFile type: file\nFile extension: .txt\nLast modified date: {date.fromtimestamp(os.path.getmtime(path))}\n"
    )


def test_with_invalid_path(capsys, mock_file_path):
    path = f"{mock_file_path}/test"
    context = {"base_path": path}

    show_details(context)

    captured = capsys.readouterr()
    assert captured.out == f"File 'test' does not exist\n"
