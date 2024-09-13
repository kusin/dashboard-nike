# import library
import plotly.express as px

# ...
def barplot(df, x, y, title):

  # create barplot
  fig = px.bar(df, x=x, y=y, text_auto='.4s',)

  # update-labels
  fig.update_traces(marker_color=px.colors.sequential.Bluyl)
  fig.update_layout(title=title, xaxis_title="", yaxis_title="")
  
  # return values
  return fig

# ...
def pieplot(df, values, names, title):
  
  # crate pieplot
  fig = px.pie(df, values=values, names=names, hole=0.5, color_discrete_sequence=px.colors.sequential.Bluyl)
  
  # update-labels
  fig.update_traces(textinfo="label+percent")
  fig.update_layout(title=title, xaxis_title="", yaxis_title="", showlegend=False)
  
  # return values
  return fig