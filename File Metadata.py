{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# OSINT: PDF Metadata\n",
    "# Task 1: Print the names of all files in the directory.\n",
    "\n",
    "from PyPDF2 import PdfFileReader, PdfFileWriter\n",
    "import os\n",
    "\n",
    "file_list =  os.listdir(\"PDF\")\n",
    "\n",
    "counter = 1\n",
    "for f in file_list:\n",
    "    print str(counter)+\"  \"+f\n",
    "    counter = counter + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# OSINT: PDF Metadata\n",
    "# Task 2. Print the superset of all attributes present in PDF metsadata.\n",
    "\n",
    "from PyPDF2 import PdfFileReader, PdfFileWriter\n",
    "import os\n",
    "\n",
    "directory = \"PDF/\"\n",
    "file_list =  os.listdir(directory)\n",
    "\n",
    "attr_superset = []\n",
    "\n",
    "for f in file_list:\n",
    "    # Opening file\n",
    "    f = directory+f\n",
    "    with open(f, 'rb') as input_file:\n",
    "        reader = PdfFileReader(input_file)\n",
    "        metadata = reader.getDocumentInfo()\n",
    "        for item, value in metadata.iteritems():\n",
    "            item = item.replace('/','')\n",
    "            if item not in attr_superset:\n",
    "                attr_superset.append(item)\n",
    "            \n",
    "print attr_superset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#OSINT: PDF Metadata\n",
    "# Task 3. Print superset of softwares used to create the PDF files.\n",
    "\n",
    "from PyPDF2 import PdfFileReader, PdfFileWriter\n",
    "import os\n",
    "\n",
    "def superset(target_field):\n",
    "    directory = \"PDF/\"\n",
    "    file_list =  os.listdir(directory)\n",
    "\n",
    "    result_supterset = []\n",
    "\n",
    "    for f in file_list:\n",
    "        # Opening file\n",
    "        f = directory+f\n",
    "        with open(f, 'rb') as input_file:\n",
    "            reader = PdfFileReader(input_file)\n",
    "            metadata = reader.getDocumentInfo()\n",
    "            if target_field in metadata:\n",
    "                field_value = metadata.get(target_field)\n",
    "                if field_value not in attr_superset:\n",
    "                    result_supterset.append(field_value)\n",
    "\n",
    "    return result_supterset\n",
    "    \n",
    "print superset('/Creator')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#OSINT: PDF Metadata\n",
    "# Task 4. Print superset of authors who created these PDF files.\n",
    "\n",
    "print superset('/Author')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#OSINT: PDF Metadata\n",
    "# Task 5. Print superset of values for all fields present in the attribute superset list.\n",
    "\n",
    "for attr in attr_superset:\n",
    "    attr = '/'+attr\n",
    "    print \"==========> \"+attr\n",
    "    print superset(attr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#OSINT: PDF Metadata\n",
    "# Task 6. List the titles of all books from author \"Disney\".\n",
    "\n",
    "from PyPDF2 import PdfFileReader, PdfFileWriter\n",
    "import os\n",
    "\n",
    "def search_pdfs(target_field, target_value):\n",
    "    directory = \"PDF/\"\n",
    "    file_list =  os.listdir(directory)\n",
    "\n",
    "    files_matched = {}\n",
    "\n",
    "    for f in file_list:\n",
    "        # Opening file\n",
    "        f = directory+f\n",
    "        with open(f, 'rb') as input_file:\n",
    "            reader = PdfFileReader(input_file)\n",
    "            metadata = reader.getDocumentInfo()\n",
    "            if target_field in metadata:\n",
    "                field_value = metadata.get(target_field)\n",
    "                if target_value in field_value:\n",
    "                    files_matched[f.replace(directory, '')] = field_value\n",
    "                    \n",
    "    return files_matched\n",
    "\n",
    "print search_pdfs('/Author','Disney')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#OSINT: PDF Metadata\n",
    "# Task 7. Print the list of files which were generated using Adobe products.\n",
    "\n",
    "print search_pdfs('/Creator','Adobe')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 1. Import the library and load notepad.exe binary.\n",
    "\n",
    "import pefile\n",
    "\n",
    "pe = pefile.PE('notepad.exe')\n",
    "\n",
    "pe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 2. Print the structure of the file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 3. Print the PE header"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 4. Import pprint and print the PE header.\n",
    "\n",
    "import pprint\n",
    "\n",
    "pprint.pprint(dir(pe.DOS_HEADER))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 5. Print the magic number of the PE file in decimal, hex and ASCII\n",
    "\n",
    "# Decimal\n",
    "print pe.DOS_HEADER.e_magic\n",
    "\n",
    "# Hex\n",
    "print hex(pe.DOS_HEADER.e_magic)\n",
    "\n",
    "# ASCII Char string\n",
    "a = hex(pe.DOS_HEADER.e_magic)\n",
    "a =  a[2:]\n",
    "print a.decode(\"hex\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 6. Print number of sections in the PE file\n",
    "\n",
    "print pe.FILE_HEADER.NumberOfSections"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 7. Print sections of the PE file\n",
    "\n",
    "print pe.sections"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 8. Print the first section of the PE file\n",
    "\n",
    "pprint.pprint(dir(pe.sections[0]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 9. Print the name and size of raw data for each section.\n",
    "\n",
    "for section in pe.sections:\n",
    "    print section.Name\n",
    "    print section.SizeOfRawData\n",
    "    print '\\n'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Analyzing PE File\n",
    "# Task 10: Load notepad_upx.exe file and list the sections.\n",
    "\n",
    "import pefile\n",
    "\n",
    "pe = pefile.PE('notepad_upx.exe')\n",
    "\n",
    "for section in pe.sections:\n",
    "    print section.Name\n",
    "    print section.SizeOfRawData\n",
    "    print '\\n'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
