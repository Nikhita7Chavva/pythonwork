{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number5\n",
      "0\n",
      "1\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "a=0\n",
    "b=1\n",
    "c=a+b\n",
    "n=int(input(\"enter the number\"))\n",
    "\n",
    "print(a)\n",
    "print(b)\n",
    "for i in range(2,n):\n",
    "    print(c)\n",
    "    a=b\n",
    "    b=c\n",
    "    c=a+b\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
