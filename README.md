Identipyer
========

In making decisions about how data can be aggregated and visualized it's helpful to understand what type of information the data contains. Beyond simple classifications like discrete vs continuous or `int` vs `str`, this becomes complex. Is a column of strings a unique identifier, or should we treat it like a category for group by aggregations? Is the data best displayed as a bar chart, line chart, or even a choropleth map? How could/should the data be augmented for a more complete analysis? Can it be geocoded, or passed to a demographics classifier to predict age/gender/etc?

With identipyer, we attempt to answer these questions using a template-matching approach that labels a column of values based on its contents. 

### Setup

```
git clone https://github.com/popily/identipyer
cd identipyer
pip install -r requirements.txt
```

### Getting Started

Imagine a csv file, `customers.csv`, with the following data.

| Name          | Age | Occupation | 
|---------------|-----|------------| 
| John Smith    | 25  | Accountant | 
| Jane Doe      | 30  | Lawyer     | 
| Jack Jones    | 50  | Doctor     | 
| Janet Johnson | 40  | Executive  | 

Using the `pandas` library for Python data analysis, we read the contents of the file into a dataframe.

```python
import pandas as pd

df = pd.read_csv('customers.csv')
```

We can now access the values in each column of column of data, and use `identipyer` to assign a semantic type label.

```python    
from identipyer.guesser import guess

header = 'Occupation'
values = df.Occupation.values.tolist()

guesses = guess(values,header=header)
```

Identipyer will return a list of strings, one for each type template that was matched.

```python
print guesses
# ['category']
```

The following semantic types are available:

- **date** something `dateutil.parser` can parse into a `datetime` object 
- **int** a whole number 
- **bool** y/n or yes/no or something true/falsey 
- **float** a number with a decimal
- **category** something you might want to group records by
- **text** string longer than 90 characters (something you could get names/places/sentiment/etc from) 
- **id** unique for each row
- **coord** a float that might be a latitude or longitude
- **coord_pair** string that looks like "coord,coord"
- **proportion** column where all values sum to 1 or 100
- **street** house number + street name
- **city** one of the world's 80,000 largest cities
- **region** smaller than a country, bigger than a city. state, province, etc
- **country** a country name on the [ISO 3166 list](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)
- **phone** a phone number
- **email** an email address
- **url** web address with or without http:// (so http://google.com or google.com)
- **address** a full address you could geocode with a service like Google Maps
