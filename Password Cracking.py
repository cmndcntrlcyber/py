{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'secret.zip'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-661c18b6c931>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mzipfile\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[0mz\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mzipfile\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mZipFile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"secret.zip\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mz\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mprintdir\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mz\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\zipfile.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, file, mode, compression, allowZip64, compresslevel)\u001b[0m\n\u001b[0;32m   1238\u001b[0m             \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1239\u001b[0m                 \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1240\u001b[1;33m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfp\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mio\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfile\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfilemode\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1241\u001b[0m                 \u001b[1;32mexcept\u001b[0m \u001b[0mOSError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1242\u001b[0m                     \u001b[1;32mif\u001b[0m \u001b[0mfilemode\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mmodeDict\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'secret.zip'"
     ]
    }
   ],
   "source": [
    "#Protected Zip File Cracking\n",
    "#Task 1. Read the archive and print the list of files inside it.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"secret.zip\")\n",
    "z.printdir()\n",
    "z.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Protected Zip File Cracking\n",
    "# Task 2. Generate a dictionary \"dict.txt\" containing all possible passwords, matching the password policy.\n",
    "\n",
    "import itertools\n",
    "alphabets = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5']\n",
    "f = open(\"dict.txt\", \"w\")\n",
    "for passlen in [6]:\n",
    "    combinations = itertools.product(alphabets, repeat = passlen)\n",
    "    for combination in combinations:\n",
    "        f.write(''.join(combination)+\"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Protected Zip File Cracking\n",
    "#Task 3. Bruteforce the \"secret.zip\" using the generated dictionary file and print the correct password.\n",
    "\n",
    "import zipfile\n",
    "cracked = False\n",
    "z = zipfile.ZipFile(\"secret.zip\")\n",
    "with open(\"dict.txt\") as f:\n",
    "    lines = f.readlines()\n",
    "for password in lines:\n",
    "    password = password.replace('\\n','')\n",
    "    try:\n",
    "        z.extractall(pwd=password)\n",
    "        correct_password = 'Correct password: %s' % password\n",
    "        cracked = True\n",
    "        break\n",
    "    except:\n",
    "        pass\n",
    "\n",
    "if cracked:\n",
    "    print correct_password\n",
    "else:\n",
    "    print \"Password not found\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Protected Zip File Cracking\n",
    "#Task 4. Print the contents of all the extracted file.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"secret.zip\")\n",
    "files = z.namelist()\n",
    "z.setpassword(\"b1c1e5\")\n",
    "z.extractall()\n",
    "z.close()\n",
    "for extracted_file in files:\n",
    "    print \"File name:\"+extracted_file+\"\\n\\nContent:\"\n",
    "    with open(extracted_file) as f:\n",
    "        content = f.readlines()\n",
    "        print ''.join(content)\n",
    "        print '\\n\\n'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack PDF Password\n",
    "# Task 1. Read the archive and print the list of files inside it.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "z.printdir()\n",
    "z.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack PDF Password\n",
    "#Task 2. Bruteforce the \"PDF.zip\" using the given dictionary file and print the correct password.\n",
    "\n",
    "import zipfile\n",
    "cracked = False\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "with open(\"dictionary.txt\") as f:\n",
    "    lines = f.readlines()\n",
    "for password in lines:\n",
    "    password = password.replace('\\n','')\n",
    "    try:\n",
    "        z.extractall(pwd=password)\n",
    "        correct_password = 'Correct password: %s' % password\n",
    "        cracked = True\n",
    "        break\n",
    "    except:\n",
    "        pass\n",
    "\n",
    "if cracked:\n",
    "    print correct_password\n",
    "else:\n",
    "    print \"Password not found\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack PDF Password\n",
    "# Task 3. Extract the files.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "files = z.namelist()\n",
    "z.setpassword(\"maprchem56458\")\n",
    "z.extractall()\n",
    "z.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack Zip Archives II\n",
    "# Task 1. Read the archive and print the list of files inside it.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "z.printdir()\n",
    "z.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack Zip Archives II\n",
    "# Task 2. Bruteforce the \"PDF.zip\" using the given dictionary file and print the correct password.\n",
    "\n",
    "import zipfile\n",
    "cracked = False\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "with open(\"dictionary.txt\") as f:\n",
    "    lines = f.readlines()\n",
    "for password in lines:\n",
    "    password = password.replace('\\n','')\n",
    "    try:\n",
    "        z.extractall(pwd=password)\n",
    "        correct_password = 'Correct password: %s' % password\n",
    "        cracked = True\n",
    "        break\n",
    "    except:\n",
    "        pass\n",
    "\n",
    "if cracked:\n",
    "    print correct_password\n",
    "else:\n",
    "    print \"Password not found\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Crack Zip Archives II\n",
    "# Task 3. Extract the files.\n",
    "\n",
    "import zipfile\n",
    "z = zipfile.ZipFile(\"PDF.zip\")\n",
    "files = z.namelist()\n",
    "z.setpassword(\"\")\n",
    "z.extractall()\n",
    "z.close()"
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
