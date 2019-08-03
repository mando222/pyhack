#!/usr/bin/env python3

import hashlib
import zlib
from pathlib import Path

class hash_file:
    def __init__(self):
        file_name = input("enter the path of the file to be hashed: ")
        my_file = Path(file_name)
        trying=True
        while trying:
            try:
                my_abs_path = my_file.resolve(strict=True)
            except FileNotFoundError:
                print("File", my_file, "not found")
                file_name = input("please enter another file to be hashed or exit to cancel operation: ")
                if file_name == 'cancel':
                    trying=False
            else:
                print("found file: ",my_abs_path)
                trying=False
                hash_type = str(input("What kind of hashing to be used (default md5)\n [md5, sha1, sha224, sha256, sha384, sha512, adler32, crc32]: ") or 'md5')
                if hash_type == 'md5':
                    hasher = hashlib.md5()
                    default_block_size = '512'
                elif hash_type == 'sha1':
                    hasher = hashlib.sha1()
                    default_block_size = '512'
                elif hash_type == 'sha224':
                    hasher = hashlib.sha224()
                    default_block_size = '512'
                elif hash_type == 'sha256':
                    hasher = hashlib.sha256()
                    default_block_size = '512'
                elif hash_type == 'sha384':
                    hasher = hashlib.sha384()
                    default_block_size = '1024'
                elif hash_type == 'sha512':
                    hasher = hashlib.sha512()
                    default_block_size = '1024'
                elif hash_type == 'adler32':
                    hasher = hashlib.md5()
                    default_block_size = '512'
                    print("not implemented useing md5")
                    # hasher = zlib.adler32()
                    # default_block_size = '512'
                elif hash_type == 'crc32':
                    hasher = hashlib.md5()
                    default_block_size = '512'
                    print("not implemented useing md5")
                    # hasher = zlib.crc32()
                    # default_block_size = '512'

                blocksize = int(input("Enter the blocksize : ") or default_block_size)
                with open(my_abs_path, 'rb') as afile:
                    buf = afile.read(blocksize)
                    while len(buf) > 0:
                        hasher.update(buf)
                        buf = afile.read(blocksize)
                print(hasher.hexdigest())