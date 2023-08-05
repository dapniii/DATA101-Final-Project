import pandas as pd
import plotly.express as px

#Import data
df = pd.read_csv('https://media.githubusercontent.com/media/adrian-florin/datasets/main/terrorism_data.csv', encoding="ISO-8859-1", low_memory=False)
df['nperps'] = abs(df['nperps'])
df['nperpcap'] = abs(df['nperpcap'])
df['count'] = 1

years_attack = df['iyear'].unique()
years_options = {1970: '1970', 1972: '1972', 1975: '1975', 1980: '1980', 1985: '1985', 1990: '1990', 1995: '1995', 2000: '2000', 2005: '2005', 2010: '2010', 2014: '2014', 2017: '2017'}
regions = df['region_txt'].unique()

#Mapbox Token
px.set_mapbox_access_token(open(".mapbox_token").read())

#Var Assignment
value_one = 'nkill'
value_two = 'count'
grp = 'gname'
region = 'Middle East & North Africa'

# options
region_option = df['region_txt'].unique()
grp_option = [
    {'Terrorist Group': 'gname'},
    {'Attack Type': 'attacktype1_txt'},
    {'Target Type': 'targtype1_txt'},
    {'Weapon Type': 'weaptype1_txt'}
]

value_one_option = [
    {'Number of People Killed':'nkill'}, 
    {'Number of People Wounded':'nwound'}
]
value_two_option = [
    {'Number of Attacks': 'count'},
    {'Number of Perpetrators': 'nperps'},
    {'Number of Perpetrators Captured': 'nperpcap'}
]

#Data Transformation
df_region = df.loc[df['region_txt'] == region_option[0]].reset_index(drop=True)

# scatter map data
scatter_dict_region = {}
for i in region_option:
    df_selected_region = df[df['region_txt'] == i].reset_index(drop=True)
    scatter_dict_region = {**scatter_dict_region, i : df_selected_region}
    
scatter_dict_top_group = {}
for i in scatter_dict_region:
    df_selected_group = scatter_dict_region.get(i)
    df_selected_group = df_selected_group.groupby(['region_txt', 'gname', ]).size().reset_index(name='attack_count').sort_values(by=['region_txt', 'attack_count'], ascending=[True, False]).head(5)
    name_df = i + " Top 10"
    scatter_dict_top_group = {**scatter_dict_top_group, name_df : df_selected_group}

top_10_groups_list = []
for i in scatter_dict_top_group:
    selected_df = scatter_dict_top_group.get(i)
    top_10_groups_list.append(selected_df)

top_10_groups_per_region = pd.concat(top_10_groups_list)
dropped = ['attack_count', 'region_txt']
top_10_groups_per_region = top_10_groups_per_region.drop(dropped, axis=1).drop_duplicates().reset_index(drop=True)

top_10_groups_per_region_list = top_10_groups_per_region['gname'].tolist()
top_10_groups_all_regions = df[df['gname'].isin(top_10_groups_per_region_list)]


# Horizontal Bar Chart Data
df_hor_bar = df_region.groupby(['country_txt'])[[value_one, value_two]].sum().reset_index()
df_hor_bar = df_hor_bar.sort_values(by=value_one, ascending=True).tail(5)

# Pie Chart Data
df_pie = pd.DataFrame(df_region.groupby(grp)[value_one].sum()).reset_index()
df_pie = df_pie.sort_values(by=value_one, ascending=False).head(5)

# Line Chart Data
df_time = pd.DataFrame(df_region.groupby([grp, 'iyear'], as_index=False)[value_one].sum())
df_time_sorted = df_time.sort_values(by=value_one, ascending=False)
top_five_kills = df_time_sorted[grp].unique()[:5].tolist()
df_time = df_time.loc[(df_time[grp] == top_five_kills[0]) | 
                      (df_time[grp] == top_five_kills[1]) | 
                      (df_time[grp] == top_five_kills[2]) | 
                      (df_time[grp] == top_five_kills[3]) | 
                      (df_time[grp] == top_five_kills[4])]

# Stacked Bar Chart Data
df_stacked = pd.DataFrame(df_region.groupby(['country_txt', grp])[value_one].sum())
df_stacked = df_stacked.sort_values(by=[value_one])
df_stacked = df_stacked.reset_index()

top_group = df_pie[grp].unique().tolist()
top_group.append('country_txt')
df_stacked_pivot = pd.pivot_table(data=df_stacked, 
                                  index='country_txt', 
                                  columns=grp, 
                                  values=value_one)
df_stacked_pivot['total'] = df_stacked_pivot.sum(axis=1)
df_stacked_pivot = df_stacked_pivot.sort_values(by=['total'], ascending=False).head(10)
df_stacked_pivot = df_stacked_pivot.reset_index()
df_stacked_pivot = df_stacked_pivot[top_group]

#Plotly Express Figures

## big map
fig_map = px.scatter_mapbox(top_10_groups_all_regions,
                        lat='latitude',
                        lon='longitude',
                        hover_name="city",
                        color=grp,
                        zoom=1,)
fig_map.update_layout(showlegend=True,
                      autosize=True,)
                    #   labels= {
                    #       'gname': 'Terrorist Group',
                    #   },
                    #   height=500,
                    #   width=450,)

## small map
fig_map_small = px.scatter_mapbox(top_10_groups_all_regions,
                        lat='latitude',
                        lon='longitude',
                        hover_name="city",
                        color=grp,
                        zoom=2)
fig_map_small.update_layout(height=350, width=450, margin={"r":0,"t":0,"l":0,"b":0}, showlegend=False)

## grouped bar
fig_bar = px.bar(df_hor_bar, x=[value_one, value_two], y='country_txt', orientation='h', barmode='group')
fig_bar.update_layout(
    width=400,
    height=350,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=3
    ),
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="right",
        x=0.99
    ),
    font=dict(
            size=9,
    )
)

## pie chart
fig_pie = px.pie(df_pie, values=value_one, names=grp)
fig_pie.update_layout(showlegend=False,
    width=200,
    height=200,
    margin=dict(
        l=100,
        r=0,
        b=0,
        t=0,
        pad=3
    ),
    legend=dict(
        yanchor="bottom",
        y=0.01,
        xanchor="right",
        x=0.99
    ),
    font=dict(
            size=9,
    )
)

## line chart
fig_line = px.area(df_time, x='iyear', y=value_one, color=grp, title=f'Number of {value_one} in {region} per {grp}')
fig_line.update_layout(
    width=400,
    height=350,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=3
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    font=dict(
            size=9,
    )
)

## stacked bar chart
fig_stacked = px.bar(df_stacked_pivot.reset_index(), x='country_txt', y=df_stacked_pivot.columns)
fig_stacked.update_layout(
    width=400,
    height=350,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=3
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),
    font=dict(
            size=9,
    )
)
