"""This module contains core scripts for splitting files"""

# Standard Library
from os import path, mkdir
from typing import Union

# Local
from .utils import path_exists, path_is_file


def split_into_parts(
    file_path: Union[str, list, tuple], output_path: str, parts: int, ratio: Union[list, tuple] = None, prefix: str = "chunk_"
):
    """Splits provided file into chunks based on parts from total size of file

    Args:
        file_path (str, tuple, list): Path to the file(s) to be splitted
        output_path (str): Output folder path
        parts (int): Parts value for splitting
        ratio (list or tuple, optional): Optional value given to split files with bytes divided as per input list
        prefix (str, optional): Optional prefix to chunks. Defaults to "chunk_".

    Raises:
        IOError: Raised if file at path does not exist
        IOError: Raised if resource at path is not a folder
    """

    if not path_is_file(file_path):
        raise IOError(f"File at path {file_path} does not exist!")

    if not path_exists(output_path):
        mkdir(output_path)

    with open(file_path, "rb") as mfile:
        content = bytearray(path.getsize(file_path))
        chunk_size = len(content) // parts
        mfile.readinto(content)

        for count, i in enumerate(range(0, len(content), chunk_size)):
            with open(
                output_path + "/" + prefix + str(count) + path.basename(file_path), "wb"
            ) as chunk_file:
                chunk_file.write(content[i : i + chunk_size])
