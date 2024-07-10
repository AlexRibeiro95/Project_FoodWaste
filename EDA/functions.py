def map_stages(row, mapping):

    import numpy as np

    for stage, items in mapping.items():
        if row['item'] in items:
            return stage
    return np.nan