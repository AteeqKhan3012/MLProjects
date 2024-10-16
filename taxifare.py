{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "61669b0c-a254-42cc-8886-df0825c48f18",
   "metadata": {},
   "outputs": [],
   "source": [
    "def prodDisc(price,discount):\n",
    "     dis=price*discount\n",
    "     print(dis)\n",
    "     price=price-dis\n",
    "     return price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8e99e1dc-c1ba-4638-90d7-74ff6a382434",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter price 2500\n",
      "Enter discount in percent 0.10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "250.0\n",
      "2250.0\n"
     ]
    }
   ],
   "source": [
    "price=float(input(\"Enter price\"))\n",
    "\n",
    "if price>2000:\n",
    "    discount=float(input(\"Enter discount in percent\"))\n",
    "    print(prodDisc(price,discount))\n",
    "else:\n",
    "    print(price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7cf51031-7d9b-434d-9c97-df5461b05ca5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2*3/10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7cfdfdee-3034-4138-9645-ab77273b2abb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.3"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3/10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c5b5c5a0-1d1d-4df5-a9b2-80008bf5e1b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "penPrice=10\n",
    "toyCarPrice=200\n",
    "\n",
    "def shopping():\n",
    "    print(\"1 = Pen\")\n",
    "    print(\"2 = Toy Car\")\n",
    "    choice=int(input())\n",
    "\n",
    "    if choice==1:\n",
    "        qty=int(input(\"Enter quantity for pen\"))\n",
    "        final_price=qty*penPrice\n",
    "        print(final_price)\n",
    "    else:\n",
    "        qty=int(input(\"Enter quantity for toy car\"))\n",
    "        final_price=qty*toyCarPrice\n",
    "        print(final_price)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "663a8412-e805-4fde-b239-01bc252d8f88",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 = Pen\n",
      "2 = Toy Car\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n",
      "Enter quantity for toy car 15\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3000\n"
     ]
    }
   ],
   "source": [
    "shopping()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "17f32fa7-70b5-449a-b7e6-5c6aba1711e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def TaxiFare():\n",
    "    distance=float(input(\"Enter distance\"))\n",
    "    rideType=input(\"Enter ride type\")\n",
    "    time=int(input(\"Enter hours\"))\n",
    "    if distance<10:\n",
    "        if rideType==\"standard\":\n",
    "            if time<8:\n",
    "                taxifare=distance*12\n",
    "                print(taxifare)\n",
    "            elif time>=8 and time<=12:\n",
    "                taxifare=distance*18\n",
    "                print(taxifare)\n",
    "            elif time>12 and time<=16:\n",
    "                taxifare=distance*24\n",
    "                print(taxifare)\n",
    "            else:\n",
    "                 taxifare=distance*30\n",
    "                 print(taxifare)\n",
    "        else:\n",
    "            if time<8:\n",
    "                taxifare=distance*16\n",
    "                print(taxifare)\n",
    "            elif time>=8 and time<=12:\n",
    "                taxifare=distance*24\n",
    "                print(taxifare)\n",
    "            elif time>12 and time<=16:\n",
    "                taxifare=distance*32\n",
    "                print(taxifare)\n",
    "            else:\n",
    "                 taxifare=distance*38\n",
    "                 print(taxifare)\n",
    "    else:\n",
    "        print(\"Not allowed\")\n",
    "                \n",
    "                \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d100a182-c542-472c-a040-1d992aa22e87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter distance 5\n",
      "Enter ride type standard\n",
      "Enter hours 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "60.0\n"
     ]
    }
   ],
   "source": [
    "TaxiFare()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a92fc97-b242-401f-84dd-7f83704d6c5d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
