{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "467637a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7f89c053",
   "metadata": {},
   "outputs": [
    {
     "ename": "ParserError",
     "evalue": "Error tokenizing data. C error: Expected 1 fields in line 27, saw 367\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mParserError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_3912\\2201450644.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf_budget_data\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mr'https://github.com/samitaahmed/Python-Challenge/blob/main/PyBank/Resources/budget_data.csv'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\util\\_decorators.py\u001b[0m in \u001b[0;36mwrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    309\u001b[0m                     \u001b[0mstacklevel\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mstacklevel\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    310\u001b[0m                 )\n\u001b[1;32m--> 311\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0margs\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    312\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    313\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py\u001b[0m in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    676\u001b[0m     \u001b[0mkwds\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mupdate\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkwds_defaults\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    677\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 678\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    679\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    680\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py\u001b[0m in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    579\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    580\u001b[0m     \u001b[1;32mwith\u001b[0m \u001b[0mparser\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 581\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mparser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    582\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    583\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, nrows)\u001b[0m\n\u001b[0;32m   1251\u001b[0m             \u001b[0mnrows\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalidate_integer\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"nrows\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnrows\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1252\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1253\u001b[1;33m                 \u001b[0mindex\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcolumns\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcol_dict\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1254\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1255\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\c_parser_wrapper.py\u001b[0m in \u001b[0;36mread\u001b[1;34m(self, nrows)\u001b[0m\n\u001b[0;32m    223\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    224\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlow_memory\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 225\u001b[1;33m                 \u001b[0mchunks\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_reader\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread_low_memory\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    226\u001b[0m                 \u001b[1;31m# destructive to chunks\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    227\u001b[0m                 \u001b[0mdata\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0m_concatenate_chunks\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchunks\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader.read_low_memory\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._read_rows\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._tokenize_rows\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\_libs\\parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.raise_parser_error\u001b[1;34m()\u001b[0m\n",
      "\u001b[1;31mParserError\u001b[0m: Error tokenizing data. C error: Expected 1 fields in line 27, saw 367\n"
     ]
    }
   ],
   "source": [
    "df_budget_data = pd.read_csv(r'C:\\Users\\samit\\Desktop\\Github\\Python---Challenge\\PyBank\\Resources/budget_data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a35b12a9",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
