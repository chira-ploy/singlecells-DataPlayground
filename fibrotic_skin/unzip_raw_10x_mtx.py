#!usr/bin/env python

#Author = Chiranan Khantham

import os
import tarfile 
        
def unzip(filename):
    """ Unpacks a tar archive, handling both compressed (.tar.gz) and 
    uncompressed (.tar) formats. """
    
    mode = 'r'
    if filename.endswith('.tar.gz'):
        mode += ':gz'  # Add 'gz' for compressed archives
    
    with tarfile.open(filename, mode) as tar:
        try:
            tar.extractall()
            
            if filename.endswith('.tar.gz'):
                os.remove(filename)  # Remove the archive after extraction
                
        except tarfile.ReadError as e:
            print(f"Error extracting {file_path}: {e}")        
        
def prep_10xmtx_directory(file_path):
    """
    Prepares a 10x genomics data directory by unpacking all .tar and .tar.gz files.
    """
    for filename in os.listdir(file_path):
        if filename.endswith('.tar'):
            unzip(filename)
            
    for filename in os.listdir(file_path):
        if filename.endswith('.tar.gz'):
            unzip(filename)
            
   