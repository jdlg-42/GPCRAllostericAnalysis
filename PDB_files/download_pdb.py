#!/usr/bin/env python
# Script to download PDB files using BioPython

import os
import sys
from Bio.PDB import PDBList
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def download_pdb_file(pdb_id, download_dir=None, rename_to_pdb=True):
    """
    Download a PDB file from the RCSB PDB database. Also adds a file called "PDB files list.txt" 
    containing the PDB ID. 
    
    Args:
        pdb_id (str): The 4-character PDB ID
        download_dir (str, optional): Directory to save the PDB file. Defaults to current directory.
        rename_to_pdb (bool, optional): Whether to rename the file from .ent to .pdb. Defaults to True.
    
    Returns:
        str: Path to the downloaded file or None if download failed.
    """
    pdb_id = pdb_id.lower()  # Ensure PDB ID is in lowercase

    try:
        # If no download directory specified, use the current directory
        if download_dir is None:
            download_dir = os.getcwd()

        # Create PDBList object
        pdbl = PDBList()
        
        # Creates the PDB files list if it doesn't exist
        if not os.path.exists(os.path.join(download_dir, "PDB_files_list.txt")):
            with open(os.path.join(download_dir, "PDB_files_list.txt"), "w") as f:
                f.write("PDB files list:\n")
        
        logging.info(f"Downloading PDB file for ID: {pdb_id}")
        logging.info(f"File will be saved to: {download_dir}")
        
        # Download the PDB file
        # The retrieve_pdb_file function downloads the file and returns the file path
        file_path = pdbl.retrieve_pdb_file(
            pdb_code=pdb_id,
            file_format="pdb",  # Format is either 'pdb' or 'mmCif'
            pdir=download_dir,  # Where to store the file
            overwrite=True      # Overwrite existing files
        )
        
        if file_path:
            logging.info(f"Successfully downloaded PDB file: {file_path}")
            
            # Rename the file from .ent to .pdb if requested
            if rename_to_pdb and file_path.endswith('.ent'):
                new_file_path = file_path.replace('.ent', '.pdb')
                try:
                    os.rename(file_path, new_file_path)
                    logging.info(f"Renamed file from {file_path} to {new_file_path}")
                    # Add the PDB ID to the list of downloaded files
                    with open(os.path.join(download_dir, "PDB_files_list.txt"), "a") as f:
                        f.write(f"{pdb_id}\n")
                        logging.info(f"Added {pdb_id} to PDB files list.")
                    return new_file_path
                except Exception as e:
                    logging.error(f"Failed to rename file from .ent to .pdb: {str(e)}")
                    return file_path  # Return original path if rename fails              
        else:
            logging.error(f"Failed to download PDB file for ID: {pdb_id}")
            return None
  

    except Exception as e:
        logging.error(f"An error occurred while downloading PDB file: {str(e)}")
        return None

if __name__ == "__main__":
    # The PDB ID to download
    pdb_id = "5g53" 
    
    # Get the script's directory as download location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Download the PDB file and rename it to .pdb format
    file_path = download_pdb_file(pdb_id, script_dir, rename_to_pdb=True)

    # add the PDB ID to the list of downloaded files
    if file_path and isinstance(file_path, tuple):
        file_path, list_file_path = file_path
        print(f"PDB file was downloaded successfully to: {file_path}")
        print(f"PDB files list updated at: {list_file_path}")
    elif isinstance(file_path, str):
        print(f"PDB file was downloaded successfully to: {file_path}")
    
    if file_path:
        print(f"PDB file was downloaded successfully to: {file_path}")
    else:
        print("Failed to download the PDB file.")
        sys.exit(1)

    # Example of how to use the script with a different PDB ID
    # To use a different PDB ID, you can modify the pdb_id variable above
    # or uncomment and run the following lines:
    # 
    # another_pdb_id = "4hhb"  # Hemoglobin
    # download_pdb_file(another_pdb_id, script_dir, rename_to_pdb=True)

