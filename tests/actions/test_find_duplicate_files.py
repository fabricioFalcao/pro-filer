import pytest

from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


@pytest.fixture()
def mock_file_path(tmp_path):
    dir_path = tmp_path / "duplicate"
    dir_path.mkdir(parents=True)

    file1_path = dir_path / "test1.txt"
    file1_path.write_text("Chiquinha era mais legal que Pitty.")

    file2_path = dir_path / "test2.txt"
    file2_path.write_text("Chiquinha era mais legal que Pitty.")

    file3_path = dir_path / "test3.txt"
    file3_path.write_text(
        "Todos os meus doguinhos marcaram minha vida. Para citar alguns: Moreninha (1 e 2), Polly Pretinha, Max, Priscila (1 e 2), Tunico (1, 2 e 3), Kika, Pink, Jimmy, Raner. Mensão honrosa: Petros"
    )

    return [file1_path, file2_path, file3_path]


def test_find_duplicate_files_valid(mock_file_path):
    context = {"all_files": mock_file_path}

    assert find_duplicate_files(context) == [
        (mock_file_path[0], mock_file_path[1])
    ]


def test_find_duplicate_files_invalid(mock_file_path):
    context = {
        "all_files": [*mock_file_path, "invalid/path/to/inexistent/file.txt"]
    }

    with pytest.raises(ValueError, match="All files must exist"):
        find_duplicate_files(context)
