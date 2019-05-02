var config = require('./webpack.config');
const webpack = require('webpack');

const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const autoprefixer = require('autoprefixer');

const styleRule = {
  test: /\.(sa|sc|c)ss$/,
  use: [
    'css-hot-loader',
    MiniCssExtractPlugin.loader,
    { loader: 'css-loader', options: { sourceMap: true } },
    { loader: 'postcss-loader', options: { plugins: () => [autoprefixer({ browsers: ['last 2 versions'] })] } },
    'sass-loader'
  ]
};

const dev_url='http://localhost:3000'
config.entry.concat([
  'webpack-dev-server/client?'+dev_url, // WebpackDevServer host and port
  'webpack/hot/only-dev-server'         // "only" prevents reload on syntax errors];
])

config.output.publicPath  = dev_url+'/'

config.module = {rules: [styleRule]};

config.plugins.unshift(new BundleTracker({filename: './webpack-stats.production.json'}));
config.plugins.concat([
  new webpack.HotModuleReplacementPlugin(),
  new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
]);

config.devServer = {
  hot: true,
  inline: true,
  historyApiFallback: true,
  headers: {
    "Access-Control-Allow-Origin": "http://localhost:8000",
  },
  host: '0.0.0.0',
  port: 3000
}

module.exports = config
