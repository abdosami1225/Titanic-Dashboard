
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Titanic.csv')
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['Survival'] = df['Survived'].map({0: 'Died', 1: 'Survived'})
df['Class_Label'] = df['Pclass'].map(
    {1: '1st Class', 2: '2nd Class', 3: '3rd Class'})

app = Dash(__name__)
server = app.server

app.layout = html.Div([

    # Header
    html.Div([
        html.H1("🚢 Titanic Survival Analysis Dashboard",
                style={'textAlign': 'center', 'color': '#2c3e50', 'marginTop': 20}),
        html.P("Interactive Data Visualization & Analysis",
               style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': 18}),]),

    html.Hr(),

    # Stats Cards
    html.Div([
        html.Div([
            html.H3(f"{len(df)}",
                    style={'color': '#3498db', 'margin': 0}),
            html.P("Total Passengers", style={'margin': 5})],
            style={'textAlign': 'center', 'padding': 20, 'backgroundColor': '#ecf0f1', 'margin': 10, 'borderRadius': 10, 'flex': 1}),

        html.Div([
            html.H3(f"{df['Survived'].sum()}",
                    style={'color': '#27ae60', 'margin': 0}),
            html.P(f"Survivors ({df['Survived'].mean()*100:.1f}%)",
                   style={'margin': 5})],
                 style={'textAlign': 'center', 'padding': 20, 'backgroundColor': '#ecf0f1', 'margin': 10, 'borderRadius': 10, 'flex': 1}),

        html.Div([
            html.H3(f"{len(df) - df['Survived'].sum()}",
                    style={'color': '#e74c3c', 'margin': 0}),
            html.P(f"Casualties ({(1-df['Survived'].mean())*100:.1f}%)",
                   style={'margin': 5})],
                 style={'textAlign': 'center', 'padding': 20, 'backgroundColor': '#ecf0f1', 'margin': 10, 'borderRadius': 10, 'flex': 1}),

        html.Div([
            html.H3(f"{df['Age'].mean():.1f}",
                    style={'color': '#9b59b6', 'margin': 0}),
            html.P("Average Age", style={'margin': 5})],
            style={'textAlign': 'center', 'padding': 20, 'backgroundColor': '#ecf0f1', 'margin': 10, 'borderRadius': 10, 'flex': 1}),],
        style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'center'}),

    html.Hr(),

    html.Div([
        html.H3("🎛️ Interactive Filters",
                style={'color': '#2c3e50', 'marginBottom': 20}),

        html.Div([
            html.Div([
                html.Label("Passenger Class:", style={
                           'fontWeight': 'bold', 'marginBottom': 5}),
                dcc.Dropdown(
                    id='class-dropdown',
                    options=[
                        {'label': 'All Classes', 'value': 'All'},
                        {'label': '1st Class', 'value': 1},
                        {'label': '2nd Class', 'value': 2},
                        {'label': '3rd Class', 'value': 3}],
                    value='All',
                    style={'width': '200px'}),],
                style={'marginRight': 30}),

            html.Div([
                html.Label("Gender:", style={
                           'fontWeight': 'bold', 'marginBottom': 5}),
                dcc.Dropdown(
                    id='gender-dropdown',
                    options=[
                        {'label': 'All', 'value': 'All'},
                        {'label': 'Male', 'value': 'male'},
                        {'label': 'Female', 'value': 'female'}],
                    value='All',
                    style={'width': '200px'}),]),],
            style={'display': 'flex', 'flexWrap': 'wrap'}),],
        style={'padding': 20, 'backgroundColor': '#ecf0f1', 'margin': 20, 'borderRadius': 10}),

    html.Div([
        html.Div([
            html.Div([dcc.Graph(id='survival-pie')],
                     style={'flex': 1, 'padding': 10}),
            html.Div([dcc.Graph(id='gender-bar')],
                     style={'flex': 1, 'padding': 10}),
            html.Div([dcc.Graph(id='class-bar')],
                     style={'flex': 1, 'padding': 10}),],
                 style={'display': 'flex', 'flexWrap': 'wrap'}),

        html.Div([
            html.Div([dcc.Graph(id='age-histogram')],
                     style={'flex': 1, 'padding': 10}),
            html.Div([dcc.Graph(id='fare-histogram')],
                     style={'flex': 1, 'padding': 10}),],
                 style={'display': 'flex', 'flexWrap': 'wrap'}),

        html.Div([
            html.Div([dcc.Graph(id='scatter-plot')],
                     style={'flex': 1, 'padding': 10}),
            html.Div([dcc.Graph(id='heatmap')], style={
                'flex': 1, 'padding': 10}),],
            style={'display': 'flex', 'flexWrap': 'wrap'}),]),

    html.Hr(),
    html.Div([
        html.P("Built with Dash & Plotly | Titanic Dataset Analysis",
               style={'textAlign': 'center', 'color': '#7f8c8d'}),
        html.P("Created for Data Visualization Assignment",
               style={'textAlign': 'center', 'color': '#95a5a6', 'fontSize': 12}),],
             style={'marginBottom': 20}),

], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f8f9fa', 'padding': '0 20px'})


@app.callback(
    [Output('survival-pie', 'figure'),
     Output('gender-bar', 'figure'),
     Output('class-bar', 'figure'),
     Output('age-histogram', 'figure'),
     Output('fare-histogram', 'figure'),
     Output('scatter-plot', 'figure'),
     Output('heatmap', 'figure')],
    [Input('class-dropdown', 'value'),
     Input('gender-dropdown', 'value')])
def update_all_charts(selected_class, selected_gender):
    filtered = df.copy()

    if selected_class != 'All':
        filtered = filtered[filtered['Pclass'] == selected_class]

    if selected_gender != 'All':
        filtered = filtered[filtered['Sex'] == selected_gender]

    survival_counts = filtered['Survival'].value_counts()
    fig1 = px.pie(
        values=survival_counts.values,
        names=survival_counts.index,
        title="Overall Survival Rate",
        color=survival_counts.index,
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        hole=0.4)
    fig1.update_layout(height=400)

    gender_data = filtered.groupby(
        ['Sex', 'Survival']).size().reset_index(name='Count')
    fig2 = px.bar(
        gender_data, x='Sex', y='Count', color='Survival',
        title="Survival by Gender",
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        barmode='group')
    fig2.update_layout(height=400)

    class_data = filtered.groupby(
        ['Pclass', 'Survival']).size().reset_index(name='Count')
    fig3 = px.bar(
        class_data, x='Pclass', y='Count', color='Survival',
        title="Survival by Passenger Class",
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        barmode='group')
    fig3.update_xaxes(tickvals=[1, 2, 3], ticktext=['1st', '2nd', '3rd'])
    fig3.update_layout(height=400)

    fig4 = px.histogram(
        filtered, x='Age', color='Survival',
        title="Age Distribution by Survival",
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        opacity=0.7,
        barmode='overlay',
        nbins=30)
    fig4.update_layout(height=400)

    fare_clean = filtered[filtered['Fare'] < filtered['Fare'].quantile(0.95)]
    fig5 = px.histogram(
        fare_clean, x='Fare', color='Survival',
        title="Fare Distribution (95th percentile)",
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        opacity=0.7,
        barmode='overlay',
        nbins=40)
    fig5.update_layout(height=400)

    fig6 = px.scatter(
        filtered, x='Age', y='Fare', color='Survival',
        title="Age vs Fare (colored by Survival)",
        color_discrete_map={'Died': '#e74c3c', 'Survived': '#27ae60'},
        opacity=0.6,
        hover_data=['Class_Label', 'Sex'])
    fig6.update_layout(height=400, yaxis_range=[0, 300])

    pivot = filtered.pivot_table(
        values='Survived',
        index='Sex',
        columns='Pclass',
        aggfunc='mean') * 100

    fig7 = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=['1st Class', '2nd Class', '3rd Class'],
        y=['Female', 'Male'],
        colorscale='RdYlGn',
        text=pivot.values.round(1),
        texttemplate='%{text}%',
        textfont={"size": 14},
        colorbar=dict(title="Survival Rate (%)")))
    fig7.update_layout(
        title="Survival Rate by Gender & Class",
        height=400)

    return fig1, fig2, fig3, fig4, fig5, fig6, fig7


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8050)
