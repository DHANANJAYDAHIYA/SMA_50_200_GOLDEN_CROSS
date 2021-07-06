{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'QCAlgorithm' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-efc0b7e72667>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mclass\u001b[0m \u001b[0mSMA20050\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mQCAlgorithm\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mInitialize\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSetStartDate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m2017\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m         \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSetCash\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m10000\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'QCAlgorithm' is not defined"
     ]
    }
   ],
   "source": [
    "class SMA20050(QCAlgorithm):\n",
    "\n",
    "    def Initialize(self):\n",
    "        self.SetStartDate(2017, 1, 1) \n",
    "        self.SetCash(10000) \n",
    "        self.spy = self.AddCrypto(\"BTCUSD\", Resolution.Hour).Symbol\n",
    "        self.Fast = self.SMA(self.spy,50,Resolution.Daily)\n",
    "        self.Slow = self.SMA(self.spy,200,Resolution.Daily)\n",
    "        self.SetBrokerageModel(BrokerageName.Bitfinex, AccountType.Margin)\n",
    "        \n",
    "        self.previous = self.Time.min\n",
    "        self.Tolerance = 0.00015\n",
    "    def OnData(self, data):\n",
    "        \n",
    "        if not self.Slow.IsReady :return\n",
    "        if  self.previous is  None or self.previous.day==self.Time.day:return\n",
    "        holdings = self.Portfolio[self.spy].Quantity\n",
    "        if holdings<=0:\n",
    "            if self.Fast.Current.Value>self.Slow.Current.Value*(1+self.Tolerance):\n",
    "                self.SetHoldings(self.spy,1)\n",
    "                self.Debug(\"BUY  >> \" + str(self.Securities[self.spy].Price))\n",
    "        else:\n",
    "            \n",
    "            if self.Fast<self.Slow:\n",
    "                self.SetHoldings(self.spy,-1)\n",
    "        if self.Portfolio[self.spy].UnrealizedProfit<= -420:\n",
    "                self.Debug(\"Sell at \"+str(self.Securities[self.spy].Price))\n",
    "                self.Liquidate()\n",
    "        self.previous = self.Time"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
