{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fdesc = open(\"\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for count in range(0,100):\n",
    "    fdesc.write(str(count) + \"\\n\")\n",
    "    \n",
    "fdesc.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "fdesc = open(\"spse.txt\", \"a\")\n",
    "\n",
    "for count in range(100, 200) :\n",
    "    fdesc.write(str(count) + \"\\n\")\n",
    "\n",
    "fdesc.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fdesc = open(\"spse.txt\", \"r\")\n",
    "\n",
    "for line in fdesc.readlines() : \n",
    "    print line.strip()\n",
    "    \n",
    "fdesc.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "os.rename(\"spse.txt\", \"spse2.txt\")"
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
