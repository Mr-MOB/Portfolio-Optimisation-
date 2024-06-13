import pandas as pd

# Sample data
data = {
    'Asset': ['Asset1', 'Asset2', 'Asset3', 'Asset4', 'Asset5'],
    'PE_Ratio': [10, 15, 20, 25, 30],
    'Debt_to_Asset_Ratio': [0.2, 0.4, 0.6, 0.8, 1.0],
    'ROCE': [5, 10, 15, 20, 25],
    'ROE': [10, 15, 20, 25, 30],
    'PB_Ratio': [1, 1.5, 2, 2.5, 3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to categorize based on standard benchmarks
def categorize_pe_ratio(pe_ratio):
    if pe_ratio < 10:
        return 'Very Low'
    elif pe_ratio < 15:
        return 'Low'
    elif pe_ratio < 20:
        return 'Moderate'
    elif pe_ratio < 25:
        return 'High'
    else:
        return 'Very High'

def categorize_debt_to_asset_ratio(dta_ratio):
    if dta_ratio < 0.2:
        return 'Very Low'
    elif dta_ratio < 0.4:
        return 'Low'
    elif dta_ratio < 0.6:
        return 'Moderate'
    elif dta_ratio < 0.8:
        return 'High'
    else:
        return 'Very High'

def categorize_roce(roce):
    if roce < 10:
        return 'Very Low'
    elif roce < 15:
        return 'Low'
    elif roce < 20:
        return 'Moderate'
    elif roce < 25:
        return 'High'
    else:
        return 'Very High'

def categorize_roe(roe):
    if roe < 10:
        return 'Very Low'
    elif roe < 15:
        return 'Low'
    elif roe < 20:
        return 'Moderate'
    elif roe < 25:
        return 'High'
    else:
        return 'Very High'

def categorize_pb_ratio(pb_ratio):
    if pb_ratio < 1:
        return 'Very Low'
    elif pb_ratio < 1.5:
        return 'Low'
    elif pb_ratio < 2:
        return 'Moderate'
    elif pb_ratio < 2.5:
        return 'High'
    else:
        return 'Very High'

# Categorize each ratio
df['PE_Category'] = df['PE_Ratio'].apply(categorize_pe_ratio)
df['Debt_to_Asset_Category'] = df['Debt_to_Asset_Ratio'].apply(categorize_debt_to_asset_ratio)
df['ROCE_Category'] = df['ROCE'].apply(categorize_roce)
df['ROE_Category'] = df['ROE'].apply(categorize_roe)
df['PB_Category'] = df['PB_Ratio'].apply(categorize_pb_ratio)

# Calculate an overall score based on the categories
category_scores = {
    'Very Low': 1,
    'Low': 2,
    'Moderate': 3,
    'High': 4,
    'Very High': 5
}

def calculate_overall_score(row):
    total_score = (category_scores[row['PE_Category']] +
                   category_scores[row['Debt_to_Asset_Category']] +
                   category_scores[row['ROCE_Category']] +
                   category_scores[row['ROE_Category']] +
                   category_scores[row['PB_Category']])
    return total_score / 5

df['Overall_Score'] = df.apply(calculate_overall_score, axis=1)

# Apply final categorization based on overall score
def categorize_overall_score(score):
    if score <= 1.5:
        return 'Very Low'
    elif score <= 2.5:
        return 'Low'
    elif score <= 3.5:
        return 'Moderate'
    elif score <= 4.5:
        return 'High'
    else:
        return 'Very High'

df['Final_Category'] = df['Overall_Score'].apply(categorize_overall_score)

print(df)
