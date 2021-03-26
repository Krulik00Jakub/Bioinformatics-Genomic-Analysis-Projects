# IslandViewer-4-batch-submission-script
Script for the submission of multiple GENBANK or EMBL files for analysis to IslandViewer 4. 

This script automates the submission of genome files for analysis to IslandViewer 4 by storing paths to genome files that the user would like to submit,
and systematically submitting them to the IslandViewer 4 server at http://www.pathogenomics.sfu.ca/islandviewer/.

Source code obtained from http://www.pathogenomics.sfu.ca/islandviewer/http_api/.

Before using the script, please ensure that you have the requests_toolbelt library installed
(i.e. "pip install requests-toolbelt"), and please replace the placeholder on line 74 of the genomeSubmissionScript.py with your authentication token.
