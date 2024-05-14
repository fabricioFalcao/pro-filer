import pytest
import os
from unittest.mock import patch

from pro_filer.actions.main_actions import show_disk_usage  # NOQA


@pytest.fixture()
def mock_file_path(tmp_path):
    dir_path = tmp_path / "test_dir"
    dir_path.mkdir(parents=True)

    file1_path = dir_path / "test1.txt"
    file1_path.touch()

    file2_path = dir_path / "test2.txt"
    file2_path.write_text("Chiquinha era mais legal que Pitty.")

    file3_path = dir_path / "test3.txt"
    file3_path.write_text(
        "Todos os meus doguinhos marcaram minha vida. Para citar alguns: Moreninha (1 e 2), Polly Pretinha, Max, Priscila (1 e 2), Tunico (1, 2 e 3), Kika, Pink, Jimmy, Raner. Mensão honrosa: Petros"
    )

    return dir_path


def test_show_disk_usage_valid(monkeypatch, capsys, mock_file_path):
    files = [f"{mock_file_path}/test{i}.txt" for i in range(3, 0, -1)]
    sizes = [os.path.getsize(file) for file in files]
    total_size = sum(sizes)

    expeted_output = ""

    for file, size in zip(files, sizes):
        percentage = int(size / total_size * 100)
        expeted_output += f"'{file}': {size} ({percentage}%)\n"

    expeted_output += f"Total size: {total_size}\n"

    context = {"all_files": files}

    # def mock_get_printable_file_path(file_path):
    #     return file_path

    # monkeypatch.setattr(
    #     "pro_filer.actions.main_actions._get_printable_file_path",
    #     mock_get_printable_file_path,
    # )

    # show_disk_usage(context)

    with patch(
        "pro_filer.actions.main_actions._get_printable_file_path", lambda x: x
    ):
        show_disk_usage(context)

    captured = capsys.readouterr()
    assert captured.out == expeted_output
