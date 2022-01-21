import pandas as pd
import os

def ReadConvert(
    folder_dir: str,
    Fnames: list,
    file_type: str,
    convert2: str = False
)->dict:
    Data_dict = {}
    for fname in Fnames:
        full_fname = fname + file_type
        full_path = os.path.join(folder_dir, full_fname)
        df = pd.read_csv(full_path, delimiter='\t')
        Data_dict[fname] = df
        if convert2:
            full_fname2 = fname + convert2
            full_path2 = os.path.join(folder_dir, full_fname2)
            df.to_csv(full_path2, sep=',', index=False)
            
    return Data_dict

# Select the needed columns in the imported dataframe
def ColumnSelect(data_dict, ValidCols):
    train_dict = {}
    keys = [key for key in ValidCols.keys() if key != 'default']
    for key in keys:
        Cols = ValidCols[key]['Columns'] + ValidCols['default']['Columns']
        
        try:
            Filter = ValidCols[key]['FILTER']
            Value = ValidCols[key]['INCLUSION']
            if Value is None:
                train_dict[key] = data_dict[key].loc[
                                            data_dict[key][Filter].isnull(),
                                            Cols
                                    ].copy()
            else:
                train_dict[key] = data_dict[key].loc[
                                            data_dict[key][Filter] == Value,
                                            Cols
                                    ].copy()
        except KeyError:
            train_dict[key] = data_dict[key].loc[:,Cols].copy()
    return train_dict