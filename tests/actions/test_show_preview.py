import pytest

from pro_filer.actions.main_actions import show_preview  # NOQA


@pytest.mark.parametrize(
    "context, expected",
    [
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                    "src/utils/utils.py",
                    "src/utils/utils2.py",
                    "src/utils/utils3.py",
                    "src/tests/__init__.py",
                    "src/tests/test_utils.py",
                    "src/tests/test_utils2.py",
                    "src/tests/test_utils3.py",
                ],
                "all_dirs": [
                    "src",
                    "src/utils",
                    "src/tests",
                    "src/functions",
                    "src/functions/alpha",
                    "src/functions/beta",
                    "src/functions/gamma",
                ],
            },
            "Found 10 files and 7 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py', 'src/utils/utils.py', 'src/utils/utils2.py']\nFirst 5 directories: ['src', 'src/utils', 'src/tests', 'src/functions', 'src/functions/alpha']\n",
        ),
        (
            {
                "all_files": [
                    "src/__init__.py",
                    "src/app.py",
                    "src/utils/__init__.py",
                ],
                "all_dirs": ["src", "src/utils"],
            },
            "Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories: ['src', 'src/utils']\n",
        ),
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n",
        ),
    ],
)
def test_show_preview(capsys, context, expected):
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected
