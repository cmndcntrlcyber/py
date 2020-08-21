{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import thread\n",
    "import time\n",
    "\n",
    "def worker_thread(id) :\n",
    "    \n",
    "    print \"Thread ID %d now alive\" %id\n",
    "    \n",
    "    count = 1\n",
    "    while True : \n",
    "            print \"Thread with ID %d has a counter value %d\"% (id, count)\n",
    "            time.sleep(2)\n",
    "            count += 1\n",
    "\n",
    "for i in range(5) :\n",
    "        thread.start_new_thread(worker_thread, (i,))\n",
    "\n",
    "print \"Main thread going for an infinite wait loop\"\n",
    "\n",
    "while True :\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import threading\n",
    "import Queue\n",
    "import time\n",
    "\n",
    "class WorkerThread(threading.Thread) :\n",
    "    \n",
    "    def _init_(self, queue) :\n",
    "            threading.Thread._init_(self)\n",
    "            self.queue = queue\n",
    "            \n",
    "    def run(self) :\n",
    "            print \"In WorkerThread\"\n",
    "            while True :\n",
    "                    counter = self.queue.get()\n",
    "                    print \"Ordered to sleep for %d seconds!\"%counter\n",
    "                    time.sleep(counter)\n",
    "                    print \"Finished sleeping for %d second\"%counter\n",
    "                    self.queue.task_done()\n",
    "\n",
    "queue = Queue.Queue()\n",
    "\n",
    "for i in range(10) :\n",
    "        print \"creating WorkerThread : %d\"%i\n",
    "        worker = WorkerThread(queue)\n",
    "        worker.setDaemon(True)\n",
    "        worker.start()\n",
    "        print \"WorkerThread %d Created!\"%i\n",
    "        \n",
    "for j in range(10) :\n",
    "    queue.put(j)"
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
