# birdsOfEurope
tracking flight trajectories for birds

<cite>
Data cite 
{
  "id": "https://doi.org/10.15468/dl.hbcqmv",
  "doi": "10.15468/DL.HBCQMV",
  "url": "https://www.gbif.org/occurrence/download/0011211-190918142434337",
  "types": {
    "ris": "DATA",
    "bibtex": "misc",
    "citeproc": "dataset",
    "schemaOrg": "Dataset",
    "resourceTypeGeneral": "Dataset"
  },
  "creators": [
    {
      "name": "Occdownload Gbif.Org",
      "nameType": "Organizational",
      "affiliation": [],
      "nameIdentifiers": []
    }
  ],
  "titles": [
    {
      "title": "Occurrence Download"
    }
  ],
  "publisher": "The Global Biodiversity Information Facility",
  "container": {},
  "subjects": [
    {
      "lang": "eng",
      "subject": "GBIF"
    },
    {
      "lang": "eng",
      "subject": "biodiversity"
    },
    {
      "lang": "eng",
      "subject": "species occurrences"
    }
  ],
  "contributors": [],
  "dates": [
    {
      "date": "2019-10-06",
      "dateType": "Created"
    },
    {
      "date": "2019-10-06",
      "dateType": "Updated"
    },
    {
      "date": "2019",
      "dateType": "Issued"
    }
  ],
  "publicationYear": 2019,
  "identifiers": [
    {
      "identifier": "0011211-190918142434337",
      "identifierType": "GBIF"
    }
  ],
  "sizes": [
    "20377605"
  ],
  "formats": [
    "Darwin Core Archive"
  ],
  "rightsList": [
    {
      "rights": "Creative Commons Attribution Non Commercial (CC-BY-NC) 4.0",
      "rightsUri": "http://creativecommons.org/licenses/by-nc/4.0/legalcode"
    }
  ],
  "descriptions": [
    {
      "lang": "eng",
      "description": "A dataset containing 390607 species occurrences available in GBIF matching the query: { \"and\" : [ \"DatasetKey is BirdMap Data - GPS tracking of Storks, Cranes and birds of prey, breeding in Northern and Eastern Europe\", \"HasCoordinate is true\", \"HasGeospatialIssue is false\" ] } The dataset includes 390607 records from 1 constituent datasets: 390607 records from BirdMap Data - GPS tracking of Storks, Cranes and birds of prey, breeding in Northern and Eastern Europe. Data from some individual datasets included in this download may be licensed under less restrictive terms.",
      "descriptionType": "Abstract"
    }
  ],
  "geoLocations": [],
  "fundingReferences": [],
  "relatedIdentifiers": [
    {
      "relationType": "References",
      "relatedIdentifier": "10.15468/vnwmrx",
      "relatedIdentifierType": "DOI"
    }
  ],
  "schemaVersion": "http://datacite.org/schema/kernel-4",
  "providerId": "gbif",
  "clientId": "gbif.gbif",
  "agency": "datacite",
  "state": "findable"
}
</cite>


![Screenshot 2022-09-28 134035](https://user-images.githubusercontent.com/61441879/192770812-ef934a91-e300-4283-9c93-0940565220e6.png)

#IMPORTING LIBRARIES 
```
import pandas as pd 
import numpy as np 
import streamlit as st 
import matplotlib.pyplot as plt 
```



