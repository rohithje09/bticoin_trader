import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from backtest import run_backtest
from strategies import MomentumStrategy, MeanReversionStrategy, TrendFollowingStrategy
from model import recommend_strategy

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Bitcoin Trading Strategy Analyzer"),
    dcc.Dropdown(
        id='strategy-dropdown',
        options=[
            {'label': 'Momentum', 'value': 'Momentum'},
            {'label': 'Mean Reversion', 'value': 'Mean Reversion'},
            {'label': 'Trend Following', 'value': 'Trend Following'},
            {'label': 'AI Recommendation', 'value': 'AI Recommendation'}
        ],
        value='Momentum'
    ),
    html.Div(id='backtest-result'),
    dcc.Graph(id='performance-graph')
])

@app.callback(
    [Output('backtest-result', 'children'),
     Output('performance-graph', 'figure')],
    [Input('strategy-dropdown', 'value')]
)
def update_result(strategy_choice):
    # AI recommendation logic
    if strategy_choice == "AI Recommendation":
        strategy_name = recommend_strategy()
    else:
        strategy_name = strategy_choice

    final_value = run_backtest(MomentumStrategy if strategy_name == "Momentum" else
                               MeanReversionStrategy if strategy_name == "Mean Reversion" else
                               TrendFollowingStrategy)
    
    # Prepare graph data (example with dummy performance data)
    fig = go.Figure(data=[go.Scatter(x=[1, 2, 3, 4], y=[1, 4, 9, 16], mode='lines+markers')])
    
    return f"Final Portfolio Value: ${final_value:.2f}", fig

if __name__ == '__main__':
    app.run_server(debug=True)
