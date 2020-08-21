{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.getcwd()\n",
    "os.mkdir(\"NewDirectory\")\n",
    "os.listdir(\".\")\n",
    "os.listdir(\"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for item in os.listdir(\".\") : \n",
    "        if os.path.isfile(item) :\n",
    "            print item + \" is a file\"\n",
    "        elif os.path.isdir(item) :\n",
    "            print item + \" is a directory\"\n",
    "        else : \n",
    "            print \"unknown!\"  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for item in glob.glob(os.path.join(\".\",\"*.py\")) :\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for item in glob.glob(os.path.join(\".\", \"*\")) :\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for item in glob.glob(os.path.join(\".\", \"*.txt\")) :\n",
    "    print item"
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
