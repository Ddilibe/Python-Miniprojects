{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4721e72c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0d1aced5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ndsidnneoma</td>\n",
       "      <td>21</td>\n",
       "      <td>2000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Dilibe</td>\n",
       "      <td>20</td>\n",
       "      <td>2001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Kachi</td>\n",
       "      <td>18</td>\n",
       "      <td>2003</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Azokam</td>\n",
       "      <td>16</td>\n",
       "      <td>2005</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Gogo</td>\n",
       "      <td>14</td>\n",
       "      <td>2007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Nma</td>\n",
       "      <td>9</td>\n",
       "      <td>2013</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Name  Age  Year\n",
       "0  Ndsidnneoma   21  2000\n",
       "1       Dilibe   20  2001\n",
       "2        Kachi   18  2003\n",
       "3       Azokam   16  2005\n",
       "4         Gogo   14  2007\n",
       "5          Nma    9  2013"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "children = {\n",
    "    'Name':['Nneoma', 'Dilibe','Kachi','Azokam','Gogo','Nma'],\n",
    "    'Age':[21,20,18,16,14,9],\n",
    "    'Year':[2000,2001,2003,2005,2007,2013]\n",
    "}\n",
    "pd_children = pd.DataFrame(children)\n",
    "pd_children"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3a1609c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I like the way juypter notebook is oh \n"
     ]
    }
   ],
   "source": [
    "print(\"I like the way juypter notebook is oh \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9873301",
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
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
