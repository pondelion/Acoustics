import numpy as np


def get_lbps_weights(
    df: np.ndarray
):
    """Calculate Local Binary Pattern (LBP) and weights.

    Args:
        df (numpy.ndarray): 2 dimentonal data

    Returns:
        lbps (numpy.ndarray): Local Binary Pattern dataframe with same shape as df.
        weights (numpy.ndarray): Weights dataframe with same shape as df.
    """

    dim_x = df.shape[1]
    dim_y = df.shape[0]

    data_expanded = np.zeros([dim_y+2, dim_x+2])
    data_expanded[:, :] = np.nan
    data_expanded[1:-1, 1:-1] = df

    stacked_shifted_data = np.array([data_expanded])

    DXDY = (
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1)
    )

    for dx, dy in DXDY:
        if dx == 0 and dy == 0:
            continue
        shifted_data = np.zeros([dim_y+2, dim_x+2])
        shifted_data[:, :] = np.nan
        shifted_data[(1+dy):(dim_y+1+dy), (1+dx):(dim_x+1+dx)] = df
        stacked_shifted_data = np.vstack([stacked_shifted_data, [shifted_data]])

    # (9, dim_x+2, dim_y+2) => (9, dim_x, dim_y)
    stacked_shifted_data = stacked_shifted_data[:, 1:-1, 1:-1]

    # Calculation for weights (standard deviations).
    means = np.nanmean(stacked_shifted_data, axis=0)
    weights = np.nanstd(stacked_shifted_data - means, axis=0)

    # Calculation for Local Binary Pattern (LBP).
    stacked_bins = (stacked_shifted_data[1:, :, :] > stacked_shifted_data[0, :, :]).astype(int)
    for i in range(stacked_bins.shape[0]):
        stacked_bins[i, :, :] *= 2**i

    lbps = stacked_bins.sum(axis=0)

    return lbps, weights
