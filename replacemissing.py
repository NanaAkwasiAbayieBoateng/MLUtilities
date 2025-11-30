''' This function takes a dataframe as input ,replaces missing values for categorical features with
     -9999.01 and for the numeric columns, the median of the column.
 
replacemissing(data) 
'''

def replacemissing(data,replace_value=-9999.01):
  
    categorical_cols = [x for x in data.columns if data[x].dtypes  in ['object']]
    numeric_cols = [x for x in data.columns if data[x].dtypes  in ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']]
    #df.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64'])
    data[categorical_cols].fillna(replace_value,inplace=True)
    data[numeric_cols] = data[numeric_cols].apply(lambda x: x.fillna(x.median()),axis=0)
    return data