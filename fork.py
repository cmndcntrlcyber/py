{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#overlays parent process with child\n",
    "\n",
    "import os\n",
    "\n",
    "def child_process () :\n",
    "    print \"I am the child process and my PID is : %d\"%os.getpid()\n",
    "   \n",
    "    print \"The child is exiting\"\n",
    "\n",
    "def parent_process() :\n",
    "\n",
    "    print \"I am the parent process with PID : %d\"%os.getpid()\n",
    "    \n",
    "    childid = os.fork()\n",
    "    \n",
    "    if childpid == 0 :\n",
    "        child_process()\n",
    "    \n",
    "    else : \n",
    "            \n",
    "            print \"We are inside the parent process\"\n",
    "            print \"Our child has the PID : %d\"%childpid\n",
    "            \n",
    "    while True :\n",
    "            pass\n",
    "        \n",
    "parent_process()     "
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
