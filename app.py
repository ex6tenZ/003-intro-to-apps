######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
artist=['Roddy Rich', 'Lil Nas X', 'Eminem', 'Olivia']
song_dur=[3.21, 2.09, 2.89, 3.05]
title_len=[2, 2, 5, 3]
color1='blue'
color2='black'
mytitle='Artist song durations & number of titles'

label1='duration'
label2='number of titles'

########### Set up the chart

def make_that_cool_barchart(artist, song_dur, title_len, color1, color2, mytitle):
    dur = go.Bar(
        x=artist,
        y=song_dur,
        name=label1,
        marker={'color':color1}
    )
    leng = go.Bar(
        x=artist,
        y=title_len,
        name=label2,
        marker={'color':color2}
    )

    artist_data = [dur, leng]
    artist_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    return go.Figure(data=artist_data, layout=artist_layout)


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(artist, song_dur, title_len, color1, color2, mytitle)
    fig.write_html('docs/barchart.html')
    print('We successfully updated the barchart!')
